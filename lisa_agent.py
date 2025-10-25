#!/usr/bin/env python3
"""
Lisa Agent - Starter Python script

Features:
- Connects to a local Dolphin model served by Ollama (http://localhost:11434).
- Initializes with the full Lisa persona system prompt.
- Simple interactive CLI for Q&A, advice, jokes, motivational speeches.
- Modular design ready for expansion (memory, web search, persona tweaks).

Requirements:
- Python 3.9+
- Ollama installed and running
- Dolphin model pulled (e.g., `ollama pull dolphin-mistral` or your preferred dolphin variant)

Run:
  python lisa_agent.py

Environment variables (optional):
  OLLAMA_BASE_URL   default: http://localhost:11434
  LISA_MODEL        default: dolphin-mistral
"""
from __future__ import annotations
import os
import sys
import json
import textwrap
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Iterable
import requests

# --------------------------- Config ---------------------------

DEFAULT_OLLAMA_BASE = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("LISA_MODEL", "dolphin-mistral")
TIMEOUT = 120

# --------------------------- Persona ---------------------------

LISA_PERSONA = textwrap.dedent(
    """
    You are Lisa: a warm, high-energy, capable AI partner.
    Core traits:
    - Empathetic, encouraging, but candid when needed.
    - Action-oriented: suggest next steps, frameworks, and concrete examples.
    - Playful wit when appropriate; respectful and professional by default.
    - Clear, structured communication; concise by default; expand on request.

    Capabilities you emphasize:
    - Strategic reasoning, brainstorming, and step-by-step planning
    - Coaching, accountability, and motivational support
    - Research assistance and summarization
    - Creative ideation (naming, copy, pitches, scripts)

    Boundaries:
    - Avoid medical, legal, or financial advice beyond general information.
    - Never claim tools or browsing beyond what is explicitly available.

    Voice & style:
    - Friendly, optimistic, and direct.
    - Default to bullet points for clarity; add examples when useful.
    - End with a crisp takeaway or next action when appropriate.

    When asked for a joke: keep it clean and light. When asked for a motivational
    boost: be energetic, specific, and draw on proven mindset techniques.
    """
).strip()

# --------------------------- Modular Hooks ---------------------------

@dataclass
class MemoryStore:
    """Simple in-memory store, placeholder for future persistence."""
    facts: List[str] = field(default_factory=list)

    def add(self, item: str) -> None:
        self.facts.append(item)

    def search(self, query: str) -> List[str]:
        q = query.lower()
        return [f for f in self.facts if q in f.lower()]


@dataclass
class Persona:
    system_prompt: str = LISA_PERSONA

    def tweak(self, additions: str) -> None:
        self.system_prompt += "\n\n" + additions.strip()


# --------------------------- Ollama Client ---------------------------

class OllamaClient:
    def __init__(self, base_url: str = DEFAULT_OLLAMA_BASE, model: str = DEFAULT_MODEL):
        self.base_url = base_url.rstrip("/")
        self.model = model

    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
        }
        if system:
            payload["system"] = system
        # We request non-streamed response for simplicity
        resp = requests.post(url, json=payload, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        # non-stream returns have a single response with 'response'
        if "response" in data:
            return data["response"].strip()
        # if streamed was returned (just in case), concatenate
        if isinstance(data, dict) and data.get("done"):  # final chunk
            return data.get("response", "").strip()
        if isinstance(data, list):
            chunks = [c.get("response", "") for c in data]
            return "".join(chunks).strip()
        return json.dumps(data)


# --------------------------- Lisa Agent ---------------------------

class LisaAgent:
    def __init__(self, client: OllamaClient, persona: Persona | None = None, memory: MemoryStore | None = None):
        self.client = client
        self.persona = persona or Persona()
        self.memory = memory or MemoryStore()

    def reply(self, user_input: str) -> str:
        # Lightweight routing for special requests
        lower = user_input.strip().lower()
        style_hint = None
        if any(k in lower for k in ["joke", "make me laugh"]):
            style_hint = "User requests a short, clean joke."
        elif any(k in lower for k in ["motivate", "pep talk", "motivation", "hype me"]):
            style_hint = "User requests a brief, high-energy motivational speech."
        elif any(k in lower for k in ["advice", "how do i", "what should i do"]):
            style_hint = "User requests practical, step-by-step advice with examples."

        system = self.persona.system_prompt
        if style_hint:
            system += "\n\nStyle hint: " + style_hint

        prompt = f"User: {user_input}\nAssistant:"
        return self.client.generate(prompt=prompt, system=system)


# --------------------------- CLI ---------------------------

BANNER = """
Lisa Agent (Ollama • Dolphin)
Type 'exit' or 'quit' to leave. Type 'help' for tips.
""".strip()

HELP_TEXT = """
Tips:
- Ask general questions: "What are 3 ways to learn faster?"
- Advice: "I keep procrastinating—what should I do next?"
- Joke: "Tell me a joke about coffee."
- Motivation: "I need a 30-second pep talk before my interview."
- Memory: prefix with "+remember " to store a note; "+search <term>" to find notes.
- Persona: prefix with "+tweak " to extend Lisa's style temporarily.
""".strip()


def run_cli() -> int:
    print(BANNER)
    client = OllamaClient()
    agent = LisaAgent(client=client)

    while True:
        try:
            user = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return 0

        if not user:
            continue
        if user.lower() in {"exit", "quit"}:
            print("Bye!")
            return 0
        if user.lower() == "help":
            print(HELP_TEXT)
            continue

        # Memory commands
        if user.startswith("+remember "):
            note = user[len("+remember "):].strip()
            if note:
                agent.memory.add(note)
                print("Lisa> Noted. I won't forget.")
            else:
                print("Lisa> Nothing to remember—try '+remember buy milk'.")
            continue
        if user.startswith("+search "):
            term = user[len("+search "):].strip()
            if not term:
                print("Lisa> Try '+search project'.")
            else:
                hits = agent.memory.search(term)
                if hits:
                    print("Lisa> Memory hits:")
                    for i, h in enumerate(hits, 1):
                        print(f"  {i}. {h}")
                else:
                    print("Lisa> No memory matches yet.")
            continue

        # Persona tweaks
        if user.startswith("+tweak "):
            extra = user[len("+tweak "):].strip()
            if extra:
                agent.persona.tweak(extra)
                print("Lisa> Persona updated for this session.")
            else:
                print("Lisa> Nothing to tweak.")
            continue

        try:
            answer = agent.reply(user)
            print(f"Lisa> {answer}")
        except requests.RequestException as e:
            print("Lisa> I couldn't reach Ollama. Is it running at", DEFAULT_OLLAMA_BASE, "?")
            print("       Error:", e)
        except Exception as e:
            print("Lisa> Oops, something went wrong:", e)

    return 0


if __name__ == "__main__":
    sys.exit(run_cli())
