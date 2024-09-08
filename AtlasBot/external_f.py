import requests
import json
import os
import openai

GPT_API_KEY = os.environ['GPT_TOKEN_KEY']
openai.api_key = GPT_API_KEY


def call_gpt_api(text):
    try:
        print("Retrieving response from GPT-3.5T")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": text
            }],
            max_tokens=300,
            temperature=0.7,
            stop=None  # You can define stop sequences if needed
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Failed to fetch response from GPT-3.5 Turbo API due to an error: {str(e)}"

#Add additional functionality to perform GPT 4 calculations


