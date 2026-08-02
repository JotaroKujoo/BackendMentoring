# 🟠 Kata 2 - Inventario de Mochila

## Objetivo

Desarrollar un pequeño gestor de inventario utilizando **listas**, reforzando los conceptos de mutabilidad, referencias, funciones y organización del código.

Esta kata no pretende evaluar únicamente el conocimiento de la sintaxis de Python, sino la capacidad para diseñar una solución clara, modular y mantenible.

---

# Situación

Imagina que estás desarrollando un videojuego RPG.

El jugador dispone de una mochila con un conjunto de objetos iniciales.

```python
[
    "Espada",
    "Poción",
    "Escudo"
]
```

El programa deberá permitir gestionar este inventario mediante un menú interactivo.

---

# Funcionalidades

El programa debe ofrecer el siguiente menú:

```text
===== INVENTARIO =====

1. Ver inventario
2. Añadir objeto
3. Eliminar objeto
4. Buscar objeto
5. Salir
```

---

## 1. Ver inventario

Mostrar todos los objetos almacenados en la mochila.

Ejemplo:

```text
1. Espada
2. Poción
3. Escudo
```

---

## 2. Añadir objeto

Solicitar al usuario el nombre de un objeto y añadirlo al inventario.

Ejemplo:

```text
Introduce el objeto:
Arco

Objeto añadido correctamente.
```

---

## 3. Eliminar objeto

Solicitar el nombre de un objeto.

- Si existe, eliminarlo del inventario.
- Si no existe, informar al usuario.

Ejemplo:

```text
Objeto eliminado correctamente.
```

o

```text
Ese objeto no está en la mochila.
```

---

## 4. Buscar objeto

Solicitar el nombre de un objeto.

Mostrar si el objeto se encuentra o no en el inventario.

Ejemplo:

```text
El objeto está en la mochila.
```

o

```text
Objeto no encontrado.
```

---

## 5. Salir

Cerrar el programa.

---

# Restricciones

Durante esta kata únicamente está permitido utilizar:

- Listas
- Funciones
- Bucles
- Condicionales

No está permitido utilizar:

- Diccionarios
- Sets
- Clases
- Archivos

---

# Objetivos de aprendizaje

Esta kata está diseñada para practicar:

- Manipulación de listas.
- Mutabilidad de los objetos.
- Organización del código mediante funciones.
- Validación de entradas del usuario.
- Separación de responsabilidades.
- Diseño de programas sencillos con estado.

---

# Criterios de evaluación

La revisión del código tendrá especialmente en cuenta:

- Claridad de la solución.
- Nombres de variables y funciones.
- División del programa en funciones.
- Ausencia de código duplicado.
- Correcta validación de entradas.
- Legibilidad y mantenibilidad.
- Aplicación de buenas prácticas vistas durante la mentoría.

---

# Reflexión

Antes de comenzar a programar responderé las siguientes preguntas:

1. ¿Qué funciones necesita el programa?
2. ¿Qué información debe intercambiar cada función?
3. ¿Qué variable representa el estado del programa?
4. ¿Qué situaciones debo validar antes de ejecutar una acción?

El objetivo de esta kata no es únicamente que el programa funcione, sino aprender a diseñar una solución antes de escribir código.
