import os
from rich import print
from openai import OpenAI
from openai.types import Model
import dt_llm_utility as utility

BASE_URL: str = "https://openrouter.ai/api/v1"
KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


def sort_key(model: dict):
    """
    Sort key.
    """

    return model["id"]


os.system(command="cls" if os.name == "nt" else "clear")

api_key: str = utility.get_key_value(
    key=KEY_NAME_OPENAI_API_KEY,
)

# client = OpenAI()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

all_models: list[Model] = client.models.list().data

# print(models)  # Test
# exit()  # Test

models: list[dict] = []

for model in all_models:
    if not model.model_extra:
        continue

    pricing_prompt: float = float(model.model_extra["pricing"]["prompt"])
    pricing_completion: float = float(model.model_extra["pricing"]["completion"])

    if pricing_prompt != 0 or pricing_completion != 0:
        continue

    modality: str = model.model_extra["architecture"]["modality"]
    context_length = model.model_extra["top_provider"]["context_length"]
    max_completion_tokens = model.model_extra["top_provider"]["max_completion_tokens"]

    new_model: dict = {
        "id": model.id,
        # "id": model.name,
        "modality": modality,
        "context_length": context_length,
        "max_completion_tokens": max_completion_tokens,
    }

    models.append(new_model)

models.sort(key=sort_key)

for index, model in enumerate(models):
    fixed_index: str = str(index + 1).rjust(3, " ")
    fixed_id = str(model["id"]).ljust(65, " ")
    fixed_modality = str(model["modality"]).ljust(20, " ")
    fixed_context_length = str(model["context_length"]).ljust(10, " ")
    fixed_max_completion_tokens = str(model["max_completion_tokens"]).ljust(10, " ")

    print(
        fixed_index,
        fixed_id,
        fixed_modality,
        fixed_context_length,
        fixed_max_completion_tokens,
    )
