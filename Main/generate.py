import json
import openai
from termcolor import colored
from halo import Halo
from utils.utils import get_openai_key, calculate_openai_cost

def generate_response():

    with open ("system.txt", "r") as file:
        system_prompt = file.read()

    with open ("user.txt", "r") as file:
        user_prompt = file.read()

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "example input"
        },
        {
            "role": "assistant",
            "content": "example output"
        },
        {
            "role": "user",
            "content": user_prompt
        },
    ]

    openai_key = get_openai_key()
    client = openai.OpenAI(openai_key = openai_key)

    with open ("model.json", "r") as file:
        model_data = json.load(file)

    spinner = Halo(text=colored("Calling OpenAI...", 'cyan'), spinner='dots')
    spinner.start()


    response = client.chat.completions.create(
        model = model_data["model_name"],
        temperature = model_data["temperature"],
        max_tokens = model_data["maxTokens"],
        messages = messages,
        response_format={
            "type": "json_object"} if model_data["jsonOutput"] else None
    )
    
    spinner.succeed(colored("Generated successfully!", 'green'))

    print(response.choices[0].messages.content)

    calculate_openai_cost(response, model_data["model_name"], True)

if __name__ == "__main__":
    generate_response()
