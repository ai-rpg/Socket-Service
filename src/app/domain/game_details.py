import uuid

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interface.i_game_details_repository import IGameDetailsRepository

@dataclass
class GameDetails:
    game_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    author: str =""
    hook:str = ""
    game_type= ""
