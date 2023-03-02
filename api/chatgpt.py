from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = "gpt-3.5-turbo"
        # self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        # self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0.7))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 4096))

    def get_response(self):
        response = openai.Completion.create(
            model=self.model,
            # messages=self.prompt.generate_prompt(),
            messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}],
            # prompt=self.prompt.generate_prompt(),
            temperature=self.temperature,
            # frequency_penalty=self.frequency_penalty,
            # presence_penalty=self.presence_penalty,
            stop=None,
            max_tokens=self.max_tokens
        )
        print(response['choices'])
        return response['choices'][0]['text'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)
