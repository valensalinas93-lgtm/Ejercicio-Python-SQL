import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # lee el archivo .env y deja sus datos disponibles para os.getenv()

# 1. CONECTAR
conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
# El cursor envía las consultas. Con dictionary=True cada fila es un diccionario.
cursor = conexion.cursor(dictionary=True)

# 2. LEER
cursor.execute("SELECT titulo, precio FROM libros ORDER BY precio DESC LIMIT 3")
for libro in cursor.fetchall():  # fetchall() = todas las filas; fetchone() = una
    print(libro["titulo"], libro["precio"])

# 3. LEER CON DATOS DEL USUARIO
# El valor nunca se pega en el SQL: se pone %s y se pasa aparte en una tupla.
# Así no hay inyección SQL. Con un solo valor la tupla lleva coma: (categoria,)
categoria = input("Categoría (Novela, Ensayo o Filosofía): ")
cursor.execute("SELECT titulo FROM libros WHERE categoria = %s", (categoria,))
print(cursor.fetchall())

# 4. ESCRIBIR
# Sin commit() el cambio no se guarda.
cursor.execute(
    "INSERT INTO libros (titulo, autor, categoria, precio, stock) VALUES (%s, %s, %s, %s, %s)",
    ("Walden", "Henry David Thoreau", "Ensayo", 9.90, 25),
)
conexion.commit()
nuevo_id = cursor.lastrowid  # id de la fila insertada
print("Insertado con id", nuevo_id)

cursor.execute("DELETE FROM libros WHERE id = %s", (nuevo_id,))
conexion.commit()
print("Filas borradas:", cursor.rowcount)  # filas afectadas

# 5. CERRAR
cursor.close()
conexion.close()
