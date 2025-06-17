from Preguntas import *
import random

def jugar_serpientes_y_escaleras():
    global posición_actual

    jugar = validar_continuación("¡Bienvenido a Serpientes y Escaleras! ¿Querés comenzar el juego? (S/N)", "Cerrando el juego...")     
    if jugar:
        nombre_jugador = input("\nIngresá tu nombre para continuar.\n\n")
        while True:
            pregunta_actual = generar_pregunta_aleatoria(preguntas)
            if not pregunta_actual:
                break
            else:
                respuesta_actual = escribir_respuesta()
                movimiento = validar_respuesta(respuesta_actual, pregunta_actual)
                posición_actual = realizar_movimiento(movimiento, tablero, posición_actual)
                if verificar_estado_del_juego(posición_actual):
                    break
                else:
                    continuar = validar_continuación()
                    if not continuar:
                        break
        crear_tablero_puntuación(nombre_jugador, posición_actual)

def validar_continuación(mensaje_bienvenida: str = "¿Querés seguir jugando?", mensaje_despedida: str = "Fin del juego.") -> bool:
    print(f"\n{mensaje_bienvenida}")
    while True:
        continuación = input("\n").upper()
        if continuación != "S":
            if continuación == "N":
                print(f"\n{mensaje_despedida}\n")
                continuación = False
                break
            else:
                print("\nEl valor ingresado es incorrecto. Volvé a ingresar el valor solicitado.")
        else:
            continuación = True
            break
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
        print("\n¡Se acabaron las preguntas! Fin del juego.")
        resultado = False
    return resultado

def escribir_respuesta() -> str:
    while True:
        try:
            respuesta = int(input("\n"))
            match respuesta:
                case 1: respuesta = "a"
                case 2: respuesta = "b"
                case 3: respuesta = "c"
                case _: raise ValueError
            return respuesta
        except ValueError:
            print("\nEl valor ingresado es incorrecto. Volvé a ingresar el valor solicitado.")
    
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
        print("\nHa respondido incorrectamente. Retrocede una casilla.")
        posición -= 1
        if tablero[posición] != 0:
            match tablero[posición]:
                case 1: posición -= 1; print("\n¡Pisaste una serpiente! Sos arrastrado 1 casilla hacia abajo.")
                case 2: posición -= 2; print("\n¡Pisaste una serpiente! Sos arrastrado 2 casillas hacia abajo.")
                case 3: posición -= 3; print("\n¡Pisaste una serpiente! Sos arrastrado 3 casillas hacia abajo.")
    return posición

def verificar_estado_del_juego(posición: int) -> bool:
    if posición == 0:
        print("\nCaíste en lo más profundo de la torre y te devoraron las serpientes. ¡Perdiste!")
        terminar = True
    elif posición == 30:
        print("\nLograste escalar hacia la cima de la torre y sobrevivir. ¡Ganaste!")
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
    print(f"\n¡Gracias por jugar, {nombre}! Llegaste a la casilla {posición}")
    
tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
posición_actual = 15