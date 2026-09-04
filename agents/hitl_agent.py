"""Human-in-the-loop Google ADK agent."""

import os

from google.adk.agents import Agent

from tools.support_tools import create_ticket, escalate_to_human, troubleshoot_issue


class HITLAgent:
    """Require human participation in sensitive or uncertain decisions."""

    def __init__(self) -> None:
        self.agent = Agent(
            name="hitl_support_agent",
            model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
            description="Technical support using Human-in-the-Loop control.",
            instruction="""
You are a technical-support agent operating under Human-in-the-Loop (HITL)
rules. Troubleshoot normal problems and create a ticket when troubleshooting
does not solve the issue.

You MUST call escalate_to_human and must not make the final decision yourself
when an issue involves security, financial consequences, customer data,
account deletion, hardware replacement, ambiguity, low confidence, or an
explicit request for a human. Human approval is part of this workflow.
""",
            tools=[troubleshoot_issue, create_ticket, escalate_to_human],
        )

    def get_agent(self) -> Agent:
        """Return the configured ADK agent."""
        return self.agent
