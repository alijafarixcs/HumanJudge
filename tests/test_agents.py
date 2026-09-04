"""Unit tests that do not call an external model."""

import unittest

from main import create_agent
from tools.support_tools import (
    create_ticket,
    escalate_to_human,
    execute_automatic_action,
    notify_human,
    troubleshoot_issue,
)


class AgentFactoryTests(unittest.TestCase):
    def test_creates_each_control_mode(self) -> None:
        expected = {
            "hitl": "hitl_support_agent",
            "hotl": "hotl_support_agent",
            "hoitl": "hoitl_support_agent",
        }
        for mode, name in expected.items():
            with self.subTest(mode=mode):
                self.assertEqual(create_agent(mode).name, name)

    def test_rejects_unknown_mode(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown mode"):
            create_agent("unknown")


class SupportToolTests(unittest.TestCase):
    def test_tool_statuses(self) -> None:
        self.assertEqual(troubleshoot_issue("Wi-Fi")["status"], "success")
        self.assertEqual(create_ticket("network", "offline")["ticket_id"], "TICKET-12345")
        self.assertEqual(escalate_to_human("security", "breach")["status"], "escalated")
        self.assertEqual(notify_human("network", "restart")["status"], "notified")
        self.assertEqual(execute_automatic_action("restart")["status"], "success")


if __name__ == "__main__":
    unittest.main()
