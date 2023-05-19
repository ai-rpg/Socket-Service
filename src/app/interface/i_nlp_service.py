import abc


class INlpService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_intent(self, string) -> str:
        raise NotImplementedError
