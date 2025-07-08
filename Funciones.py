from Preguntas import *
import random

def validar_continuación(mensaje_bienvenida: str = "¿Querés seguir jugando? (S/N)", mensaje_despedida: str = "Fin del juego.") -> bool:
    """
    Solicita al usuario si desea continuar jugando.

    Parámetros:
        mensaje_bienvenida (str): Mensaje que se muestra al preguntar si desea continuar.
        mensaje_despedida (str): Mensaje que se muestra al finalizar el juego.

    Devuelve:
        bool: True si el usuario desea continuar, False si no.
    """
    continuación = input(f"\n{mensaje_bienvenida}\n\n").upper()
    while continuación != "S" and continuación != "N":
        continuación = input("\nEl valor ingresado es incorrecto. Volvé a ingresar el valor solicitado.\n\n").upper()
    if continuación == "N":
        print(f"\n{mensaje_despedida}")
    return continuación == "S"

def generar_pregunta_aleatoria(preguntas: list) -> dict | bool:
    """
    Selecciona y muestra una pregunta aleatoria de la lista de preguntas.

    Parámetros:
        preguntas (list): Lista de preguntas disponibles.

    Devuelve:
        dict: Pregunta seleccionada si hay preguntas disponibles.
        bool: False si no quedan preguntas.
    """
    if preguntas:
        pregunta_aleatoria = preguntas[random.randint(0, len(preguntas) - 1)]
        preguntas.remove(pregunta_aleatoria)
        print(f"\nPregunta:\n{pregunta_aleatoria['pregunta']}")
        respuestas = list(pregunta_aleatoria.values())
        print(f"\nOpciones:")
        for i in range(1, len(respuestas) - 1):
            print(f"{i}) {respuestas[i]}")
        resultado = pregunta_aleatoria
    else:
        print("\n¡Se acabaron las preguntas! Fin del juego.\n")
        resultado = False
    return resultado

def escribir_respuesta() -> str:
    """
    Solicita al usuario que ingrese una respuesta y la valida.

    Parámetros:
        Ninguno.

    Devuelve:
        str: Letra correspondiente a la opción elegida ('a', 'b' o 'c').
    """
    respuesta = int(input("\n"))
    match respuesta:
        case 1: respuesta = "a"
        case 2: respuesta = "b"
        case 3: respuesta = "c"
        case _: raise ValueError
    return respuesta
    
def verificar_respuesta(respuesta: str, pregunta: dict) -> bool:
    """
    Verifica si la respuesta ingresada es correcta.

    Parámetros:
        respuesta (str): Respuesta del usuario.
        pregunta (dict): Pregunta con la respuesta correcta.

    Devuelve:
        bool: True si la respuesta es correcta, False si no.
    """
    return respuesta == pregunta["respuesta_correcta"]

def realizar_movimiento(avanzar: bool, tablero: list, posición: int) -> int:
    """
    Actualiza la posición del jugador según la respuesta y los efectos del tablero.
    """
    if avanzar:
        print("\nRespondiste correctamente. Avanzás una casilla.")
        posición += 1
        posición = aplicar_movimientos_extra(posición, tablero, "\n¡Encontraste una escalera! La subís y avanzás {} casilla/s hacia arriba.", sumar)
    else:
        print("\nRespondiste incorrectamente. Retrocedés una casilla.")
        posición -= 1
        posición = aplicar_movimientos_extra(posición, tablero, "\n¡Pisaste una serpiente! Te arrastró {} casilla/s hacia abajo.", restar)
    return posición

def aplicar_movimientos_extra(posición: int, tablero: list, mensaje: str, operación: callable) -> int:
    """
    Aplica el objeto del tablero (escalera o serpiente) si corresponde.

    Parámetros:
        posición (int): Posición actual del jugador.
        tablero (list): Lista que representa el tablero.
        mensaje (str): Mensaje a mostrar si hay efecto.
        operación (callable): Suma o resta, según el efecto.

    Devuelve:
        int: Nueva posición del jugador.
    """
    if tablero[posición] != 0:
        print(mensaje.format(tablero[posición]))
        posición = operación(posición, tablero[posición])
    return posición

def sumar(número: int, cantidad: int) -> int:
    """
    Suma dos números enteros.

    Parámetros:
        número (int): Primer número.
        cantidad (int): Número a sumar.

    Devuelve:
        int: Resultado de la suma.
    """
    return número + cantidad

def restar(número: int, cantidad: int) -> int:
    """
    Resta dos números enteros.

    Parámetros:
        número (int): Primer número.
        cantidad (int): Número a restar.

    Devuelve:
        int: Resultado de la resta.
    """
    return número - cantidad

def verificar_estado_del_juego(posición: int) -> bool:
    """
    Verifica si el juego ha terminado según la posición del jugador.

    Parámetros:
        posición (int): Posición actual del jugador.

    Devuelve:
        bool: True si el juego terminó, False si continúa.
    """
    terminar = False
    if posición == 0 or posición == 30:
        terminar = True
    return terminar

def crear_tablero_puntuación(nombre: str, posición: int):
    """
    Guarda la puntuación del jugador en un archivo CSV.

    Parámetros:
        nombre (str): Nombre del jugador.
        posición (int): Casilla alcanzada por el jugador.
    """
    try:
        with open("Puntuación.csv", "r") as archivo:
            líneas = archivo.readlines() # Intenta leer el archivo
    except FileNotFoundError:
        líneas = [] # Si no existe, líneas pasa a ser una lista vacía
    with open("Puntuación.csv", "a") as archivo:
        if len(líneas) == 0:
            archivo.write("jugador,puntuacion\n") # Si está vacío, escribe la cabecera
        archivo.write(f"{nombre}, {posición}\n") 
    print(f"¡Gracias por jugar, {nombre}! Llegaste a la casilla {posición}")