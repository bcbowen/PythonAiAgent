import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main() -> int:
    if len(sys.argv) == 1 or not sys.argv[1]: 
        print("You forgot the argument, sizzlechest")
        sys.exit(1)
    
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    verbose = "--verbose" in sys.argv
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    #content = client.generate_content(model, prompt)
    content = client.models.generate_content(model=model, contents=messages)
    print(content.text)
    if content.usage_metadata and verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {content.usage_metadata.candidates_token_count}")
    sys.exit(0)

if __name__ == "__main__":
    main()
