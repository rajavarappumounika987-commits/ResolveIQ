from .decision import analyze_escalation
from .prompts import SYSTEM_PROMPT, build_agent_prompt


def run_agent(ticket, historical_cases):
    """
    Run the ResolveIQ escalation intelligence agent.

    The agent receives the current ticket and relevant historical
    cases recalled from memory.
    """

    # Build the context for the AI reasoning layer
    agent_prompt = build_agent_prompt(
        ticket,
        historical_cases
    )

    # Current decision engine
    result = analyze_escalation(
        ticket,
        historical_cases
    )

    result["agent"] = "ResolveIQ"
    result["prompt_version"] = "v2"
    result["system_prompt"] = SYSTEM_PROMPT
    result["agent_prompt"] = agent_prompt

    return result
