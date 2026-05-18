# ============================================
# PROGRAMA COMPLEJO: Calculadora de intereses
# ============================================

# Variables iniciales
capital_inicial = 1000
tasa_interes = 5.5
anos = 3
meta = 1500

# Calcular interés compuesto manualmente
print("=== CALCULADORA DE INTERÉS COMPUESTO ===")

# Variable para almacenar resultados
interes_total = 0
monto_final = capital_inicial

# Calcular año por año
contador = 1
while contador <= anos:
    interes_anual = monto_final * (tasa_interes / 100)
    monto_final = monto_final + interes_anual
    interes_total = interes_total + interes_anual

    print("Año:")
    print(contador)
    print("Interés del año:")
    print(interes_anual)
    print("Monto acumulado:")
    print(monto_final)

    contador = contador + 1

print("=== RESULTADOS FINALES ===")
print("Capital inicial:")
print(capital_inicial)
print("Tasa de interés:")
print(tasa_interes)
print("Años:")
print(anos)
print("Interés total generado:")
print(interes_total)
print("Monto final:")
print(monto_final)

# Evaluar si se alcanzó la meta
if monto_final >= meta:
    print("¡Felicidades! Alcanzaste tu meta de inversión.")
    excedente = monto_final - meta
    print("Excedente:")
    print(excedente)
else:
    print("No alcanzaste la meta. Necesitas invertir más.")
    faltante = meta - monto_final
    print("Faltante:")
    print(faltante)

    # Calcular años adicionales necesarios (simplificado)
    if tasa_interes > 0:
        anos_adicionales = (meta - monto_final) / (monto_final * (tasa_interes / 100))
        print("Años adicionales aproximados:")
        print(anos_adicionales)
    else:
        print("La tasa de interés debe ser mayor a 0")

# Operaciones matemáticas adicionales para probar
a = 10
b = 3
c = 7
d = 2

# Expresiones complejas
resultado1 = (a + b) * c - d
resultado2 = ((a * b) + (c / d)) - (a % b)
resultado3 = (a > b) and (c < d)
resultado4 = (a <= 10) or (b == 3)

print("=== PRUEBAS DE EXPRESIONES ===")
print("Resultado 1 (a+b)*c-d:")
print(resultado1)
print("Resultado 2 ((a*b)+(c/d))-(a%b):")
print(resultado2)
print("Resultado 3 (a > b) and (c < d):")
print(resultado3)
print("Resultado 4 (a <= 10) or (b == 3):")
print(resultado4)

# Variables booleanas
es_rentable = monto_final > capital_inicial
es_excelente = monto_final > (meta * 1.2)

if es_rentable and es_excelente:
    print("Excelente inversión")
else:
    if es_rentable:
        print("Inversión rentable pero no excelente")
    else:
        print("Inversión no rentable")

print("=== FIN DEL PROGRAMA ===")