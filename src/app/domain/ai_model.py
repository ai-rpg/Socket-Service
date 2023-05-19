import uuid

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from config import OPENAPIKEY
if TYPE_CHECKING:
    from interface.i_ai_service import IAIService
import openai as ai

@dataclass
class AIModel:
    model: str = "text-davinci-003"
    max_token = 1000
    temperature = 0.5
    ai.api_key = OPENAPIKEY

