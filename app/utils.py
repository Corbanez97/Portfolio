import openai
import os

openai.organization = "org-Urk1Ei6EFtzc2wwglwsAwRn9"
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        model="image-alpha-001",
        size="256x256",
        response_format="url",
        n = 1
    )

    return [item['url'] for item in response['data']]