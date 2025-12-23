import random


movimientos = ["piedra", "papel", "tijera"]
reglas = {
    "piedra" : "tijera",
    "tijera" : "papel",
    "papel"  : "piedra"
}

puntos_usuario = 0
puntos_ia = 0
PUNTOS_PARA_GANAR = 3   


def obtener_movimiento_ia():
    return random.choice(movimientos)


def obtener_movimiento_usuario():
    movimiento = str(input("Introduce tu movimiento: PIEDRA - PAPEL - TIJERA: "))
    if movimiento.lower() not in movimientos:
        print("Movimiento invalid, elige una opcion correcta")
        return None
    return movimiento


def mostar_marcador(p_usuario, p_ia):
    print(f"Marcador: Tu: {p_usuario} - Computadora: {p_ia}")
    print("--------------------------------------")


def anunciar_ganador(p_usuario, p_ia):
    if p_usuario > p_ia:
        print("Felicidades has ganado")
        print(f"Tus puntos: {p_usuario}")
        print(f"Puntos de la computadora: {p_ia}")
    else:
        print("Has perdido")
        print(f"Tus puntos: {p_usuario}")
        print(f"Puntos de la computadora: {p_ia}")

while puntos_usuario < PUNTOS_PARA_GANAR and puntos_ia < PUNTOS_PARA_GANAR:
    
    movimiento_ia = obtener_movimiento_ia()
    
    movimiento_usuario = obtener_movimiento_usuario()
    if movimiento_usuario is None:
        continue
    
    
    print(f"Elegiste: {movimiento_usuario}")
    print(f"El ordenador eligio: {movimiento_ia}")

    if movimiento_usuario == movimiento_ia:
        print("Empate")
    elif reglas[movimiento_usuario] == movimiento_ia:
        print("Has ganado")
        puntos_usuario += 1
    else:
        print("Has perdido")
        puntos_ia += 1
            
    mostar_marcador(puntos_usuario, puntos_ia)
    
anunciar_ganador(puntos_usuario, puntos_ia)
    