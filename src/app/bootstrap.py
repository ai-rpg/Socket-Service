from .config import BUILD_VERSION, METRICS_PATH, NAME, OPENAPIKEY
from .logger import log

import openai as DM_AI
import openai as Summary_AI

DM_AI.api_key = OPENAPIKEY
Summary_AI.api_key = OPENAPIKEY

