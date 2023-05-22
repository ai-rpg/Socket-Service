from dataclasses import dataclass, field


@dataclass
class FateModel:
    roll: int = 0
    result: str = ""
