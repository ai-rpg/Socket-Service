from typing import List

from domain.ai_model import AIModel
from interface.i_ai_service import IAIService
from interface.i_ai_summary_service import IAISummaryService

import openai as ai
from logger import log
from config import OPENAPIKEY


class AISummaryService(IAISummaryService):
    def __init__(self):
        self.ai = ai
        self.ai.api_key = OPENAPIKEY

    def get_summary(self, history) -> str:
        log.info("getting responce for prompt -> " + history)
        response = self.ai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=100,
            temperature=0.7,
            top_p=0.5,
            frequency_penalty=0.5,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant for text summarization.",
                },
                {"role": "user", "content": f"Summarize this : {history}"},
            ],
        )
        return response.choices[0].message.content
