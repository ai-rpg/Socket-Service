from dataclasses import dataclass, field
from typing import List

@dataclass
class GameCache:
    user_id:str
    sid:str
    gamelog: str

@dataclass
class GameCacheList:
    games: list[GameCache] = field(default_factory=list)