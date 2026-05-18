from token_types import TokenType
from token_class import Token


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.java_code = []
        self.indent_level = 0
        self.errors = []

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type, error_msg=""):
        token = self.current_token()
        if token and token.type == expected_type:
            self.pos += 1
            return token
        else:
            if token:
                self.errors.append(
                    f"Error at line {token.line}, col {token.column}: {error_msg} - found {token.type.name}")
            else:
                self.errors.append(f"Error: {error_msg}")
            return None

    def parse(self):
        self.java_code = []
        self.indent_level = 0
        self.java_code.append("public class Main {")
        self.indent_level = 1
        self.java_code.append(self.indent() + "public static void main(String[] args) {")
        self.indent_level = 2

        # Saltar tokens iniciales basura
        while self.current_token() and self.current_token().type in [TokenType.NEWLINE, TokenType.SPACE]:
            self.pos += 1

        # Parsear todas las sentencias
        while self.current_token() and self.current_token().type != TokenType.EOF:
            self.parse_statement()
            # Saltar NEWLINEs después de cada sentencia
            while self.current_token() and self.current_token().type == TokenType.NEWLINE:
                self.pos += 1

        self.indent_level = 1
        self.java_code.append(self.indent() + "}")
        self.indent_level = 0
        self.java_code.append("}")

        if self.errors:
            return None
        return "\n".join(self.java_code)

    def parse_statement(self):
        token = self.current_token()
        if not token:
            return

        # Ignorar tokens de control
        if token.type == TokenType.INDENT:
            self.pos += 1
            return
        if token.type == TokenType.DEDENT:
            self.pos += 1
            return
        if token.type == TokenType.NEWLINE:
            self.pos += 1
            return
        if token.type == TokenType.SPACE:
            self.pos += 1
            return
        if token.type == TokenType.COMMENT:
            self.pos += 1
            return

        # Sentencias reales
        if token.type == TokenType.PRINT:
            self.parse_print()
        elif token.type == TokenType.IF:
            self.parse_if()
        elif token.type == TokenType.ELIF:
            self.parse_elif()
        elif token.type == TokenType.ELSE:
            self.parse_else()
        elif token.type == TokenType.WHILE:
            self.parse_while()
        elif token.type == TokenType.IDENTIFIER:
            self.parse_assignment()
        else:
            self.errors.append(f"Unexpected token {token.type.name} at line {token.line}, col {token.column}")
            self.pos += 1

    def parse_print(self):
        self.consume(TokenType.PRINT)
        self.consume(TokenType.LPAREN, "Expected '(' after print")
        expr = self.parse_expression()
        self.consume(TokenType.RPAREN, "Expected ')' after print expression")
        self.java_code.append(self.indent() + f'System.out.println({expr});')

    def parse_if(self):
        self.consume(TokenType.IF)
        condition = self.parse_expression()
        self.consume(TokenType.COLON, "Expected ':' after if condition")

        self.java_code.append(self.indent() + f"if ({condition}) {{")
        self.indent_level += 1

        # Saltar hasta el INDENT o NEWLINE
        self.skip_to_block()

        # Parsear bloque
        self.parse_block()

        self.indent_level -= 1

        # Verificar si hay else o elif después
        self.check_else_or_elif()

        self.java_code.append(self.indent() + "}")

    def parse_elif(self):
        # Similar a if pero sin abrir nueva llave
        self.consume(TokenType.ELIF)
        condition = self.parse_expression()
        self.consume(TokenType.COLON, "Expected ':' after elif condition")

        # Cerrar bloque anterior y abrir elif
        self.java_code.append(self.indent() + f"}} else if ({condition}) {{")
        self.indent_level += 1

        self.skip_to_block()
        self.parse_block()

        self.indent_level -= 1
        self.check_else_or_elif()

    def parse_else(self):
        self.consume(TokenType.ELSE)
        self.consume(TokenType.COLON, "Expected ':' after else")

        self.java_code.append(self.indent() + "} else {")
        self.indent_level += 1

        self.skip_to_block()
        self.parse_block()

        self.indent_level -= 1
        self.java_code.append(self.indent() + "}")

    def parse_while(self):
        self.consume(TokenType.WHILE)
        condition = self.parse_expression()
        self.consume(TokenType.COLON, "Expected ':' after while condition")

        self.java_code.append(self.indent() + f"while ({condition}) {{")
        self.indent_level += 1

        self.skip_to_block()
        self.parse_block()

        self.indent_level -= 1
        self.java_code.append(self.indent() + "}")

    def parse_assignment(self):
        ident = self.consume(TokenType.IDENTIFIER)
        if not ident:
            return
        self.consume(TokenType.ASSIGN, "Expected '=' in assignment")
        expr = self.parse_expression()

        # Determinar tipo de variable (int, double, boolean, String)
        java_type = self.infer_type(expr)

        # Verificar si la variable ya fue declarada (simple, no declaramos explícitamente en Java)
        # En Java necesitamos declarar el tipo, pero como no tenemos símbolos, usamos var o inferimos
        self.java_code.append(self.indent() + f"{java_type} {ident.value} = {expr};")

    def infer_type(self, expr):
        """Inferir tipo Java basado en la expresión"""
        if expr.startswith('"') and expr.endswith('"'):
            return "String"
        elif expr == "true" or expr == "false":
            return "boolean"
        elif '.' in expr and any(c.isdigit() for c in expr):
            # Posible double
            return "double"
        elif any(c.isdigit() for c in expr):
            return "int"
        else:
            return "int"  # Por defecto

    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        left = self.parse_and()
        while self.current_token() and self.current_token().type == TokenType.OR:
            self.pos += 1
            right = self.parse_and()
            left = f"({left} || {right})"
        return left

    def parse_and(self):
        left = self.parse_comparison()
        while self.current_token() and self.current_token().type == TokenType.AND:
            self.pos += 1
            right = self.parse_comparison()
            left = f"({left} && {right})"
        return left

    def parse_comparison(self):
        left = self.parse_term()
        while self.current_token() and self.current_token().type in [TokenType.LT, TokenType.LE, TokenType.GT,
                                                                     TokenType.GE, TokenType.EQ, TokenType.NE]:
            op_token = self.current_token()
            self.pos += 1
            right = self.parse_term()
            left = f"({left} {self.operator_to_java(op_token.type)} {right})"
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current_token() and self.current_token().type in [TokenType.PLUS, TokenType.MINUS]:
            op_token = self.current_token()
            self.pos += 1
            right = self.parse_factor()
            left = f"({left} {self.operator_to_java(op_token.type)} {right})"
        return left

    def parse_factor(self):
        left = self.parse_primary()
        while self.current_token() and self.current_token().type in [TokenType.TIMES, TokenType.DIVIDE, TokenType.MOD]:
            op_token = self.current_token()
            self.pos += 1
            right = self.parse_primary()
            left = f"({left} {self.operator_to_java(op_token.type)} {right})"
        return left

    def parse_primary(self):
        token = self.current_token()
        if not token:
            return "???"

        if token.type == TokenType.NUMBER:
            self.pos += 1
            # Verificar si es float o int
            if isinstance(token.value, float) or '.' in str(token.value):
                return str(token.value)
            return str(token.value)
        elif token.type == TokenType.STRING:
            self.pos += 1
            return f'"{token.value}"'
        elif token.type == TokenType.IDENTIFIER:
            self.pos += 1
            return token.value
        elif token.type == TokenType.TRUE:
            self.pos += 1
            return "true"
        elif token.type == TokenType.FALSE:
            self.pos += 1
            return "false"
        elif token.type == TokenType.NONE:
            self.pos += 1
            return "null"
        elif token.type == TokenType.LPAREN:
            self.pos += 1
            expr = self.parse_expression()
            self.consume(TokenType.RPAREN, "Expected ')'")
            return f"({expr})"
        elif token.type == TokenType.NOT:
            self.pos += 1
            expr = self.parse_primary()
            return f"(!{expr})"
        else:
            self.errors.append(f"Unexpected token in expression: {token.type.name} at line {token.line}")
            self.pos += 1
            return "???"

    def skip_to_block(self):
        """Saltar hasta encontrar INDENT o inicio del bloque"""
        while self.current_token():
            if self.current_token().type == TokenType.INDENT:
                self.pos += 1
                break
            elif self.current_token().type == TokenType.NEWLINE:
                self.pos += 1
            else:
                break

    def parse_block(self):
        """Parsear un bloque indentado hasta DEDENT"""
        while self.current_token() and self.current_token().type != TokenType.DEDENT and self.current_token().type != TokenType.EOF:
            # Saltar NEWLINEs
            if self.current_token().type == TokenType.NEWLINE:
                self.pos += 1
                continue
            if self.current_token().type == TokenType.SPACE:
                self.pos += 1
                continue
            if self.current_token().type == TokenType.COMMENT:
                self.pos += 1
                continue
            if self.current_token().type == TokenType.INDENT:
                self.pos += 1
                continue

            self.parse_statement()

            # Saltar NEWLINE después de la sentencia
            while self.current_token() and self.current_token().type == TokenType.NEWLINE:
                self.pos += 1

        # Consumir DEDENT
        if self.current_token() and self.current_token().type == TokenType.DEDENT:
            self.pos += 1

    def check_else_or_elif(self):
        """Verificar si hay else o elif después de un if/elif"""
        # Saltar NEWLINEs
        while self.current_token() and self.current_token().type == TokenType.NEWLINE:
            self.pos += 1

        if self.current_token():
            if self.current_token().type == TokenType.ELIF:
                self.parse_elif()
            elif self.current_token().type == TokenType.ELSE:
                self.parse_else()

    def operator_to_java(self, op_type):
        mapping = {
            TokenType.PLUS: "+",
            TokenType.MINUS: "-",
            TokenType.TIMES: "*",
            TokenType.DIVIDE: "/",
            TokenType.MOD: "%",
            TokenType.LT: "<",
            TokenType.LE: "<=",
            TokenType.GT: ">",
            TokenType.GE: ">=",
            TokenType.EQ: "==",
            TokenType.NE: "!=",
            TokenType.AND: "&&",
            TokenType.OR: "||",
            TokenType.NOT: "!",
        }
        return mapping.get(op_type, "?")

    def indent(self):
        return "    " * self.indent_level