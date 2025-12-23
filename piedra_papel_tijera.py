import random


movimientos = ["piedra", "papel", "tijera"]
reglas = {
    "piedra" : "tijera",
    "tijera" : "papel",
    "papel"  : "piedra"
}

puntos_usuario = 0
puntos_ia = 0

while puntos_usuario < 3 and puntos_ia < 3:
    
    movimiento_ia = random.choice(movimientos)
    movimiento_usuario = str(input("Introduce tu movimiento: PIEDRA - PAPEL - TIJERA: "))
    
    if movimiento_usuario.lower() not in movimientos:
        print("El movimientos no está permitido")
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
            
    print(f"Marcador: Tu: {puntos_usuario} - Computadora: {puntos_ia}")
    print("--------------------------------------")
    
if puntos_usuario > puntos_ia:
    print("Felicidades has ganado")
    print(f"Tus puntos: {puntos_usuario}")
    print(f"Puntos de la computadora: {puntos_ia}")
else:
    print("Has perdido")
    print(f"Puntos de la computadora: {puntos_ia}")
    print(f"Tus puntos: {puntos_usuario}")
    