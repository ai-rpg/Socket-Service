import abc


class IFateService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_fate(self, roll) -> str:
        raise NotImplementedError

    @abc.abstractclassmethod
    def generate_random_number() -> int:
        raise NotImplementedError
