import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import exit, argv
import config

if len(argv) <= 1:
    print("No prompt provided") 
    exit(1)

prompt = argv[1]
verbose =  "--verbose" in argv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

response = client.models.generate_content(
    model=config.model_name,
    contents=messages,
    #config=types.GenerateContentConfig(system_instruction=config.system_prompt),
    config = config.agent_config
)

for function_call in response.function_calls:
    print(f"Calling function: {function_call.name}({function_call.args})")

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


