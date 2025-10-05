# Learning OpenRouter

- Package: 'rich'
    - https://pypi.org/project/rich
    - https://github.com/Textualize/rich
    - https://rich.readthedocs.io/en/latest

- Package: 'openai'
    - https://pypi.org/project/openai
    - https://github.com/openai/openai-python

- Package: 'dotenv-python'
    - https://pypi.org/project/dotenv-python
    - https://github.com/TsuiJie/dotenv-python

---

### References

- https://openrouter.ai
    - https://openrouter.ai/chat
    - https://openrouter.ai/models
    - https://openrouter.ai/activity
    - https://openrouter.ai/rankings
    - https://openrouter.ai/settings/keys
    - https://openrouter.ai/docs/quick-start

- https://openrouter.ai/models?max_price=0&order=newest

---

### Setup Environment

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```

```bash
python -m pip list
```

```bash
python -m pip install -U pip
```

```bash
python -m pip install -U rich
```

```bash
python -m pip install -U openai
```

```shell
python -m pip install -U python-dotenv
```

```bash
python -m pip list
```

Now! We Create / Modify / Delete / Run the Source Codes...

```bash
deactivate
```

---

### Create '.env' File (For Saving API Keys)

- In the root of project, create a file, with the name of '.env', and write the key name and value:
    - OPENAI_API_KEY="..."

---
