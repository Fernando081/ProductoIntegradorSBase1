import sys
import os
from grammar.lexer import Lexer
from parser import Parser
from token_types import TokenType  # 👈 IMPORTANTE


def main():
    # Pedir el nombre del archivo por consola
    print("=" * 50)
    print("TRANSPILADOR PYTHON -> JAVA")
    print("=" * 50)

    filename = input("Ingresa la ruta del archivo .py o .txt: ").strip()

    # Quitar comillas si las tiene
    filename = filename.strip('"').strip("'")

    if not os.path.exists(filename):
        print(f"\n❌ Error: No se encontró el archivo '{filename}'")
        print("Asegúrate de que el archivo existe en la ruta especificada.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            source_code = f.read()
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {e}")
        return

    print(f"\n📄 Leyendo archivo: {filename}")
    print("-" * 50)

    # Tokenizar
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    print("\n=== TOKENS GENERADOS ===")
    for token in tokens:
        if token.type not in [TokenType.INDENT, TokenType.DEDENT, TokenType.NEWLINE]:
            print(f"  {token}")

    # Parsear y generar Java
    parser = Parser(tokens)
    java_code = parser.parse()

    if parser.errors:
        print("\n=== ERRORES DETECTADOS ===")
        for err in parser.errors:
            print(f"  ❌ {err}")
    else:
        output_filename = filename.replace(".py", ".java").replace(".txt", ".java")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(java_code)
        print(f"\n✅ CÓDIGO JAVA GENERADO EXITOSAMENTE")
        print(f"📁 Archivo: {output_filename}")
        print("\n=== CÓDIGO JAVA GENERADO ===")
        print("-" * 50)
        print(java_code)
        print("-" * 50)


if __name__ == "__main__":
    main()