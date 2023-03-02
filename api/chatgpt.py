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
        # response = openai.ChatCompletion.create(
        #     model=self.model,
        #     messages=[{"role": "user", "content":"HI"}],
        #     temperature=self.temperature,
        #     # frequency_penalty=self.frequency_penalty,
        #     # presence_penalty=self.presence_penalty,
        #     stop=None,
        #     max_tokens=self.max_tokens
        # )
        # return response
        # # return response['choices'][0]['text'].strip()
        # Use OpenAI's ChatCompletion API to get the chatbot's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
            messages=[{"role": "user", "content": self.prompt.generate_prompt()}],  # The conversation history up to this point, as a list of dictionaries
            max_tokens=4096,  # The maximum number of tokens (words or subwords) in the generated response
            stop=None,  # The stopping sequence for the generated response, if any (not used here)
            temperature=0.7,  # The "creativity" of the generated response (higher temperature = more creative)
        )

        # Find the first response from the chatbot that has text in it (some responses may not have text)
        for choice in response.choices:
            if "text" in choice:
                return choice.text

        # If no response with text is found, return the first response's content (which may be empty)
        return response.choices[0].message.content

    def add_msg(self, text):
        self.prompt.add_msg(text)
