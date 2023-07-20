from dataclasses import dataclass, field
from typing import List
import json


@dataclass
class GameCache:
    user_id: str
    sid: str
    gamelog: list = field(default_factory=list)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
