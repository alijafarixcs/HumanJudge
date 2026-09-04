# Human Control Agents with Google ADK

Three technical-support agents demonstrating different levels of human control
with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

> These are control architectures, not special ADK agent types. Each example
> uses a regular ADK `Agent`; its instructions, tools, and escalation behavior
> determine how humans participate.

## Control models

| Model | Human role | Runtime behavior |
| --- | --- | --- |
| **HITL** — Human-in-the-Loop | Decision maker | Sensitive or uncertain actions stop and escalate for human review. |
| **HOTL** — Human-on-the-Loop | Supervisor | The agent acts autonomously and notifies a human who can intervene. |
| **HOITL** — Human-out-of-the-Loop | Not involved | A low-risk, predefined workflow runs autonomously. |

```text
Low autonomy                                            High autonomy

HITL                       HOTL                         HOITL
AI -> human decision       AI -> action                AI -> action
          -> continue             -> human monitors           (autonomous)
```

## Project structure

```text
agents/
├── hitl_agent.py
├── hotl_agent.py
└── hoitl_agent.py
tools/
└── support_tools.py
agent.py
main.py
requirements.txt
.env.example
```

## Setup

Python 3.11 or newer is required.

```powershell
pyenv local 3.11
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Set your Gemini API key in `.env`. Never commit the real `.env` file.

## Select a mode

Set `AGENT_MODE` in `.env` to one of:

```dotenv
AGENT_MODE=hitl
# AGENT_MODE=hotl
# AGENT_MODE=hoitl
```

You can also change `GOOGLE_MODEL` without editing the source.

## Run

Start the ADK developer UI from the directory containing this project:

```powershell
adk web
```

Or use the terminal runner:

```powershell
adk run .
```

Run `python main.py` to display the selected mode without starting a chat.

## Important limitations

The tools are deterministic demonstrations: tickets are not persisted and
automatic actions do not affect a real system. Production use needs durable
storage, authentication, authorization, audit logging, idempotency, timeouts,
monitoring, and tested escalation paths. Do not use HOITL for high-risk work.

## License

Released under the [MIT License](LICENSE).
