import halo
from termcolor import colored
import json

def get_openai_key():
    with open("../keys.json", "r") as file:
        keys = json.load(file)
    return keys["openai_key"]

MODEL_COSTS = {
    "gpt-4o": { "input": 0.0025, "cached_input": 0.00125, "output": 0.01 },
    "gpt-4o-2024-11-20": { "input": 0.0025, "cached_input": 0.00125, "output": 0.01 },
    "gpt-4o-mini": { "input": 0.00015, "cached_input": 0.000075, "output": 0.0006 },
    "o1-preview": { "input": 0.015, "cached_input": 0.0075, "output": 0.06 },
    "o1-mini": { "input": 0.003, "cached_input": 0.0015, "output": 0.012 },
    "claude-3-5-sonnet-20240620": { "input": 0.003, "output": 0.015 }
}

def calculate_openai_cost(response, model_name, print_breakdown):
    usage = response.usage
    rates = MODEL_COSTS[model_name]
    
    # Get token counts
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    cached_tokens = usage.prompt_tokens_details.cached_tokens if hasattr(usage, 'prompt_tokens_details') else 0
    
    # Calculate costs with cache discount
    non_cached_tokens = prompt_tokens - cached_tokens
    input_cost = (
        (non_cached_tokens / 1000 * rates["input"]) +  # Full price for non-cached tokens
        (cached_tokens / 1000 * rates["input"] * 0.5)  # 50% discount for cached tokens
    )
    output_cost = (completion_tokens / 1000) * rates["output"]
    total_cost = round(input_cost + output_cost, 6)
    
    # Print breakdown
    if print_breakdown:
        print("\n" + colored("═" * 50, 'blue'))
        print(colored("▶ Final Token Usage & Cost", 'yellow', attrs=['bold']))
        print(colored("  ▪ Input Tokens: ", "cyan") + 
            colored(f"{prompt_tokens:,} ({cached_tokens:,} cached) (${input_cost:.4f})", 'white'))
        print(colored("  ▪ Output Tokens: ", "cyan") + 
            colored(f"{completion_tokens:,} (${output_cost:.4f})", 'white'))
        print(colored("  ▪ Total Tokens: ", "cyan") + 
            colored(f"{usage.total_tokens:,}", 'white'))
        print(colored("  ▪ Total Cost: ", "cyan") + 
            colored(f"${total_cost:.4f} USD", 'green'))
        print(colored("═" * 50, 'blue'))
    
    return total_cost
