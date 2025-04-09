from openai import OpenAI
from google import genai
# These variables are imported from __init__.py
from . import gemini_api_key, openai_api_key, system_prompt

def openai_prompt(content, language, model="gpt-4o-mini"):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt.format(language=language)},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content

def gemini_prompt(content, language, model="gemini-2.0-flash"):

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model=model, contents=content
    )
    return response.text