import abc
from typing import List
from domain.ai_model import AIModel


class IAISummaryService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_summary(self, history) -> str:
        raise NotImplementedError
