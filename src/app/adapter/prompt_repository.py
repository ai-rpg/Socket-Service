from typing import List

from domain.prompt import Prompt
from interface.i_prompt_repository import IPromptRepository

from logger import log

class PromptRepository(IPromptRepository):
    def __init__(self):
        # TODO document why this method is empty
        pass

    def generate(self, game_details) -> Prompt:
        log.info("generating prompt")
        prompt = Prompt()
        prompt.prompt_string = """Assume the role of an expert in the characters, scenarios, locations, and plot of a """ + game_details.game_type + """. 
        As an expert be my Dungeon Master in a roleplaying game based on this adventure. 
        Give a narrative description of everything that follows, based on my actions, in the style of """+ game_details.author + """, without taking control of me or my character. 
        Also, give suitable names for characters and places. """ +  game_details.hook
        return prompt   