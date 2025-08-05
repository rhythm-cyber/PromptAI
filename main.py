import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from googletrans import Translator
from langdetect import detect, LangDetectException

def detect_and_translate(text):
    try:
        lang = detect(text)
        if lang == 'en':
            return text
        else:
            translator = Translator()
            translated = translator.translate(text, src=lang, dest='en')
            return translated.text
    except LangDetectException:
        return text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return text

def create_ai_prompt(text):
    return f"You are a helpful assistant. Please respond to the following query: \"{text}\""

class PromptAILayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PromptAILayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.input_text = TextInput(hint_text='Enter text in any language...', size_hint_y=None, height=150)
        self.add_widget(self.input_text)

        self.generate_button = Button(text='Generate Prompt', size_hint_y=None, height=50)
        self.generate_button.bind(on_press=self.generate_prompt)
        self.add_widget(self.generate_button)

        self.result_label = Label(text='Generated prompt will appear here.', size_hint_y=None, height=150)
        self.add_widget(self.result_label)

    def generate_prompt(self, instance):
        input_text = self.input_text.text
        if input_text:
            english_text = detect_and_translate(input_text)
            final_prompt = create_ai_prompt(english_text)
            self.result_label.text = final_prompt
        else:
            self.result_label.text = "Please enter some text."

class PromptAIApp(App):
    def build(self):
        return PromptAILayout()

if __name__ == '__main__':
    PromptAIApp().run()
