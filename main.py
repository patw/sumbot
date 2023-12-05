from fastapi import FastAPI
import json
import requests
import time

# Load the llm config from the json file provided on command line
with open("model.json", 'r') as file:
    model = json.load(file)

# Whip the llama into gear
DEFAULT_SYSTEM = "You are a helpful assistant who will always answer the question with only the data provided"
DEFAULT_PROMPT = "Entity:\n{%D}\nDescribe the {%E} in a single paragraph, without saying it's a JSON object or including any URLs or images:"
DEFAULT_TOKENS = 512 # many words
DEFAULT_TEMP = 0.7 # very mild temp for more boring results

# Fast API init
app = FastAPI(
        title="SumBot",
        description="Send me a JSON record and say what kind of entity it is (movie, transaction, person) and I'll summarize it with an LLM",
        version="1.1",
        contact={
            "name": "Pat Wendorf",
            "email": "pat.wendorf@mongodb.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    }
)

def remove_extra_formatting(text):
    cleaned_text = text.replace("\n", " ") # remove newline
    cleaned_text = cleaned_text.replace("\t", " ") # remove tabs
    cleaned_text = cleaned_text.replace("  ", " ") # remove double spaces
    return cleaned_text

# Endpoint to compare 2 images by URL and show similarity
@app.post("/summarize")
async def summarize_json_data(entity_type: str, input_json: str):

    # Build the prompt
    prompt = model["prompt_format"].replace("{%S}", DEFAULT_SYSTEM)
    prompt = prompt.replace("{%P}", DEFAULT_PROMPT)
    prompt = prompt.replace("{%D}", input_json)
    prompt = prompt.replace("{%E}", entity_type)

    api_data = {
        "prompt": prompt,
        "n_predict": DEFAULT_TOKENS,
        "temperature": DEFAULT_TEMP,
        "stop": model["stop_tokens"]
    }

    # Time the process
    start_time = time.time()
    try:
        # Call the model API
        response = requests.post(model["llama_endpoint"], headers={"Content-Type": "application/json"}, json=api_data)
        json_output = response.json()
        end_time = time.time()
        milliseconds_elapsed = (end_time - start_time) * 1000
        output = {"summary": remove_extra_formatting(json_output['content']), "ms": round(milliseconds_elapsed)}
    except:
        output = {"error": "My AI model is not responding try again in a moment 🔥🐳"}

    # remove annoying formatting in output
    return output