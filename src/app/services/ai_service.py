from interface.i_ai_service import IAIService
import requests
from config import NAME, AISERVICEURL

class AIService(IAIService):
    def __init__(self):
        pass

    def request_from_ai(self, msgs):
        url = AISERVICEURL + "/msg"
        payload = json.dumps({
        "msgs": [
            {
            "role": "string",
            "content": "string"
            }
        ]
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

