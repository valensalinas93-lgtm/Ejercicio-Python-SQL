# 📚 Python + SQL: programa de la librería

Hasta ahora las consultas las escribías tú en Workbench. Aquí las lanza un programa de Python: el programa de mostrador de una librería, donde quien atiende no sabe SQL y solo elige opciones de un menú.

## 🛠️ Preparar

1. En Workbench, abre `libreria.sql` (**File → Open SQL Script…**) y ejecútalo entero. Al refrescar **Schemas** debe aparecer `libreria`, con 22 filas en la tabla `libros`.
2. Abre la carpeta `python-sql` en VS Code y, en su terminal:

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install mysql-connector-python python-dotenv
   ```

3. Copia `.env.example` como `.env` y rellénalo con los datos de tu conexión de Workbench (clic derecho sobre la conexión → **Edit Connection**).

La contraseña va en `.env` y no en el código: ese archivo está en el `.gitignore` y no se sube a GitHub.

## 💻 Ejercicio

`ejemplo.py` es un programa corto que lee, escribe y borra en la base de datos. Ejecútalo y léelo antes de empezar.

El trabajo se hace en `ejercicio.py`. La opción 1 ya funciona; las demás te tocan a ti.

```bash
python ejercicio.py
```

### 1. 📖 Ver libros

Ya está hecha. Cámbiala para que salgan del más caro al más barato.

### 2. 🔍 Buscar por autor

Pregunta un autor y muestra solo sus libros.

Con George Orwell salen tres. Prueba también con un autor que no esté.

### 3. 📉 Stock bajo

Pregunta un número y muestra los libros con menos ejemplares que ese número, primero los que menos tienen.

Con 6 salen tres, dos de ellos agotados.

### 4. 💶 Vender

Pregunta el id del libro y la cantidad.

- Si el libro no existe, avisa.
- Si no hay stock suficiente, dice cuántos ejemplares quedan.
- Si lo hay, resta el stock y muestra el total a cobrar.

Vende 2 ejemplares del libro 1: cobra 25.90 y el stock baja de 12 a 10. Compruébalo también en Workbench.

### 5. ➕ Añadir libro

Pregunta título, autor, categoría, precio y stock, guarda el libro y muestra el id que le ha tocado.

El libro nuevo debe aparecer en la opción 1 y poder venderse.

### Reto Extra (Opcional)

- Opción 6: valor del almacén, la suma de precio × stock de todos los libros.
- Opción 7: subir el precio un porcentaje a toda una categoría y decir cuántos libros han cambiado.
- Que el programa no se rompa si en "cantidad" alguien escribe letras.

## 🚑 Si algo falla

| Mensaje | Qué hacer |
|---|---|
| `No module named 'mysql'` o `'dotenv'` | Activa el entorno e instala las librerías (punto 2 de Preparar) |
| `Access denied for user 'root'` | La contraseña de `.env` no es la de Workbench |
| `Access denied` con `using password: NO` | No encuentra el `.env`: debe llamarse así y estar en esta carpeta |
| `Can't connect to MySQL server` | Entra desde Workbench. Si conecta, revisa `DB_HOST` y `DB_PORT` en `.env` |
| `Unknown database 'libreria'` | Falta ejecutar `libreria.sql` (punto 1 de Preparar) |
| `Not all parameters were used` | No hay los mismos `%s` que valores |
| `Unread result found` | Hiciste una consulta y no recogiste el resultado |
| Los datos están hechos un lío | Vuelve a ejecutar `libreria.sql` y empiezas de cero |

---

¡Felices consultas y happy coding! 🧡

Factoría F5
