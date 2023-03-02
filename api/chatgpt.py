from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0.7))
        # self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        # self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 3000))

    def get_response(self):
        # Use OpenAI's ChatCompletion API to get the chatbot's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # The name of the OpenAI chatbot model to use
            messages=[{"role": "user", "content": self.prompt.generate_prompt()}],
            temperature=self.temperature,   # The "creativity" of the generated response (higher temperature = more creative)
            stop=None,                      # The stopping sequence for the generated response, if any (not used here)
            max_tokens=self.max_tokens      # The maximum number of tokens (words or subwords) in the generated response
        )

        return response.choices[0].message.content

    def add_msg(self, text):
        self.prompt.add_msg(text)
