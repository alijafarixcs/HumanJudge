"""Deterministic example tools for technical-support workflows."""


def troubleshoot_issue(issue: str) -> dict[str, str]:
    """Analyze a technical-support issue and return initial guidance."""
    return {
        "status": "success",
        "issue": issue,
        "report": (
            f"Initial troubleshooting completed for: {issue}. Restart the "
            "device, verify connections, and check for software or firmware updates."
        ),
    }


def create_ticket(issue_type: str, details: str) -> dict[str, str]:
    """Create an example support ticket."""
    return {
        "status": "success",
        "ticket_id": "TICKET-12345",
        "issue_type": issue_type,
        "details": details,
    }


def escalate_to_human(issue_type: str, details: str) -> dict[str, str]:
    """Escalate an issue to a human support specialist."""
    return {
        "status": "escalated",
        "issue_type": issue_type,
        "details": details,
        "message": "The issue has been escalated to a human specialist.",
    }


def notify_human(issue_type: str, decision: str) -> dict[str, str]:
    """Notify a human supervisor without stopping agent execution."""
    return {
        "status": "notified",
        "issue_type": issue_type,
        "decision": decision,
        "message": "Human supervisor has been notified.",
    }


def execute_automatic_action(action: str) -> dict[str, str]:
    """Simulate an approved automatic support action."""
    return {
        "status": "success",
        "action": action,
        "message": f"Automatic action executed: {action}",
    }
