# Transpilador Básico: Python a Java

Este proyecto es un transpilador construido en Python que analiza código fuente básico de Python y genera su equivalente en código Java. A continuación, se detalla la arquitectura del proyecto y la función de cada uno de sus componentes principales, de acuerdo al código fuente.

## Estructura del Proyecto y Análisis de Archivos

### 1. Análisis Léxico (Lexer)
**Archivo:** `grammar/lexer.py`
* **Propósito:** Contiene la clase `Lexer` que toma el código fuente de Python como una cadena de texto y lo procesa carácter por carácter para dividirlo en una secuencia de "tokens" comprensibles por el analizador.
* **Características Principales:**
    * Reconoce palabras reservadas clave de Python (`if`, `else`, `elif`, `while`, `for`, `print`, `True`, `False`, etc.).
    * Maneja la indentación de Python dinámicamente (`INDENT` y `DEDENT`) a través de un sistema de pilas (`self.indent_stack`). Esto es fundamental porque traduce la estructura visual del código Python en bloques jerárquicos.
    * Filtra y descarta los comentarios (`#`) y los espacios vacíos, pero mantiene un registro preciso de la línea y columna para poder reportar errores.

### 2. Definición de Tokens
**Archivo:** `src/token_types.py`
* **Propósito:** Define todos los tipos de elementos sintácticos válidos del lenguaje en una estructura de enumeración (`TokenType`).
* **Clasificaciones:** Enumera palabras reservadas, identificadores, literales (números y cadenas), operadores de asignación, comparación y lógicos, además de delimitadores (paréntesis, llaves, saltos de línea e indentación).

**Archivo:** `src/token_class.py`
* **Propósito:** Contiene la `dataclass` llamada `Token`. 
* **Características Principales:** Encapsula la información de cada símbolo encontrado por el Lexer. Sus atributos principales son el tipo de token, su valor en texto crudo, y sus coordenadas de ubicación (`line` y `column`).

### 3. Análisis Sintáctico y Generación de Código (Parser)
**Archivo:** `src/parser.py`
* **Propósito:** Alberga la clase `Parser`, que consume el arreglo de tokens del Lexer para comprender la gramática del programa y emitir el código fuente objetivo (Java).
* **Características Principales:**
    * Estructura la base del archivo resultante generando la clase estándar `public class Main` y su método estático `main`.
    * Parsea e interpreta instrucciones como funciones `print()`, asignaciones de variables (`=`), condicionales (`if`/`elif`/`else`) y estructuras cíclicas (`while`).
    * **Inferencia de Tipos (`infer_type`):** Como Java tiene un tipado fuerte y Python dinámico, este archivo cuenta con un pequeño analizador que deduce si el valor de una variable debe ser de tipo `int`, `double`, `boolean` o `String` en Java.
    * Interpreta operadores booleanos propios de Python (`and`, `or`, `not`) y los inyecta como su contraparte directa en Java (`&&`, `||`, `!`).

### 4. Punto de Entrada de la Aplicación (Main)
**Archivo:** `src/main.py`
* **Propósito:** Actúa como el controlador principal e interfaz por línea de comandos para que el usuario interactúe con el transpilador.
* **Flujo de ejecución:**
    1. Solicita interactivamente la ruta del archivo de texto o de Python (`.py`).
    2. Lee el archivo y pasa el texto completo al `Lexer`.
    3. Imprime por consola una tabla de los "Tokens Generados" para propósitos de depuración.
    4. Proporciona la lista de tokens al `Parser` para ensamblar el código final.
    5. Guarda automáticamente el resultado en disco reemplazando la extensión del archivo a `.java` y notificando el éxito o los errores detectados en pantalla.

### 5. Archivos de Prueba
**Archivo:** `tests/valid/entrada.py`
* **Propósito:** Un archivo de ejemplo en Python utilizado para verificar el transpilador. Muestra variables, un condicional básico `if/else` y un bucle `while`.

**Archivo:** `tests/valid/entrada.java`
* **Propósito:** Muestra el resultado esperado que el transpilador generará a partir del código en Python. Demuestra cómo envuelve todo en la clase `Main` y convierte la sintaxis a los estándares de Java (añadiendo `;`, formateando los bloques con llaves `{}` e iterando correctamente).
