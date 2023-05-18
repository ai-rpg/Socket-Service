from typing import List

from domain.game_details import GameDetails
from interfaces.game_defails_respository import GameDetailsRepository
from logger import log

import yaml

class GameDetailsRepository(GameDetailsRepository):
    def __init__(self):
        # TODO document why this method is empty
        pass

    def get(self) -> GameDetails:
        log.info("get game details")
        with open("game_details.yaml", "r") as stream:
            try:
                details = yaml.safe_load(stream)
                return details
            except yaml.YAMLError as exc:
                print(exc)