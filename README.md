# NLU Module



## Dependencies

```
torch~=2.6.0+cu118
transformers~=4.48.3
openai~=1.61.1
```



## AzureOpenAI

Remember to replace the AzureOpenAI information in "NLU_module\source\model_definition.py" with your own.

```python
os.environ['OPENAI_GPT_KEY'] = 'XXXXXXXXXXXXXX' # Change to your AzureOpenAI key
os.environ['AZURE_ENDPOINT_GPT'] = 'https://XXXXXXXXXXXXXX.cognitiveservices.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview' # Change to your endpoint
```



## Example

run.py is an example of using this module.

```
python run.py
```