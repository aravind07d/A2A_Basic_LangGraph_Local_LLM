# Basic Agent-to-Agent (A2A) Example

This is a basic example of an Agent-to-Agent (A2A) system using **LangGraph** and **Ollama**.

## Overview

The system consists of two agents:
1.  **Generator**: Generates a short story or joke based on a given topic.
2.  **Critic**: Reviews the generated content and provides feedback.

## Prerequisites

1.  **Python 3.9+**
2.  **Ollama**: Installed and running locally.
    - Download from [ollama.com](https://ollama.com/)
    - Run `ollama serve` (usually runs in background)
    - Pull the model (default is `llama3`): `ollama pull llama3`

## Setup

1.  Install dependencies:
    ```bash
    # Create venv
    python -m venv .venv
    # Activate venv
    .venv\Scripts\activate
    # Install dependencies
    pip install -r requirements.txt
    ```

2.  (Optional) Configure settings:
    - You can create a `.env` file or modify `config/settings.py` to change the model or base URL.

## Usage

Run the main script:

```bash
python main.py --topic "Space Exploration"
```

## Structure

- `agents/`: Contains agent logic (Generator, Critic).
- `workflow/`: Contains LangGraph state and graph definition.
- `config/`: Configuration settings.
