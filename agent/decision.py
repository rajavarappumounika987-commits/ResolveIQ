def analyze_escalation(ticket, historical_cases):
    """
    Analyze a new support ticket against historical cases.
    """

    customer_id = ticket.get("customer_id")
    frustration = ticket.get("frustration", "medium").lower()

    if not historical_cases:
        return {
            "severity": "medium",
            "recurring_issue": False,
            "recommendation": "Standard troubleshooting",
            "reason": "No relevant historical cases were found."
        }

    failed_attempts = []
    successful_resolutions = []

    for case in historical_cases:
        result = case.get("result", "").lower()

        if result == "failed":
            failed_attempts.append(
                case.get("attempted_solution", "Unknown")
            )

        elif result == "resolved":
            successful_resolutions.append(
                case.get("resolution", "Unknown")
            )

    recurring_issue = len(historical_cases) >= 2

    if recurring_issue and len(failed_attempts) >= 2:

        recommendation = "Escalate to Payment Operations"

        reason = (
            f"Customer {customer_id} has a recurring issue. "
            f"Previous troubleshooting attempts failed: "
            f"{', '.join(failed_attempts)}."
        )

        severity = "high"

    elif successful_resolutions:

        recommendation = (
            f"Try previously successful resolution: "
            f"{successful_resolutions[-1]}"
        )

        reason = (
            "A relevant historical case contains a successful "
            "resolution that may apply to the current issue."
        )

        severity = "medium"

    else:

        recommendation = "Standard troubleshooting"

        reason = (
            "Historical cases were found, but there is not enough "
            "evidence to recommend escalation."
        )

        severity = "medium"

    if frustration == "high" and recurring_issue:
        severity = "high"

    return {
        "severity": severity,
        "recurring_issue": recurring_issue,
        "previous_failed_attempts": failed_attempts,
        "successful_resolutions": successful_resolutions,
        "recommendation": recommendation,
        "reason": reason
    }
