# 🟠 Misión 1 - Analizador de Strings

## 📖 Objetivo

En esta misión pondrás en práctica todos los conceptos aprendidos sobre **strings**, **indexación** y **slicing**.

El objetivo no es únicamente que el programa funcione, sino demostrar que comprendes cómo acceder y recorrer una cadena de texto utilizando únicamente los conceptos básicos de Python.

---

## 🎯 Conceptos que se practican

- Variables
- Strings
- Indexación positiva
- Indexación negativa
- Slicing
- `len()`
- Bucles `for`
- Condicionales `if`

---

## 📋 Enunciado

Crea una función llamada:

```python
def analizar_texto(texto):
```

La función recibirá una cadena de texto y deberá mostrar la siguiente información:

Si recibe:

```python
"Programacion"
```

La salida deberá ser similar a:

```text
Texto original: Programacion

Primer carácter: P
Último carácter: n

Primeros 4 caracteres: Prog
Últimos 4 caracteres: cion

Texto invertido: noicamargorP

Número de caracteres: 12

Caracteres en posiciones pares:
P
o
r
m
c
o

Caracteres en posiciones impares:
r
g
a
a
i
n
```

> **Importante:** La salida no tiene que ser idéntica carácter por carácter, pero sí debe contener toda la información solicitada.

---

## 🚫 Restricciones

No está permitido utilizar:

- `reversed()`
- `[::-1]`
- `split()`
- `join()`
- `replace()`
- Cualquier otra función que resuelva directamente el problema.

Solo puedes utilizar:

- Variables
- `for`
- `if`
- Indexación
- Slicing
- `len()`

---

## 💡 Recomendación

Antes de escribir código, divide el problema en tareas pequeñas.

Por ejemplo:

1. Mostrar el texto original.
2. Obtener el primer carácter.
3. Obtener el último carácter.
4. Obtener los primeros cuatro caracteres.
5. Obtener los últimos cuatro caracteres.
6. Contar los caracteres.
7. Mostrar los caracteres en posiciones pares.
8. Mostrar los caracteres en posiciones impares.
9. Invertir el texto manualmente.

Una vez tengas el algoritmo claro, comienza a programar.

---

## 🎯 Objetivo oculto

Esta misión está diseñada para practicar la capacidad de dividir un problema grande en problemas pequeños.

No busques únicamente que el código funcione. Piensa en cómo organizar la solución antes de escribirla.

---

## 📂 Entrega

El repositorio deberá contener al menos:

```
Mision-01-Analizador-Strings/
│
├── README.md
└── main.py
```

---

## ⭐ Extra (Opcional)

Si terminas la misión antes de tiempo, añade una comprobación para que la función funcione correctamente con:

- Una cadena vacía (`""`)
- Un único carácter (`"A"`)
- Una palabra de menos de cuatro caracteres

No utilices `try/except` para resolver estos casos.

---

## 📌 Criterios de evaluación

Durante la revisión se evaluará:

- Correctitud del programa.
- Claridad del algoritmo.
- Legibilidad del código.
- Nombres de variables.
- Uso correcto de la indexación y el slicing.
- Calidad de la solución.
