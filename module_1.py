import os
from openai import AzureOpenAI
from dotenv import load_dotenv 

if(load_dotenv(dotenv_path='key.env', verbose=True) == False):
    raise Exception('env file not found')

api_key = os.environ['OPENAI_API_KEY']
azure_endpoint = os.environ['OPENAI_AZURE_ENDPOINT']
deployment_name=os.environ['deployment_name']
api_version=os.environ['api_version']

# print(api_key)
# print(azure_endpoint)
# print(deployment_name)
# print(api_version)

client = AzureOpenAI(
    api_key = api_key,  
    api_version = api_version,
    azure_endpoint = azure_endpoint
)

def get_completion(prompt, temperature=0.0):
    messages = [{"role": "user", 
                 "content": prompt}]

    response = client.chat.completions.create(
        model = deployment_name,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    # print(response.model_dump_json(indent=2))
    return response.choices[0].message.content

def get_completion_from_messages(messages, temperature=0.0):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message.content
