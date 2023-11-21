# SumBot
Summarize structured JSON data into LLM produced, semantically rich paragraphs.  Great for embedding!

## Local Installation

```
pip install -r requirements.txt
```

## Downloading the Mistral 7b model (with dolphin fine tune)

```wget https://huggingface.co/TheBloke/dolphin-2.1-mistral-7B-GGUF/resolve/main/dolphin-2.1-mistral-7b.Q5_K_S.gguf```

## Local Running

```
uvicorn main:app --host 0.0.0.0 --port 3002 --reload
```

## Accessing API

http://localhost:3002/docs