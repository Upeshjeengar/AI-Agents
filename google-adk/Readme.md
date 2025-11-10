How to Run 
```
python3 -m venv .venv 
source .venv/bin/activate
pip3 install google-adk 
pip3 install litellm 
adk run my_agent
adk web  //for web version of agent
```

### LLM Used
```
model = LiteLlm(
    model = "openai/llama3.1",
    api_key = "ollama",
    base_url = "http://localhost:11434/v1"  
)
```


If you want to use Google's LLM, replace   
store your API's in `.env` and load it with:
```
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

```model = gemini-2.0-flash```  
or any of the [google's model](https://ai.google.dev/gemini-api/docs/models)

If you want to use any online LLMs from API, You can see [litellm's](https://docs.litellm.ai/docs/providers/) documentation on how to use any popular LLM 
