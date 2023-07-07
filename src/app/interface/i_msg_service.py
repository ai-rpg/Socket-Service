import abc

class IMsgService(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def send_msg(self, msg):
        raise NotImplementedError