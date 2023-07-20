import abc


class IRedisRepository(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def set(self, GameCache):
        raise NotImplementedError

    @abc.abstractclassmethod
    def get(self, user_id):
        raise NotImplementedError
