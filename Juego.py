from Funciones import *

TABLERO = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
posición_actual = 15
jugar = True
estado_juego = "inicio"
continuar = True
pregunta_actual = None
respuesta_actual = None

while jugar:
    try:
        if estado_juego == "inicio":
            jugar = validar_continuación("¡Bienvenido a Serpientes y Escaleras! ¿Querés comenzar el juego? (S/N)", "Cerrando el juego...")
            estado_juego = "nombre"
        elif estado_juego == "nombre":
            nombre_jugador = input("\nIngresá tu nombre para continuar.\n\n")
            estado_juego = "jugando"
        elif estado_juego == "jugando":
            if continuar:
                if pregunta_actual is None:
                    pregunta_actual = generar_pregunta_aleatoria(preguntas)
                    if not pregunta_actual:
                        estado_juego = "fin del juego"
                else:
                    if respuesta_actual is None:
                        respuesta_actual = escribir_respuesta()
                        movimiento = verificar_respuesta(respuesta_actual, pregunta_actual)
                        posición_actual = realizar_movimiento(movimiento, TABLERO, posición_actual)
                    if verificar_estado_del_juego(posición_actual):
                        if posición_actual == 0:
                            print("\nCaíste en lo más profundo de la torre y te devoraron las serpientes. ¡Perdiste!\n")
                        else:
                            print("\nLograste escalar hacia la cima de la torre y sobrevivir. ¡Ganaste!\n")
                        estado_juego = "fin del juego"
                    else:
                        continuar = validar_continuación()
                        if not continuar:
                            estado_juego = "fin del juego"
                        else:
                            pregunta_actual = None
                            respuesta_actual = None
        elif estado_juego == "fin del juego":
            crear_tablero_puntuación(nombre_jugador, posición_actual)
            jugar = False
    except ValueError:
        print("\nEl valor ingresado es incorrecto. Volvé a ingresar el valor solicitado.")