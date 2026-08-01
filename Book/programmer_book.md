# 📖 The Programmer Book

> "Un buen programador no memoriza soluciones; aprende a pensar mejor."

Este libro recoge las conclusiones obtenidas durante mi proceso de aprendizaje.
No pretende ser una documentación de Python, sino una colección de principios y reflexiones que me ayuden a escribir mejor código y a pensar como un ingeniero de software.

---

# Capítulo 1 - Variables

### Una variable debe representar fielmente la realidad que describe.

No debo modificar el significado de una variable para que una condición funcione.

Es preferible adaptar la lógica del programa antes que romper el significado de los datos.

**Ejemplo:**

❌ `intentos = 1` cuando todavía no ha habido ningún intento.

✔ `intentos = 0` y adaptar correctamente la condición del bucle.

---

# Capítulo 2 - Condiciones

### Una condición debe expresar la intención del programa.

No basta con que una condición funcione.

Debe ser fácil de leer y transmitir claramente la regla de negocio.

**Ejemplo:**

❌ `while intentos != max_intentos`

✔ `while intentos < max_intentos`

La segunda expresa exactamente la intención:

> "Mientras queden intentos."

---

# Capítulo 3 - Funciones

### Una función debe tener un contrato claro.

Antes de escribir una función debo ser capaz de responder:

- ¿Qué recibe?
- ¿Qué devuelve?
- ¿Qué responsabilidad tiene?

Si una función devuelve un tipo distinto dependiendo del camino seguido, su comportamiento será difícil de entender.

---

### Una función debería devolver siempre el tipo de dato esperado.

Si el contrato indica que devuelve un `bool`, todos los caminos de ejecución deben devolver un `bool`.

Nunca debo depender de retornos implícitos como `None`.

---

# Capítulo 4 - Resolver problemas

### Antes de escribir código, divide el problema.

Los problemas grandes rara vez se resuelven de una vez.

Primero los divido en pequeñas tareas independientes.

Después resuelvo cada una por separado.

---

### No pienso en código. Pienso en el algoritmo.

El código es la traducción de una idea.

Si no soy capaz de explicar el algoritmo con palabras, probablemente todavía no entiendo el problema.

---

# Capítulo 5 - Errores

### Un error es información.

Cuando algo falla no debo preguntarme:

> "¿Cómo lo arreglo?"

Primero debo preguntarme:

> "¿Qué me está diciendo este error?"

---

### No busco que funcione.

Busco entender por qué funciona.

Una solución sin comprensión es solo código copiado.

---

# Capítulo 6 - Legibilidad

### El código se lee muchas más veces de las que se escribe.

Siempre debo escribir pensando en la persona que lo leerá dentro de seis meses.

Aunque esa persona sea yo mismo.

---

### El código debe contar una historia.

Un buen nombre de variable y una buena estructura eliminan la necesidad de comentarios innecesarios.

---

# Capítulo 7 - Mentalidad

### Programar consiste en tomar decisiones.

La sintaxis se aprende.

El criterio se construye.

---

### La IA no debe pensar por mí.

La IA debe ayudarme a pensar mejor.

Mi objetivo no es obtener respuestas rápidas.

Mi objetivo es desarrollar criterio para poder evaluar si una respuesta es correcta.

---

### La calidad del razonamiento es más importante que la velocidad.

Prefiero invertir una hora entendiendo un concepto que cinco minutos memorizando una solución.

El conocimiento construido permanece.
