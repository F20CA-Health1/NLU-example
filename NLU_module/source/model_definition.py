import os
from openai import AzureOpenAI


os.environ['OPENAI_GPT_KEY'] = 'XXXXXXXXXXXXXX' # Change to your AzureOpenAI key
os.environ['AZURE_ENDPOINT_GPT'] = 'https://XXXXXXXXXXXXXX.cognitiveservices.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview'
os.environ['GPT_MODEL_NAME'] = 'gpt-35-turbo'

gpt_35 = AzureOpenAI(
            api_key = os.environ['OPENAI_GPT_KEY'],
            api_version="2024-05-01-preview",
            azure_endpoint = os.environ['AZURE_ENDPOINT_GPT']
        )