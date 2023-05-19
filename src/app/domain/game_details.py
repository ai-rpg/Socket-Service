import uuid

from dataclasses import dataclass, field


@dataclass
class GameDetails:
    game_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    author: str = ""
    hook: str = ""
    game_type = ""
