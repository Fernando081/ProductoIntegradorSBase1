\# Proyecto\_Integrador\_Base\_1\_Equipo\_S.W.A.T.\_2026-1



\# Python-to-Java Transpilador - Analizador Léxico y Sintáctico



Breve descripción del lenguaje y propósito del lexer:

Este proyecto implementa un transpilador funcional que convierte un subconjunto del lenguaje Python a código Java equivalente. Incluye un analizador léxico que maneja correctamente la indentación estricta de Python (generando tokens INDENT/DEDENT) y un analizador sintáctico que genera bloques delimitados por llaves al estilo Java, con inferencia básica de tipos.



\## Información del Curso



\- \*\*Materia:\*\* Programación de Sistemas Base 1

\- \*\*Institución:\*\* Universidad Autónoma de Tamaulipas

\- \*\*Semestre:\*\* 2026-1

\- \*\*Profesor:\*\* Muñoz Quintero Dante Adolfo



\## Integrantes del Equipo



| Nombre | Matrícula |

|--------|-----------|

| Suarez Martinez Maciel Francisco | 2213332213 |

| Estrada Olvera Frank | 2211330015 |

| Ortega Resendiz Luis Fernando | 2183330150 |



\## Descripción del Lenguaje



El lenguaje soportado es un subconjunto de Python orientado a cálculos aritméticos, asignaciones de variables, estructuras condicionales (`if`, `elif`, `else`) y ciclos (`while`). El transpilador traduce este código a un programa Java válido dentro de una clase principal llamada `Main`, infiriendo tipos como `int`, `double`, `boolean` y `String`.



\*\*Características principales:\*\*

\- Manejo de indentación (conversión a llaves `{}` en Java)

\- Inferencia de tipos en tiempo de traducción

\- Soporte para expresiones relacionales y lógicas básicas

\- Manejo de errores léxicos y de indentación



\## Tokens Reconocidos



| Categoría | Ejemplos | Descripción |

|-----------|----------|-------------|

| KEYWORD | `if`, `else`, `elif`, `while`, `print`, `True`, `False` | Palabras reservadas del lenguaje |

| IDENTIFIER | `x`, `total`, `contador` | Nombres de variables o funciones |

| NUMBER | `10`, `3.14`, `0` | Números enteros o flotantes |

| STRING | `"hola mundo"` | Cadenas de texto |

| OPERATOR | `+`, `-`, `\*`, `/`, `%`, `=`, `==`, `>`, `<`, `!=` | Operadores matemáticos y lógicos |

| INDENT / DEDENT | (Espacios al inicio de línea) | Controlan la estructura de bloques de código |

| DELIMITERS | `(`, `)`, `:`, `,` | Delimitadores de sintaxis |

| COMMENT | `# comentario` | Comentarios de línea (ignorados) |



\## Cómo ejecutar



\### Requisitos previos

\- Python 3.8 o superior instalado

\- Java JDK 11 o superior (para ejecutar el código generado)



\### Paso a paso



1\. \*\*Clonar el repositorio\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com/Fernando081/ProductoIntegradorSBase1.git

&#x20;  cd Proyecto\_Integrador\_Base\_1\_Equipo\_S.W.A.T.\_2026-1
