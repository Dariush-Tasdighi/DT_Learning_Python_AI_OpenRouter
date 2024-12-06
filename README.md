# Using OpenRouter API

- https://openrouter.ai
- https://pypi.org/project/groq

## References

- https://openrouter.ai/chat
- https://openrouter.ai/models
- https://openrouter.ai/activity
- https://openrouter.ai/rankings
- https://openrouter.ai/settings/keys
- https://openrouter.ai/docs/quick-start

### Search Models and Useful Models

- https://openrouter.ai/models?max_price=0&q=llama
- https://openrouter.ai/meta-llama/llama-3.1-8b-instruct:free
- https://openrouter.ai/meta-llama/llama-3.1-70b-instruct:free
- https://openrouter.ai/meta-llama/llama-3.1-405b-instruct:free

## Setup Environment

- python -m venv .venv
- .\\.venv\Scripts\activate
- pip list
- python -m pip install -U pip
- pip install -U openai
- pip install -U python-dotenv
- pip list

Writing / Editing / Running Source Code!

- deactivate

## Create .env File (For Saving Passwords / API Keys / Access Tokens)

- In the root of folder, create a file with the name of '.env' and write the below code:
    - OPENAI_API_KEY="..."

## Fix PyLint Warnings

- Open the command palette: Press F1 [OR] CTRL + SHIFT + P
- Choose "Preference: Open Settins (JSON)"

```
{
    "security.workspace.trust.untrustedFiles": "open",
    "pylint.args": [
        "ignored-modules=cv2,streamlit,groq",
        "--extension-pkg-whitelist=cv2,pygame,numpy,streamlit,groq"
    ]
}
```
