import re
from src.token_types import TokenType
from src.token_class import Token


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1
        self.indent_stack = [0]
        self.indents = []

        self.keywords = {
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'elif': TokenType.ELIF,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'in': TokenType.IN,
            'def': TokenType.DEF,
            'return': TokenType.RETURN,
            'print': TokenType.PRINT,
            'True': TokenType.TRUE,
            'False': TokenType.FALSE,
            'None': TokenType.NONE,
            'and': TokenType.AND,
            'or': TokenType.OR,
            'not': TokenType.NOT,
        }

    def tokenize(self):
        self.tokens = []
        self.current = 0
        self.line = 1
        self.column = 1
        self.indent_stack = [0]

        while not self.is_at_end():
            self.start = self.current
            self.tokenize_next()

        # Cerrar indents pendientes
        while len(self.indent_stack) > 1:
            self.tokens.append(Token(TokenType.DEDENT, "", self.line, self.column))
            self.indent_stack.pop()

        self.tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return self.tokens

    def tokenize_next(self):
        c = self.advance()

        # Espacios se ignoran completamente (no se generan tokens)
        if c == ' ' or c == '\t':
            pass  # Ignorar espacios

        elif c == '\n':
            self.line += 1
            self.column = 1
            # Manejar indentación
            self.handle_indentation()

        elif c == '#':
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()
            # Ignorar comentarios (no generar token)

        elif c == '(':
            self.tokens.append(Token(TokenType.LPAREN, "(", self.line, self.column - 1))
        elif c == ')':
            self.tokens.append(Token(TokenType.RPAREN, ")", self.line, self.column - 1))
        elif c == '{':
            self.tokens.append(Token(TokenType.LBRACE, "{", self.line, self.column - 1))
        elif c == '}':
            self.tokens.append(Token(TokenType.RBRACE, "}", self.line, self.column - 1))
        elif c == ':':
            self.tokens.append(Token(TokenType.COLON, ":", self.line, self.column - 1))
        elif c == ',':
            self.tokens.append(Token(TokenType.COMMA, ",", self.line, self.column - 1))
        elif c == ';':
            self.tokens.append(Token(TokenType.SEMICOLON, ";", self.line, self.column - 1))
        elif c == '=':
            if self.match('='):
                self.tokens.append(Token(TokenType.EQ, "==", self.line, self.column - 2))
            else:
                self.tokens.append(Token(TokenType.ASSIGN, "=", self.line, self.column - 1))
        elif c == '!':
            if self.match('='):
                self.tokens.append(Token(TokenType.NE, "!=", self.line, self.column - 2))
            else:
                self.tokens.append(Token(TokenType.ERROR, "!", self.line, self.column - 1))
        elif c == '<':
            if self.match('='):
                self.tokens.append(Token(TokenType.LE, "<=", self.line, self.column - 2))
            else:
                self.tokens.append(Token(TokenType.LT, "<", self.line, self.column - 1))
        elif c == '>':
            if self.match('='):
                self.tokens.append(Token(TokenType.GE, ">=", self.line, self.column - 2))
            else:
                self.tokens.append(Token(TokenType.GT, ">", self.line, self.column - 1))
        elif c == '+':
            self.tokens.append(Token(TokenType.PLUS, "+", self.line, self.column - 1))
        elif c == '-':
            self.tokens.append(Token(TokenType.MINUS, "-", self.line, self.column - 1))
        elif c == '*':
            self.tokens.append(Token(TokenType.TIMES, "*", self.line, self.column - 1))
        elif c == '/':
            self.tokens.append(Token(TokenType.DIVIDE, "/", self.line, self.column - 1))
        elif c == '%':
            self.tokens.append(Token(TokenType.MOD, "%", self.line, self.column - 1))
        elif c == '"' or c == "'":
            self.string(c)
        elif c.isdigit():
            self.number()
        elif c.isalpha() or c == '_':
            self.identifier()
        else:
            self.tokens.append(Token(TokenType.ERROR, c, self.line, self.column - 1))

    def handle_indentation(self):
        # Calcular indentación de la nueva línea
        col = 1
        while self.peek() == ' ':
            self.advance()
            col += 1

        if col > self.indent_stack[-1]:
            # Indentación aumentó
            self.indent_stack.append(col)
            self.tokens.append(Token(TokenType.INDENT, "", self.line, col))
        elif col < self.indent_stack[-1]:
            # Indentación disminuyó
            while col < self.indent_stack[-1]:
                self.indent_stack.pop()
                self.tokens.append(Token(TokenType.DEDENT, "", self.line, col))
            if col != self.indent_stack[-1]:
                self.tokens.append(Token(TokenType.ERROR, "Indentation error", self.line, col))

    def string(self, delimiter):
        start_line = self.line
        start_col = self.column - 1
        while self.peek() != delimiter and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.is_at_end():
            self.tokens.append(Token(TokenType.ERROR, "Unterminated string", start_line, start_col))
            return
        self.advance()
        value = self.source[self.start + 1:self.current - 1]
        self.tokens.append(Token(TokenType.STRING, value, start_line, start_col))

    def number(self):
        start_col = self.column - 1
        while self.peek().isdigit():
            self.advance()
        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
            value = float(self.source[self.start:self.current])
            self.tokens.append(Token(TokenType.NUMBER, value, self.line, start_col))
        else:
            value = int(self.source[self.start:self.current])
            self.tokens.append(Token(TokenType.NUMBER, value, self.line, start_col))

    def identifier(self):
        start_col = self.column - 1
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()
        text = self.source[self.start:self.current]
        token_type = self.keywords.get(text, TokenType.IDENTIFIER)
        self.tokens.append(Token(token_type, text, self.line, start_col))

    def advance(self):
        char = self.source[self.current]
        self.current += 1
        self.column += 1
        return char

    def match(self, expected):
        if self.is_at_end() or self.source[self.current] != expected:
            return False
        self.current += 1
        self.column += 1
        return True

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def is_at_end(self):
        return self.current >= len(self.source)