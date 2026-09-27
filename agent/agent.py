from .decision import analyze_escalation
from .prompts import SYSTEM_PROMPT


def run_agent(ticket, historical_cases):
    """
    Run the ResolveIQ decision engine.

    Parameters:
        ticket: dictionary containing the current support issue
        historical_cases: list of relevant previous cases

    Returns:
        dictionary containing the AI recommendation
    """

    result = analyze_escalation(
        ticket,
        historical_cases
    )

    result["agent"] = "ResolveIQ"
    result["prompt_version"] = "v1"

    return result
