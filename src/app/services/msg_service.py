from interface.i_msg_service import IMsgService
from config import GRPCPORT, GRPCHOST
from .protos import msg_pb2_grpc
from .protos import msg_pb2
import grpc


class MsgService(IMsgService):
    def __init__(self):
        self.channel = grpc.insecure_channel(GRPCHOST + ":" + GRPCPORT)
        self.sub = msg_pb2_grpc.msgStub(self.channel)

    def send_msg(self, msg):
        request = msg_pb2.msg_request()
        request.msg = msg
        request.user_id = "1"
        response = self.sub.GotMsg(request)
        return response
