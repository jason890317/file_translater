from model import gemini_prompt, openai_prompt


if __name__ == "__main__":
    prompt = "Hello, how are you?"
    print(gemini_prompt(prompt, "English"))
    print(openai_prompt(prompt, "English"))
        