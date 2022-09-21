import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY

def text_model(input_text):
    response = openai.Completion.create(
    model="text-curie-001",
    prompt=input_text,
    temperature=0.3,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    )

    return response['choices'][0]['text']