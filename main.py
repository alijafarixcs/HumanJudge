"""Select the Google ADK support agent through ``AGENT_MODE``."""

import os

from dotenv import load_dotenv

from agents import HITLAgent, HOITLAgent, HOTLAgent

load_dotenv()


def create_agent(mode: str):
    """Create the ADK agent for a human-control mode."""
    factories = {
        "hitl": HITLAgent,
        "hotl": HOTLAgent,
        "hoitl": HOITLAgent,
        "hiotl": HOITLAgent,  # Tolerate this common transposition.
    }
    try:
        return factories[mode.lower()]().get_agent()
    except KeyError as error:
        raise ValueError("Unknown mode. Use: hitl, hotl, or hoitl") from error


MODE = os.getenv("AGENT_MODE", "hitl")
root_agent = create_agent(MODE)


class Main:
    """Print instructions for running the selected example agent."""

    @staticmethod
    def run() -> None:
        print("Human Control Patterns with Google ADK")
        print(f"Current mode: {MODE.upper()}")
        print("Run `adk web` or `adk run main` to interact with the agent.")


if __name__ == "__main__":
    Main.run()
