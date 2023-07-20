import abc


class IAdventureService(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def get_adventure(self, adventure_id, user_id):
        raise NotImplementedError

    @abc.abstractclassmethod
    def update_adventure(self, adventure):
        raise NotImplementedError
