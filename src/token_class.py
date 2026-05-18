from dataclasses import dataclass
from token_types import TokenType

@dataclass
class Token:
    type: TokenType
    value: any
    line: int
    column: int

    def __str__(self):
        return f"Token({self.type.name}, {repr(self.value)}, line={self.line}, col={self.column})"