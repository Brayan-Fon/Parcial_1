# Parcial – Paradigmas de Programación

## 1. Estructural – Descripción del error
Se usó el operador de asignación (`=`) en lugar del operador de comparación (`==`).

En Python, `=` sirve para asignar valores a variables, no para comparar valores.

El uso de `=` dentro de una condición genera un `SyntaxError`.

---

## 2. Corrección aplicada


def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador

print(cuenta_pares([1, 2, 3, 4, 5, 6]))


---

## 3. OOP

### ❌ Error encontrado
Uso incorrecto de variables dentro del método `area`.

En el método `area`, se usaban las variables `base` y `altura` directamente, pero estas no están definidas en el alcance local del método.

En realidad, las dimensiones del rectángulo se guardaron como atributos de instancia: `self.base` y `self.altura`.

Por eso, la línea correcta debe referenciar esos atributos con `self`.

### Correccion aplicada

def area(self):
        return self.base * self.altura


