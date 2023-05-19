import random

from typing import List

from interface.i_fate_service import IFateService


class FateService(IFateService):
    def __init__(self):
        # TODO document why this method is empty
        pass

    def get_fate(self, roll) -> str:
        # TODO document why this method is empty
        result = ""
        if roll == 1:
            result = "No, and "
        if roll == 2:
            result = "No"
        if roll == 3:
            result = "No, but "
        if roll == 4:
            esult = "Yes, but "
        if roll == 5:
            result = "Yes"
        if roll == 6:
            result = "Yes, and"
        return result

    def generate_random_number(self) -> int:
        return random.randint(1, 6)
