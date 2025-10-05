import os
from rich import print
from openai import OpenAI
from openai.types import Model
import dt_llm_utility as utility

BASE_URL: str = "https://openrouter.ai/api/v1"
KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


def sort_function(model: dict):
    """
    Sort function.
    """

    return model["id"]


os.system(command="cls" if os.name == "nt" else "clear")

api_key: str | None = utility.get_key_value(
    key=KEY_NAME_OPENAI_API_KEY,
)

# client = OpenAI()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

models: list[Model] = client.models.list().data

# print(data)  # Test
# exit()  # Test

suported_models: list[dict] = []

for model in models:
    if not model.model_extra:
        continue

    pricing_prompt: float = float(model.model_extra["pricing"]["prompt"])
    pricing_completion: float = float(model.model_extra["pricing"]["completion"])

    if pricing_prompt != 0 or pricing_completion != 0:
        continue

    modality: str = model.model_extra["architecture"]["modality"]
    context_length = model.model_extra["top_provider"]["context_length"]
    max_completion_tokens = model.model_extra["top_provider"]["max_completion_tokens"]

    suported_model: dict = {
        "id": model.id,
        # "id": model.name,
        "modality": modality,
        "context_length": context_length,
        "max_completion_tokens": max_completion_tokens,
    }

    suported_models.append(suported_model)

suported_models.sort(key=sort_function)

for index, suported_model in enumerate(suported_models):
    fixed_index: str = str(index + 1).rjust(3, " ")
    fixed_id = str(suported_model["id"]).ljust(65, " ")
    fixed_modality = str(suported_model["modality"]).ljust(20, " ")
    fixed_context_length = str(suported_model["context_length"]).ljust(10, " ")
    fixed_max_completion_tokens = str(suported_model["max_completion_tokens"]).ljust(
        10, " "
    )

    print(
        fixed_index,
        fixed_id,
        fixed_modality,
        fixed_context_length,
        fixed_max_completion_tokens,
    )
