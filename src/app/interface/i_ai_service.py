import abc


class IAIService(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def request_from_ai(self, msg):
        raise NotImplementedError
