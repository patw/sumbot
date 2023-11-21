from fastapi import FastAPI
import threading

# Whip the llama into gear
from llama_cpp import Llama
llama_model = Llama(model_path="dolphin-2.1-mistral-7b.Q5_K_S.gguf", n_ctx=4096)
prompt_format = "<|im_start|>system\n{system}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant:"
DEFAULT_SYSTEM = "You are a helpful assistant who will always answer the question with only the data provided"
DEFAULT_PROMPT = "Describe the following {entity} data in a single paragraph, without saying it's a JSON object or including any URLs:"
DEFAULT_TOKENS = 512 # many words
DEFAULT_TEMP = 0.1 # very mild temp for more boring results
BAN_TOKEN = "<|im_end|>" 

# Prevent double gen crashes
data_lock = threading.Lock()

# Fast API init
app = FastAPI(
        title="SumBot",
        description="Send me a JSON record and say what kind of entity it is (movie, transaction, person) and I'll summarize it with an LLM",
        version="1.0",
        contact={
            "name": "Pat Wendorf",
            "email": "pat.wendorf@mongodb.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    }
)

# Endpoint to compare 2 images by URL and show similarity
@app.post("/summarize")
async def summarize_json_data(entity_type: str, input_json: str):

    # Build the prompt
    prompt = prompt_format.replace("{system}", DEFAULT_SYSTEM)
    prompt = prompt.replace("{prompt}", DEFAULT_PROMPT + " " + input_json)
    prompt = prompt.replace("{entity}", entity_type)
    prompt = prompt.replace("  ", "") # Too much whitespace slows it down?
    
    print(prompt)

    # Call the LLM and return
    with data_lock:
        llm_result = llama_model(prompt, max_tokens=DEFAULT_TOKENS, temperature=DEFAULT_TEMP)["choices"][0]["text"]
        llm_result = llm_result.replace(BAN_TOKEN, "")  # Remove any leaked control tokens
        return llm_result