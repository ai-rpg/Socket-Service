from typing import List

from domain.game_details import GameDetails
from interface.i_game_defails_respository import IGameDetailsRepository
from logger import log

import yaml
import os

class GameDetailsRepository(IGameDetailsRepository):
    def __init__(self):
        # TODO document why this method is empty
        pass

    def get(self) -> GameDetails:
        log.info("get game details")
        # get the current working directory
        current_working_directory = os.getcwd()

        # print output to the console
        print(current_working_directory)
        with open(os.path.join(current_working_directory, "src", "game_details.yaml"), "r") as stream:
            try:
                details = yaml.safe_load(stream)
                r_details = GameDetails()
                r_details.author = details['author']
                r_details.game_type = details['game_type']
                r_details.hook = details['hook']
                return r_details
            except yaml.YAMLError as exc:
                print(exc)