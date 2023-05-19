from config import BUILD_VERSION, METRICS_PATH, NAME, OPENAPIKEY
from logger import log

from adapter.game_details_repository import GameDetailsRepository
from adapter.prompt_repository import PromptRepository
from services.ai_service import AIService
from services.ai_summary_service import AISummaryService
from services.fate_service import FateService
from services.nlp_service import NlpService

nlp = NlpService()

fate_service = FateService()

print(fate_service.generate_random_number())
print(fate_service.get_fate(fate_service.generate_random_number()))

game_defails_respository = GameDetailsRepository()
prompt_repository = PromptRepository()

dm_ai = AIService()
summary_ai = AISummaryService()

game_details = game_defails_respository.get()
base_prompt = prompt_repository.generate(game_details)
history = ""

dm_response = dm_ai.get_response(base_prompt.prompt_string)
history += dm_response
summary = summary_ai.get_summary(history)
fate_service = FateService()
print(fate_service.generate_random_number())
print(dm_response)
nlp.get_intent(dm_response)

#for x in range(3):
#    user_text = input(">>")
#    dm_text = dm_ai.get_response(summary + " " + user_text)
#    history += dm_text
#    summary = summary_ai.get_summary(history)
#    print(dm_text)
