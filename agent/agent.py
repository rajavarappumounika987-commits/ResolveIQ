import os

from groq import Groq
from dotenv import load_dotenv

from .decision import analyze_escalation
from .prompts import SYSTEM_PROMPT, build_agent_prompt


load_dotenv()


def run_agent(ticket, historical_cases):
    """
    Run the ResolveIQ AI escalation agent.
    """

    # Build context from the current ticket and recalled history
    agent_prompt = build_agent_prompt(
        ticket,
        historical_cases
    )

    # Create Groq client
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not configured."
        )

    client = Groq(api_key=api_key)

    # Ask the LLM to analyze the case
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": agent_prompt
            }
        ],
        temperature=0.2,
    )

    ai_reasoning = response.choices[0].message.content

    # Keep our structured escalation logic as a safety layer
    decision = analyze_escalation(
        ticket,
        historical_cases
    )

    return {
        **decision,
        "agent": "ResolveIQ",
        "prompt_version": "v3",
        "ai_reasoning": ai_reasoning
    }
