# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# KEY_NAME_API_KEY: str = "OPENAI_API_KEY"
# BASE_URL: str = "https://openrouter.ai/api/v1"

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

# models = client.models.list().data

# for model in models:
#     print(model)
# **************************************************


# **************************************************
# import os
# from openai import OpenAI
# from openai.types import Model
# from dotenv import load_dotenv

# KEY_NAME_API_KEY: str = "OPENAI_API_KEY"
# BASE_URL: str = "https://openrouter.ai/api/v1"

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

# models = client.models.list().data

# first_model: Model = models[0]

# print("=" * 50)
# print(first_model)
# print("-" * 50)
# print("Id:", first_model.id)
# print("-" * 50)
# print("Owned By:", first_model.owned_by)
# print("-" * 50)
# print("Prompt Price:", first_model.model_extra["pricing"]["prompt"])
# print("-" * 50)
# print("Modality:", first_model.model_extra["architecture"]["modality"])
# print("=" * 50)
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# Model(
#   id='openai/o1-pro',
#   created=1742423211,
#   object=None,
#   owned_by=None,
#   name='OpenAI: o1-pro',
#   description='The o1 series of models are trained with reinforcement learning to think before they answer and perform complex reasoning. The o1-pro model uses more compute to think harder and provide consistently better answers.',
#   context_length=200000,
#   architecture={
#       'modality': 'text+image->text',
#       'tokenizer': 'GPT',
#       'instruct_type': None
#   },
#   pricing={
#       'prompt': '0.00015',
#       'completion': '0.0006',
#       'image': '0.21675',
#       'request': '0',
#       'input_cache_read': '0',
#       'input_cache_write': '0',
#       'web_search': '0',
#       'internal_reasoning': '0'
#   },
#   top_provider={
#       'context_length': 200000,
#       'max_completion_tokens': 100000,
#       'is_moderated': True
#   },
#   per_request_limits=None
# )
# **************************************************
# **************************************************
# **************************************************


# **************************************************
import os
from openai import OpenAI
from openai.types import Model
from dotenv import load_dotenv

KEY_NAME_API_KEY: str = "OPENAI_API_KEY"
BASE_URL: str = "https://openrouter.ai/api/v1"


def sort_function(model: Model):
    return model["id"]


os.system(command="cls")

load_dotenv()

api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
if not api_key:
    print("API Key not found!")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

data = client.models.list().data

suported_models = []
for model in data:
    modality = model.model_extra["architecture"]["modality"]
    price: float = float(model.model_extra["pricing"]["prompt"])

    suported_model: dict = {
        "id": model.id,
        "price": price,
        "modality": modality,
        "owned_by": model.owned_by,
    }

    if price == 0.0:
        suported_models.append(suported_model)

suported_models.sort(key=sort_function)

for model in suported_models:
    print(
        "Id:",
        str(model["id"]).ljust(55, " "),
        "Modality:",
        str(model["modality"]).ljust(20, " "),
        "Price:",
        str(model["price"]),
    )
# **************************************************
