import os
from dotenv import load_dotenv
load_dotenv()
from openai import AzureOpenAI
import json


# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("OPENAI_API_VERSION", "2024-04-01-preview")
deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

result = client.images.generate(
    model=deployment,
    prompt="Create an image of a person boating in water",
    n=1,
    style="vivid",
    quality="standard",
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)