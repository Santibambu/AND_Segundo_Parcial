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
    while continuación not in ["S", "N"]:
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

def realizar_movimiento(avanzar: bool, tablero: list, posición: int):
    """
    Actualiza la posición del jugador según la respuesta y el tablero.

    Parámetros:
        avanzar (bool): True si la respuesta fue correcta, False si no.
        tablero (list): Lista que representa el tablero.
        posición (int): Posición actual del jugador.

    Devuelve:
        int: Nueva posición del jugador.
    """
    if avanzar == True:
        print("\nRespondiste correctamente. Avanzás una casilla.")
        posición += 1
        if tablero[posición] != 0:
            print(f"\n¡Encontraste una escalera! La subís y avanzás {tablero[posición]} casilla/s hacia arriba.")
            posición += tablero[posición]
    else:
        print("\nRespondiste incorrectamente. Retrocedés una casilla.")
        posición -= 1
        if tablero[posición] != 0:
            print(f"\n¡Pisaste una serpiente! Te arrastró {tablero[posición]} casilla/s hacia abajo.")
            posición -= tablero[posición]
    return posición

def verificar_estado_del_juego(posición: int) -> bool:
    """
    Verifica si el juego ha terminado según la posición del jugador.

    Parámetros:
        posición (int): Posición actual del jugador.

    Devuelve:
        bool: True si el juego terminó, False si continúa.
    """
    terminar = True
    if posición not in [0, 30]:
        terminar = False
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