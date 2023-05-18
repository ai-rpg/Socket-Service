import uuid

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_details_repository import GameDetailsRepository

@dataclass
class GameDetails:
    game_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    author: str =""
    hook:str = ""
    game_type= ""

    def get(self, game_details_repository: "GameDetailsRepository"):
        return game_details_repository.get(self)