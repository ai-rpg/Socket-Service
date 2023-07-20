from interface.i_adventure_service import IAdventureService
import requests
from config import NAME, ADVENTURESERVICEURL
import json

from logger import log


class AdventureService(IAdventureService):
    def __init__(self):
        pass

    def get_adventure(self, adventure_id, user_id):
        try:
            url = ADVENTURESERVICEURL + "/adventure/{user_id}/{adventure_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.request("GET", url, headers=headers)
            return response
        except Exception as inst:
            log.error(
                "get_adventure",
                extra={"tags": {"application": NAME}},
                exc_info=True,
            )

    def update_adventure(self, adventure):
        try:
            pass
        except Exception as inst:
            log.error(
                "update_adventure",
                extra={"tags": {"application": NAME}},
                exc_info=True,
            )
