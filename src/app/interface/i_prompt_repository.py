import abc
from typing import List

from domain.prompt import Prompt


class IPromptRepository(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def generate(self, game_details, character_name) -> Prompt:
        raise NotImplementedError
