# Using OpenRouter API

- https://openrouter.ai
- https://pypi.org/project/openai

### References

- https://openrouter.ai/chat
- https://openrouter.ai/models
- https://openrouter.ai/activity
- https://openrouter.ai/rankings
- https://openrouter.ai/settings/keys
- https://openrouter.ai/docs/quick-start

### Search Models and Useful Models

- https://openrouter.ai/meta-llama/llama-3.3-70b-instruct:free
- https://openrouter.ai/models?max_price=0&q=llama&order=newest

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
python -m pip install -U openai
```

```shell
python -m pip install -U python-dotenv
```

##### Just for Jupiter Notebook

```bash
python -m pip install -U ipython
```

```bash
python -m pip install -U ipykernel
```

```bash
python -m pip install -U ipywidgets
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