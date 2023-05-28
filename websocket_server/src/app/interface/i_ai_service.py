import abc
from typing import List
from domain.ai_model import AIModel


class IAIService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_response(self, prompt) -> AIModel:
        raise NotImplementedError

    @abc.abstractclassmethod
    def store_converation(self, role, content):
        raise NotImplementedError
