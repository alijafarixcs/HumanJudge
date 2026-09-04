"""Human-on-the-loop Google ADK agent."""

import os

from google.adk.agents import Agent

from tools.support_tools import (
    create_ticket,
    execute_automatic_action,
    notify_human,
    troubleshoot_issue,
)


class HOTLAgent:
    """Operate autonomously while a human supervisor monitors decisions."""

    def __init__(self) -> None:
        self.agent = Agent(
            name="hotl_support_agent",
            model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
            description="Technical support using Human-on-the-Loop control.",
            instruction="""
You are a technical-support agent operating under Human-on-the-Loop (HOTL)
rules. Troubleshoot and resolve normal issues autonomously. Create tickets and
execute permitted automatic actions when useful.

Call notify_human for unusual situations, financial impact, repeated action
failures, security concerns, possible customer-data impact, low confidence, or
an important automated decision. Notification normally does not stop the
action; the human supervisor may intervene.
""",
            tools=[
                troubleshoot_issue,
                create_ticket,
                notify_human,
                execute_automatic_action,
            ],
        )

    def get_agent(self) -> Agent:
        """Return the configured ADK agent."""
        return self.agent
