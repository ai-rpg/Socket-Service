from interface.i_ai_service import IAIService
import requests
from config import NAME, AISERVICEURL
import json
from logger import log
class AIService(IAIService):
    def __init__(self):
        pass

    def request_from_ai(self, msgs):
        log.info(msgs)
        url = AISERVICEURL + "/msg"
        payload = json.dumps(msgs)
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, headers=headers, data=payload)
        log.info(requests, extra={"tags": {"application": NAME}}, exc_info=True)
        return response
