import os
import time
from rich import print
from openai import OpenAI
import dt_llm_utility as utility
from openai.types.chat import ChatCompletion

EXIT_COMMANDS: list[str] = [
    "bye".strip().lower(),
    "exit".strip().lower(),
    "quit".strip().lower(),
]

USER_QUESTION: str = "User: "
MESSAGE_NO_CONTENT_RECEIVED: str = "[-] No content received!"

KEY_NAME_ROLE = "role".strip().lower()
KEY_NAME_CONTENT = "content".strip().lower()
KEY_NAME_TEMPRETURE = "temperature".strip().lower()

ROLE_USER: str = "user".strip().lower()
ROLE_SYSTEM: str = "system".strip().lower()
ROLE_ASSISTANT: str = "assistant".strip().lower()

TEMPERATURE: float = 0.7
# NEW
KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"
BASE_URL: str = "https://openrouter.ai/api/v1".strip().lower()
MODEL_NAME: str = "google/gemma-3-27b-it:free".strip().lower()

SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_MESSAGE: dict = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def chat(
    messages: list[dict],
    think: bool = False,
    notify: bool = False,
    base_url: str = BASE_URL,
    api_key: str | None = None,
    model_name: str = MODEL_NAME,
    temperature: float = TEMPERATURE,
) -> tuple[str | None, int, int]:
    """Chat function."""

    # NEW
    if not api_key:
        api_key = utility.get_key_value(
            key=KEY_NAME_OPENAI_API_KEY,
        )

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    if notify:
        print(f"OpenAI chat started ({model_name})...")

    response: ChatCompletion = client.chat.completions.create(
        stream=False,
        model=model_name,
        messages=messages,  # type: ignore
        # NEW
        temperature=temperature,
    )

    if notify:
        print(f"OpenAI chat finished ({model_name}).")

    assistant_answer: str | None = response.choices[0].message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if response and assistant_answer:
        if response.usage:
            prompt_tokens = response.usage.prompt_tokens
        if response.usage:
            completion_tokens = response.usage.completion_tokens

    return assistant_answer, prompt_tokens, completion_tokens


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    messages: list[dict] = []
    messages.append(SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input(USER_QUESTION).strip()

        if user_prompt.lower() in EXIT_COMMANDS:
            break

        user_message: dict = {
            KEY_NAME_ROLE: ROLE_USER,
            KEY_NAME_CONTENT: user_prompt,
        }
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = chat(
            messages=messages,
        )

        response_time: float = time.time() - start_time

        if not assistant_answer:
            messages.pop()
            assistant_answer = MESSAGE_NO_CONTENT_RECEIVED
        else:
            assistant_message: dict = {
                KEY_NAME_ROLE: ROLE_ASSISTANT,
                KEY_NAME_CONTENT: assistant_answer,
            }
            messages.append(assistant_message)

        print("-" * 50)
        print(assistant_answer)
        print("-" * 50)
        print("Prompt Tokens (Input):", prompt_tokens)
        print("-" * 50)
        print("Completion Tokens (Output):", completion_tokens)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)
        print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        # Log 'error'
        print(f"[-] {error}")
