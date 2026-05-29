# Building with the Claude API

A hands-on course for learning how to build applications using the Anthropic Claude API.

## Overview

This course walks through practical examples of interacting with Claude, Anthropic's AI assistant, using the official Python SDK. You'll learn how to structure API requests, manage conversations, and build chat-based applications.

## Course Notebooks

| Notebook | Description |
|----------|-------------|
| `001_requests.ipynb` | Introduction to making basic API requests to Claude |
| `002_requests.ipynb` | Intermediate request patterns and response handling |
| `003_requests.ipynb` | Building multi-turn conversations with message history |

## Prerequisites

- Python 3.8+
- An [Anthropic API key](https://console.anthropic.com/)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/biojoel21/anthropic-course.git
   cd anthropic-course
   ```

2. **Install dependencies**
   ```bash
   pip install anthropic python-dotenv
   ```

3. **Configure your API key**

   Create a `.env` file in the root of the project:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Key Concepts Covered

- **API Client Setup** – Initializing the Anthropic client and selecting a model
- **Message Formatting** – Structuring `user` and `assistant` messages correctly
- **Multi-turn Chat** – Managing conversation history with a messages list
- **Parameters** – Controlling model behavior with `max_tokens`, `temperature`, and `system` prompts

## Example Usage

```python
from anthropic import Anthropic

client = Anthropic()

messages = []
messages.append({"role": "user", "content": "Hello, Claude!"})

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=messages
)

print(response.content[0].text)
```

## Model

This course uses **`claude-sonnet-4-6`** as the default model.

## Resources

- [Anthropic Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/en/api/)
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)

## License

This project is intended for educational purposes.
