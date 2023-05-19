import uuid

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interface.i_prompt_repository import IPromptRepository

@dataclass
class Prompt:
    prompt_string: str = ""
