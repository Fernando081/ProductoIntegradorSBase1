# ============================================
# PROGRAMA AVANZADO: Análisis de calificaciones
# ============================================

print("=== SISTEMA DE ANÁLISIS DE CALIFICACIONES ===")

# Datos de entrada (simulados)
num_estudiantes = 5
calificaciones = [85, 92, 78, 90, 68]
nombres = ["Ana", "Luis", "Carlos", "Marta", "Jose"]

# Variables de control
suma_calificaciones = 0
calificacion_maxima = 0
calificacion_minima = 100
aprobados = 0
reprobados = 0

# Procesar calificaciones con while
indice = 0
while indice < num_estudiantes:
    cal = calificaciones[indice]
    nombre = nombres[indice]

    print("Estudiante:")
    print(nombre)
    print("Calificación:")
    print(cal)

    # Acumular suma
    suma_calificaciones = suma_calificaciones + cal

    # Actualizar máximo
    if cal > calificacion_maxima:
        calificacion_maxima = cal
        nombre_maximo = nombre

    # Actualizar mínimo
    if cal < calificacion_minima:
        calificacion_minima = cal
        nombre_minimo = nombre

    # Contar aprobados y reprobados (aprueba con 70)
    if cal >= 70:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    indice = indice + 1

# Calcular promedio
promedio = suma_calificaciones / num_estudiantes

print("=== RESULTADOS DEL ANÁLISIS ===")
print("Número de estudiantes:")
print(num_estudiantes)
print("Suma de calificaciones:")
print(suma_calificaciones)
print("Promedio:")
print(promedio)
print("Calificación más alta:")
print(calificacion_maxima)
print("Estudiante con mejor calificación:")
print(nombre_maximo)
print("Calificación más baja:")
print(calificacion_minima)
print("Estudiante con peor calificación:")
print(nombre_minimo)
print("Aprobados:")
print(aprobados)
print("Reprobados:")
print(reprobados)

# Evaluación del grupo
if promedio >= 90:
    print("Excelente rendimiento grupal")
else:
    if promedio >= 80:
        print("Buen rendimiento grupal")
    else:
        if promedio >= 70:
            print("Rendimiento grupal aceptable")
        else:
            print("Rendimiento grupal bajo - necesita mejora")

# Cálculo adicional: desviación simple
suma_diferencias = 0
indice = 0
while indice < num_estudiantes:
    diferencia = calificaciones[indice] - promedio
    if diferencia < 0:
        diferencia = diferencia * -1  # valor absoluto
    suma_diferencias = suma_diferencias + diferencia
    indice = indice + 1

desviacion_promedio = suma_diferencias / num_estudiantes
print("Desviación promedio absoluta:")
print(desviacion_promedio)

# Análisis por rangos
rango_alto = 0
rango_medio = 0
rango_bajo = 0

indice = 0
while indice < num_estudiantes:
    cal = calificaciones[indice]
    if cal >= 90:
        rango_alto = rango_alto + 1
    else:
        if cal >= 70:
            rango_medio = rango_medio + 1
        else:
            rango_bajo = rango_bajo + 1
    indice = indice + 1

print("=== DISTRIBUCIÓN POR RANGOS ===")
print("Excelente (>=90):")
print(rango_alto)
print("Aprobado (70-89):")
print(rango_medio)
print("Reprobado (<70):")
print(rango_bajo)

# Expresiones complejas para probar
a = 15
b = 4
c = 20
d = 2
e = 3

resultado_final = ((a * b) - (c / d)) + (a % b) - (c - a)
es_consistente = (promedio >= 70) and (aprobados > reprobados)
mejora_necesaria = (reprobados > 0) and (promedio < 75)

print("=== PRUEBAS ADICIONALES ===")
print("Resultado final de expresión:")
print(resultado_final)
print("Es consistente (promedio>=70 y aprobados>reprobados):")
print(es_consistente)
print("Mejora necesaria (reprobados>0 y promedio<75):")
print(mejora_necesaria)

print("=== FIN DEL PROGRAMA ===")