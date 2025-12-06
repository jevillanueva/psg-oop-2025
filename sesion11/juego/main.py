from clases import Jugador, Computadora
from logica import Juego


print("🎮 Bienvenido al juego de Piedra, Papel o Tijera")
nombre = input("Introduce tu nombre: ")
jugador = Jugador(nombre)
computadora = Computadora()
juego = Juego(jugador, computadora)

while True:
    print("\n--- Menú ---")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        juego.jugar()
    elif opcion == "2":
        print("¡Gracias por jugar! 👋")
        break
    else:
        print("Opción inválida, intenta de nuevo.")