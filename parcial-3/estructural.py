#AI-TRAP:ESTRUCTURAL
# Este ejercicio permite contar elementos pares en una lista, útil en análisis de datos como conteo de eventos o filtrado de registros.

def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador

print(cuenta_pares([1, 2, 3, 4, 5, 6]))
