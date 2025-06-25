from Preguntas import *
import random

def validar_continuación(mensaje_bienvenida: str = "¿Querés seguir jugando? (S/N)", mensaje_despedida: str = "Fin del juego.") -> bool:
    continuación = input(f"\n{mensaje_bienvenida}\n\n").upper()
    if continuación not in ["S", "N"]:
        raise ValueError
    elif continuación == "N":
        print(f"\n{mensaje_despedida}\n")
        continuación = False 
    else:
        continuación = True
    return continuación

def generar_pregunta_aleatoria(preguntas: list) -> dict | bool:
    if preguntas:
        pregunta_aleatoria = preguntas[random.randint(0, len(preguntas) - 1)]
        preguntas.remove(pregunta_aleatoria)
        print(f"\nPregunta:\n{pregunta_aleatoria["pregunta"]}")
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
    respuesta = int(input("\n"))
    match respuesta:
        case 1: respuesta = "a"
        case 2: respuesta = "b"
        case 3: respuesta = "c"
        case _: raise ValueError
    return respuesta
    
def validar_respuesta(respuesta: str, pregunta: dict) -> bool:
    return respuesta == pregunta["respuesta_correcta"]

def realizar_movimiento(avanzar: bool, tablero: list, posición: int):
    if avanzar == True:
        print("\nRespondiste correctamente. Avanzás una casilla.")
        posición += 1
        if tablero[posición] != 0:
            match tablero[posición]:
                case 1: posición += 1; print("\n¡Encontraste una escalera! La subís y avanzás 1 casilla hacia arriba.")
                case 2: posición += 2; print("\n¡Encontraste una escalera! La subís y avanzás 2 casillas hacia arriba.")
    else:
        print("\nRespondiste incorrectamente. Retrocedés una casilla.")
        posición -= 1
        if tablero[posición] != 0:
            match tablero[posición]:
                case 1: posición -= 1; print("\n¡Pisaste una serpiente! Te arrastró 1 casilla hacia abajo.")
                case 2: posición -= 2; print("\n¡Pisaste una serpiente! Te arrastró 2 casillas hacia abajo.")
                case 3: posición -= 3; print("\n¡Pisaste una serpiente! Te arrastró 3 casillas hacia abajo.")
    return posición

def verificar_estado_del_juego(posición: int) -> bool:
    if posición == 0:
        print("\nCaíste en lo más profundo de la torre y te devoraron las serpientes. ¡Perdiste!\n")
        terminar = True
    elif posición == 30:
        print("\nLograste escalar hacia la cima de la torre y sobrevivir. ¡Ganaste!\n")
        terminar = True
    else:
        terminar = False
    return terminar

def crear_tablero_puntuación(nombre: str, posición: int):
    try:
        with open("Puntuación.csv", "r") as archivo:
            líneas = archivo.readlines()
    except FileNotFoundError:
        líneas = []
    with open("Puntuación.csv", "a") as archivo:
        if len(líneas) == 0:
            archivo.write("jugador,puntuacion\n")
        archivo.write(f"{nombre}, {posición}\n")
    print(f"¡Gracias por jugar, {nombre}! Llegaste a la casilla {posición}")