from typing import List

from domain.ai_model import AIModel
from interface.i_ai_service import IAIService
import openai as ai
from logger import log
from config import OPENAPIKEY


class AIService(IAIService):
    history = []

    def __init__(self):
        self.ai = ai
        self.ai.api_key = OPENAPIKEY
        self.history = []

    def get_response(self, prompt) -> str:
        model = AIModel()

        log.info("getting responce for prompt -> " + prompt)
        response = self.ai.ChatCompletion.create(
            model="gpt-3.5-turbo", #model.model,
            messages=self.history
        )
        return response.choices[0].message.content

    def store_converation(self, role, content):
        self.history.append({'role':role, 'content': content})