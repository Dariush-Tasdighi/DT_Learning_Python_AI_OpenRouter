# **************************************************
# Set the Default Model Name
# **************************************************
# model_name = "openai/gpt-3.5-turbo"
model_name = "meta-llama/llama-3.1-8b-instruct:free"
# model_name = "meta-llama/llama-3.1-70b-instruct:free"
# model_name = "meta-llama/llama-3.1-405b-instruct:free"
# **************************************************

# **************************************************
# Set the Default Base URL
# **************************************************
base_url = "https://openrouter.ai/api/v1"
# **************************************************

# **************************************************
# Because of sanctions! You must use VPN / DNS / ...
# **************************************************
import os
from openai import OpenAI
from dotenv import load_dotenv

os.system(command="cls")

# ********************
# *** Solution (1) ***
# ********************
# api_key = "abcde12345..."  # Bad Practice
# # print(api_key)
# client = OpenAI(base_url=base_url, api_key=api_key)
# ********************

# ********************
# *** Solution (2) ***
# ********************
# نکته مهم
# باید دستور ذیل نوشته شود
# هر چند که بر خلاف دستورات آتی
# مستقیما از آن استفاده نمی‌شود
# ********************
# load_dotenv()

# api_key = os.getenv(key="OPENAI_API_KEY")
# # print(api_key)
# api_key = os.environ.get(key="OPENAI_API_KEY")
# # print(api_key)

# client = OpenAI(base_url=base_url, api_key=api_key)
# ********************

# ********************
# *** Solution (3) ***
# ********************
load_dotenv()

client = OpenAI(base_url=base_url)
# ********************

chat_completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke.",
        }
    ],
)

print("-" * 50)
print("type of chat_completion:", type(chat_completion))
print("-" * 50)
print(chat_completion)
print("-" * 50)
# **************************************************

# **************************************************
# *** Value of 'chat_completion'
# **************************************************
# ChatCompletion(
# 	id='gen-1733514102-PUcbwXxtIDbgsnIIEOrL',
# 	choices=
# 	[
# 		Choice(
# 			finish_reason='stop',
# 			index=0,
# 			logprobs=None,
# 			message=ChatCompletionMessage(
# 				content="Here's a joke...",
# 				refusal='',
# 				role='assistant',
# 				audio=None,
# 				function_call=None,
# 				tool_calls=None
# 			)
# 		)
# 	],
# 	created=1733514102,
# 	model='meta-llama/llama-3.1-8b-instruct',
# 	object='chat.completion',
# 	service_tier=None,
# 	system_fingerprint=None,
# 	usage=CompletionUsage(
# 		completion_tokens=25,
# 		prompt_tokens=15,
# 		total_tokens=40,
# 		completion_tokens_details=None,
# 		prompt_tokens_details=None
# 	),
# 	provider='DeepInfra'
# )
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = OpenAI(base_url=base_url)

# chat_completion = client.chat.completions.create(
#     model=model_name,
#     messages=[
#         {
#             "role": "user",
#             "content": "Tell me a joke.",
#         }
#     ],
# )

# response = chat_completion.choices[0].message.content
# print("-" * 50)
# print(response)
# print("-" * 50)
# **************************************************

# **************************************************
# Chatbot with System Role
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# load_dotenv()
# client = OpenAI(base_url=base_url)

# while True:
#     print("-" * 50)
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     message_user = {"role": "user", "content": prompt}
#     message_system = {"role": "system", "content": "you are a helpful assistant."}

#     # نکته مهم: ترتیب نوشتن پیغام‌ها و نقش‌ها اهمیت دارد
#     messages = [message_system, message_user]

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages
#     )

#     response = chat_completion.choices[0].message.content

#     result = f"\nAI: {response}\n"
#     print(result)
# **************************************************

# **************************************************
# Chatbot with System Role & with History & with Temperature
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# temperature = 0.5

# messages = []
# message_system = {"role": "system", "content": "you are a helpful assistant."}
# messages.append(message_system)

# load_dotenv()
# client = OpenAI(base_url=base_url)

# while True:
#     print("-" * 50)
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     message_user = {"role": "user", "content": prompt}
#     messages.append(message_user)

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages, temperature=temperature
#     )

#     response = chat_completion.choices[0].message.content

#     message_assistant = {"role": "assistant", "content": response}
#     messages.append(message_assistant)

#     result = f"\nAI: {response}\n"
#     print(result)
# **************************************************

# **************************************************
# Translator Assistant Chatbot with System Role
# without History & without Temperature
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# print("Welcome to Dariush Tasdighi Chatbot!\n")

# temperature = 0.0  # Note

# message_system = {
#     "role": "system",
#     "content": """You are a translator assistant from english language to persian language.
# If user write just one english word, you must just translate it to persian language.
# after of this translation, you must not translate anything and your answers must be just in english language.
# You must write the pronounciation of user english word.
# You must write the type of user english word, for example: noun, verb and so on.
# You must write 5 synonyms for user english word.
# you must write 2 antonyms for user english word.
# you must write 2 short sentences that has the user english word.""",
# }

# load_dotenv()
# client = OpenAI(base_url=base_url)

# while True:
#     print("-" * 50)
#     prompt = input("User: ")

#     if prompt.lower() in ["quit", "exit"]:
#         break

#     messages = []
#     messages.append(message_system)

#     message_user = {"role": "user", "content": prompt}
#     messages.append(message_user)

#     chat_completion = client.chat.completions.create(
#         model=model_name, messages=messages, temperature=temperature
#     )

#     response = chat_completion.choices[0].message.content

#     result = f"\nAI: {response}\n"
#     print(result)
# **************************************************

# **************************************************
# Get OpenRouter Models List
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# client = OpenAI(base_url=base_url)

# print("-" * 50)
# models = client.models
# print("Type of models:", type(models))

# print("-" * 50)
# list = models.list()
# print("Type of list:", type(list))

# print("-" * 50)
# data = list.data
# print("Type of list:", type(data))

# # print("-" * 50)
# # print(models)

# # print("-" * 50)
# # print(list)

# # print("-" * 50)
# # print(data)

# # print("-" * 50)
# # for model in data:
# #     print(model)

# # print("-" * 50)
# # new_data = []
# # for model in data:
# #     new_data.append(model.id)

# print("-" * 50)
# new_data = [item.id for item in data]

# new_data.sort()
# for model in new_data:
#     print(model)

# print("-" * 50)
# **************************************************
