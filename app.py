from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from langdetect import detect, LangDetectException

app = Flask(__name__)

def detect_and_translate(text):
    """
    Detects the language of the input text and translates it to English if it's not already English.
    """
    try:
        lang = detect(text)
        if lang == 'en':
            return text
        else:
            translator = Translator()
            translated = translator.translate(text, src=lang, dest='en')
            return translated.text
    except LangDetectException:
        return text # Assume English if detection fails
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return text

def create_ai_prompt(text):
    """
    Formats the English text into a prompt for an AI agent.
    """
    prompt = f"You are a helpful assistant. Please respond to the following query: \"{text}\""
    return prompt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    user_text = data['text']

    # 1. Detect language and translate to English
    english_text = detect_and_translate(user_text)

    # 2. Create the AI prompt
    final_prompt = create_ai_prompt(english_text)

    return jsonify({'prompt': final_prompt})

if __name__ == '__main__':
    app.run(debug=True)
