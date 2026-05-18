from enum import Enum, auto

class TokenType(Enum):
    # Palabras reservadas de Python
    IF = auto()
    ELSE = auto()
    ELIF = auto()
    WHILE = auto()
    FOR = auto()
    IN = auto()
    DEF = auto()
    RETURN = auto()
    PRINT = auto()
    TRUE = auto()
    FALSE = auto()
    NONE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()

    # Identificadores y literales
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    # Operadores
    ASSIGN = auto()
    EQ = auto()
    NE = auto()
    LT = auto()
    LE = auto()
    GT = auto()
    GE = auto()
    PLUS = auto()
    MINUS = auto()
    TIMES = auto()
    DIVIDE = auto()
    MOD = auto()

    # Delimitadores
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    COLON = auto()
    COMMA = auto()
    SEMICOLON = auto()
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()

    COMMENT = auto()
    SPACE = auto()
    EOF = auto()
    ERROR = auto()