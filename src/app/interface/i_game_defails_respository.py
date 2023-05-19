import abc
from typing import List
from domain.game_details import GameDetails


class IGameDetailsRepository(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get(self) -> GameDetails:
        raise NotImplementedError
