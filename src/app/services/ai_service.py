from typing import List

from domain.ai_model import AIModel
from interface.i_ai_service import IAIService
import openai as ai
from logger import log
from config import OPENAPIKEY
class AIService(IAIService):
    def __init__(self):
        self.ai = ai
        self.ai.api_key = OPENAPIKEY

    def get_response(self, prompt) -> str:
        model = AIModel()

        log.info("getting responce for prompt -> " + prompt)
        response = self.ai.Completion.create(
            engine=model.model,
            prompt=prompt,
            temperature=model.temperature,
            max_tokens=model.max_token
        )
        return response.choices[0].text

    