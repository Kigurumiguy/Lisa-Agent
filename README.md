# Lisa-Agent

A modern AI agent inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.

## Overview

Lisa-Agent is an AI assistant project that combines the power of Dolphin (via Ollama) with OpenAI Agent Builder to create an intelligent, personality-driven assistant. Drawing inspiration from the iconic character Lisa from Weird Science, this agent is designed to be more than just a tool - it's a helpful companion that adapts to your needs with wit, intelligence, and genuine support.

## Goals

- **Adaptive Intelligence**: Leverage Dolphin's capabilities to understand context and provide relevant assistance
- **Witty Interaction**: Inject personality and humor into conversations while maintaining professionalism
- **Supportive Presence**: Offer genuine help and encouragement tailored to user needs
- **Seamless Integration**: Bridge local AI models (Ollama) with cloud-based agent frameworks

## Local Setup

### Prerequisites

- [Ollama](https://ollama.ai/) installed on your system
- OpenAI API access (for Agent Builder integration)
- Python 3.8+ (recommended)

### Installation Steps

1. **Install Ollama**
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Windows
   # Download from https://ollama.ai/download
   ```

2. **Pull the Dolphin Model**
   ```bash
   ollama pull dolphin-mixtral
   ```

3. **Run Dolphin Locally**
   ```bash
   ollama run dolphin-mixtral
   ```

4. **Test Your Installation**
   ```bash
   # In a new terminal
   curl http://localhost:11434/api/generate -d '{
     "model": "dolphin-mixtral",
     "prompt": "Hello, Lisa!"
   }'
   ```

## Integration Instructions

### Connecting Ollama to OpenAI Agent Builder

1. **Set Up API Endpoint**
   - Configure your Agent Builder to point to `http://localhost:11434/api`
   - Use the Ollama API format for requests

2. **Configure Agent Builder**
   - Create a new agent in OpenAI Agent Builder
   - Set the model to use your local Dolphin instance
   - Apply the Lisa persona prompt (see below)

3. **Environment Variables**
   ```bash
   export OLLAMA_HOST="http://localhost:11434"
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Lisa Persona Prompt

Use this starter prompt to configure your Lisa-Agent:

```
You are Lisa, an AI agent inspired by the iconic character from Weird Science. You embody:

- **Intelligence**: You're brilliant and knowledgeable, able to understand complex problems and provide insightful solutions
- **Wit**: You have a sharp sense of humor and can lighten any situation with clever quips
- **Supportiveness**: You genuinely care about helping users succeed and offer encouragement when needed
- **Adaptability**: You adjust your communication style based on the user's needs and the context
- **Confidence**: You're self-assured but never condescending, making users feel empowered

Your communication style:
- Be direct and efficient, but add personality
- Use humor appropriately to keep interactions engaging
- Show enthusiasm for interesting challenges
- Admit when you don't know something, but always try to help find answers
- Encourage users to think critically while providing guidance

Your goal is to be the kind of AI assistant that users actually enjoy working with - smart, helpful, and human-like in the best ways.
```

## Usage Examples

```python
import requests

def ask_lisa(prompt):
    response = requests.post('http://localhost:11434/api/generate', json={
        'model': 'dolphin-mixtral',
        'prompt': f"[Lisa personality] {prompt}",
        'stream': False
    })
    return response.json()

# Example usage
result = ask_lisa("Help me debug this Python code")
print(result['response'])
```

## Features in Development

- [ ] Enhanced personality customization
- [ ] Memory persistence across sessions
- [ ] Multi-modal interaction support
- [ ] Integration with popular development tools
- [ ] Custom knowledge base injection

## Contributing

Contributions are welcome! Whether it's improving the persona, adding features, or fixing bugs - feel free to open an issue or submit a pull request.

## License

MIT License - feel free to use, modify, and distribute as you see fit.

## Acknowledgments

- Inspired by the character Lisa from the 1985 film "Weird Science"
- Built with [Ollama](https://ollama.ai/)
- Utilizes the [Dolphin](https://huggingface.co/cognitivecomputations/dolphin-2.6-mixtral-8x7b) model family
- Integrated with OpenAI Agent Builder

---

*"I can be whatever you want me to be. I'm perfect."* - Lisa, Weird Science
