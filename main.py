# main.py

from googletrans import Translator
from langdetect import detect, LangDetectException

def detect_and_translate(text):
    """
    Detects the language of the input text and translates it to English if it's not already English.
    """
    try:
        # Detect the language
        lang = detect(text)
        print(f"Detected language: {lang}")

        if lang == 'en':
            return text
        else:
            # Translate the text to English
            translator = Translator()
            translated = translator.translate(text, src=lang, dest='en')
            print(f"Translated to English: {translated.text}")
            return translated.text
    except LangDetectException:
        print("Language detection failed. Assuming English.")
        return text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return text

def create_ai_prompt(text):
    """
    Formats the English text into a prompt for an AI agent.
    """
    prompt = f"You are a helpful assistant. Please respond to the following query: \"{text}\""
    return prompt

def main():
    """
    Main function to run the AI Prompt Bot.
    """
    print("Welcome to PromptAI!")
    print("This tool will help you create prompts for AI agents in any language.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter your text: ")
        if user_input.lower() == 'exit':
            break

        # 1. Detect language and translate to English
        english_text = detect_and_translate(user_input)

        # 2. Create the AI prompt
        final_prompt = create_ai_prompt(english_text)

        print(f"\nGenerated AI Prompt:\n{final_prompt}\n")

if __name__ == "__main__":
    main()
