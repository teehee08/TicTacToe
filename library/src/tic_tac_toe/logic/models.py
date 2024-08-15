import enum
from __future__ import annotations
import re

class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Mark:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

from dataclasses import dataclass
from functools import cached_property
@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")
        
    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")
    
    @cached_property
    def O_count(self) -> int:
        return self.cells.count("O")        

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")
    
@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark ("X")

    