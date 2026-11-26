import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # lee el archivo .env y deja sus datos disponibles para os.getenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
cursor = conexion.cursor(dictionary=True)  # cada fila llega como un diccionario


def mostrar(libros):
    """Enseña una lista de libros, uno por línea."""
    if not libros:
        print("No hay libros que mostrar.")
    for libro in libros:
        print(
            libro["id"], "|", libro["titulo"], "|", libro["autor"], "|",
            libro["categoria"], "|", libro["precio"], "€ | stock:", libro["stock"],
        )


def ver_libros():
    cursor.execute("SELECT * FROM libros ORDER BY titulo")
    mostrar(cursor.fetchall())


def buscar_por_autor():
    print("Sin hacer todavía (paso 2)")


def stock_bajo():
    print("Sin hacer todavía (paso 3)")


def vender():
    print("Sin hacer todavía (paso 4)")


def anadir_libro():
    print("Sin hacer todavía (paso 5)")


while True:
    print()
    print("1. Ver libros")
    print("2. Buscar por autor")
    print("3. Stock bajo")
    print("4. Vender")
    print("5. Añadir libro")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        ver_libros()
    elif opcion == "2":
        buscar_por_autor()
    elif opcion == "3":
        stock_bajo()
    elif opcion == "4":
        vender()
    elif opcion == "5":
        anadir_libro()
    elif opcion == "0":
        break
    else:
        print("Esa opción no existe.")

cursor.close()
conexion.close()
