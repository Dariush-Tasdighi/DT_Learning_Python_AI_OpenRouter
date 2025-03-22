# **************************************************
KEY_NAME_API_KEY: str = "OPENAI_API_KEY"
BASE_URL: str = "https://openrouter.ai/api/v1"
MODEL_NAME: str = "google/gemma-3-27b-it:free"
# **************************************************


# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
# if not api_key:
#     print("API Key not found!")
#     exit()

# client = OpenAI(
#     api_key=api_key,
#     base_url=BASE_URL,
# )

# chat_completion = client.chat.completions.create(
#     model=MODEL_NAME,
#     messages=[
#         {
#             "role": "user",
#             "content": "Tell me a joke.",
#         }
#     ],
# )

# response = chat_completion.choices[0].message.content

# print("=" * 50)
# print("type of chat_completion:", type(chat_completion))
# print("-" * 50)
# print(chat_completion)
# print("-" * 50)
# print(response)
# print("=" * 50)
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# ChatCompletion(
#   id='gen-1742681078-jzoiZvBCsyUgbbth5iwl',
#   choices=[
#       Choice(
#           finish_reason='stop',
#           index=0,
#           logprobs=None,
#           message=ChatCompletionMessage(
#               content="Why don't skeletons ever go on dates?...",
#               refusal=None, role='assistant',
#               annotations=None,
#               audio=None,
#               function_call=None,
#               tool_calls=None
#           ),
#           native_finish_reason='STOP'
#       )
#   ],
#   created=1742681078,
#   model='google/gemma-3-27b-it',
#   object='chat.completion',
#   service_tier=None,
#   system_fingerprint=None,
#   usage=CompletionUsage(
#       completion_tokens=38,
#       prompt_tokens=6,
#       total_tokens=44,
#       completion_tokens_details=None,
#       prompt_tokens_details=None
#   ),
#   provider='Google AI Studio'
# )
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Simple Chatbot with System Role, Without History & Without Temperature
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# SYSTEM_PROMPT: str = "you are a helpful assistant."
# SYSTEM_MESSAGE = {"role": "system", "content": SYSTEM_PROMPT}

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()

# api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
# if not api_key:
#     print("API Key not found!")
#     exit()

# client = OpenAI(
#     api_key=api_key,
#     base_url=BASE_URL,
# )

# while True:
#     print("-" * 50)
#     user_prompt: str = input("User: ")

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         break

#     user_message = {"role": "user", "content": user_prompt}

#     # نکته مهم: ترتیب نوشتن پیغام‌ها و نقش‌ها اهمیت دارد
#     messages = [SYSTEM_MESSAGE, user_message]

#     chat_completion = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=messages,
#     )

#     response: str | None = chat_completion.choices[0].message.content

#     if not response:
#         response = "I'm sorry, I don't understand."

#     response = response.strip()

#     result = f"\nAI: {response}"
#     print(result)
#     # print(repr(result))
#     print("-" * 50)
#     print()
# **************************************************

# **************************************************
# Simple Chatbot with System Role & with History & with Temperature
# **************************************************
import os
from openai import OpenAI
from dotenv import load_dotenv

KEY_NAME_API_KEY: str = "OPENAI_API_KEY"
BASE_URL: str = "https://openrouter.ai/api/v1"

TEMPERATURE: float = 0.7
MODEL_NAME: str = "google/gemma-3-27b-it:free"

SYSTEM_PROMPT: str = "you are a helpful assistant."
SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}

os.system(command="cls")

print("Welcome to Dariush Tasdighi Chatbot!\n")

load_dotenv()

api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
if not api_key:
    print("API Key not found!")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

messages: list[dict] = []
messages.append(SYSTEM_MESSAGE)

while True:
    print("-" * 50)
    user_prompt: str = input("User: ")

    if user_prompt.lower() in ["bye", "exit", "quit"]:
        break

    user_message: dict = {"role": "user", "content": user_prompt}
    messages.append(user_message)

    chat_completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
    )

    assistant_answer: str | None = chat_completion.choices[0].message.content

    if not assistant_answer:
        messages.pop()
        assistant_answer = "I'm sorry, I don't understand!"
    else:
        assistant_answer = assistant_answer.strip()
        message_assistant = {"role": "assistant", "content": assistant_answer}
        messages.append(message_assistant)

    result = f"\nAI: {assistant_answer}"
    print(result)
    print("-" * 50)
    print()
# **************************************************
