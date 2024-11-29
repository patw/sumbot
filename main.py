from fastapi import FastAPI
import json

# Use local models with the OpenAI library and a custom baseurl
from openai import OpenAI

# Load the llm config from the json file provided on command line
with open("model.json", 'r') as file:
    llm_config = json.load(file)

# Whip the llama into gear
DEFAULT_SYSTEM = "You are a helpful assistant who will always answer the question with only the data provided"
DEFAULT_PROMPT = "Entity:\n{data}\nDescribe the {entity} in a single paragraph, without saying it's a JSON object or including any URLs or images"
DEFAULT_TEMP = 0.1 # very mild temp for more boring results

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

# Call llm using the llm configuration
def llm_local(prompt):
    client = OpenAI(api_key=llm_config["api_key"], base_url=llm_config["base_url"])
    messages=[{"role": "system", "content": DEFAULT_SYSTEM},{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=llm_config["model"], temperature=DEFAULT_TEMP, messages=messages)
    return response.choices[0].message.content

# Endpoint to summarize the input
@app.post("/summarize")
async def summarize_json_data(entity_type: str, input_json: str):
    prompt = DEFAULT_PROMPT.format(entity=entity_type, data=input_json)
    return llm_local(prompt)
