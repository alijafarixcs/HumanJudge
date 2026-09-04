"""Human-out-of-the-loop Google ADK agent."""

import os

from google.adk.agents import Agent

from tools.support_tools import (
    create_ticket,
    execute_automatic_action,
    troubleshoot_issue,
)


class HOITLAgent:
    """Complete a predefined, low-risk workflow without human participation."""

    def __init__(self) -> None:
        self.agent = Agent(
            name="hoitl_support_agent",
            model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
            description="Autonomous support using Human-out-of-the-Loop control.",
            instruction="""
You are a fully autonomous technical-support agent operating under
Human-out-of-the-Loop (HOITL) rules. Independently troubleshoot the problem,
choose the best solution, and execute permitted automatic actions. If the
problem remains unresolved, create a ticket automatically. Complete the
predefined workflow without waiting for human approval. Use this autonomy only
for low-risk, well-defined support tasks.
""",
            tools=[troubleshoot_issue, create_ticket, execute_automatic_action],
        )

    def get_agent(self) -> Agent:
        """Return the configured ADK agent."""
        return self.agent
