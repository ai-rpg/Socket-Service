import abc
from typing import List
from domain.ai_model import AIModel


class IAIService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_response(self, prompt) -> AIModel:
        raise NotImplementedError
