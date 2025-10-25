# Lisa-Agent

A modern AI agent inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.

## Overview

Lisa-Agent is an AI assistant project that combines the power of Dolphin (via Ollama) with a modular Python framework to create an intelligent, personality-driven assistant. Drawing inspiration from the iconic character Lisa from Weird Science, this agent is designed to be more than just a tool - it's a helpful companion that adapts to your needs with wit, intelligence, and genuine support.

## Quick Start

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.ai/) installed
- Dolphin model pulled (e.g., `dolphin-mistral` or your preferred variant)

### 1. Install Ollama

```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Pull and Start Dolphin Model

```bash
# Pull the model
ollama pull dolphin-mistral

# Start Ollama server (if not running)
ollama serve
```

### 3. Run the Lisa Agent

```bash
# Clone this repository
git clone https://github.com/Kigurumiguy/Lisa-Agent.git
cd Lisa-Agent

# Install dependencies
pip install requests

# Run Lisa
python lisa_agent.py
```

### 4. Start Interacting

```
Lisa Agent (Ollama • Dolphin)
Type 'exit' or 'quit' to leave. Type 'help' for tips.

You> What are 3 ways to learn faster?
Lisa> Here are three evidence-based techniques to accelerate learning:

• **Active recall**: Test yourself frequently instead of just re-reading...
```

## Features

### Core Capabilities
- **Q&A and Advice**: Ask anything and get thoughtful, structured responses
- **Motivational Support**: Request pep talks and encouragement
- **Entertainment**: Ask for clean jokes and light conversation
- **Memory System**: Store and search notes with `+remember` and `+search`
- **Persona Tweaks**: Adjust Lisa's style with `+tweak` commands

### CLI Commands

- `help` - Show available commands
- `+remember <note>` - Store a fact or note
- `+search <term>` - Search stored memories
- `+tweak <style>` - Temporarily adjust Lisa's persona
- `exit` or `quit` - Leave the session

### Example Interactions

```
You> Tell me a joke about programming
Lisa> Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You> I need motivation before my presentation
Lisa> You've got this! Remember: you know your material better than anyone in that room...

You> +remember I have a meeting with Sarah on Friday
Lisa> Noted. I won't forget.

You> +search meeting
Lisa> Memory hits:
  1. I have a meeting with Sarah on Friday
```

## Configuration

### Environment Variables

- `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
- `LISA_MODEL` (default: `dolphin-mistral`)

### Custom Model

```bash
# Use a different Dolphin variant
export LISA_MODEL="dolphin-mixtral"
python lisa_agent.py
```

## Architecture

### Modular Design

The agent is built with expansion in mind:

- **`OllamaClient`**: Handles communication with local Ollama server
- **`Persona`**: Manages Lisa's personality and system prompts
- **`MemoryStore`**: Simple in-memory storage (ready for persistence upgrades)
- **`LisaAgent`**: Core agent orchestration and routing

### Future Expansion Points

- **Persistent Memory**: Replace in-memory store with SQLite/JSON files
- **Web Search**: Add search capabilities via APIs
- **Tool Integration**: Connect external tools and services
- **Voice Interface**: Add speech-to-text and text-to-speech
- **GUI**: Build a desktop or web interface

## Goals

- **Adaptive Intelligence**: Leverage Dolphin's capabilities to understand context and provide relevant assistance
- **Witty Interaction**: Inject personality and humor into conversations while maintaining professionalism
- **Supportive Presence**: Offer genuine help and encouragement tailored to user needs
- **Local-First**: Run entirely on your hardware with optional cloud integrations

## Contributing

Feel free to submit issues, feature requests, or pull requests! This project is designed to be hackable and extensible.

## License

MIT License - see the code for details.

---

*"I'm Lisa. I do things that are good for you and bad for people who aren't nice to you."* - Building an AI companion that's got your back. 🚀
