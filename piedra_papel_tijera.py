import random


movimientos = ["piedra", "papel", "tijera"]

movimiento_ia = random.choice(movimientos)
movimiento_usuario = str(input("Introduce tu movimiento: PIEDRA - PAPEL - TIJERA: "))


if movimiento_usuario.lower() not in movimientos:
    print("El movimientos no está permitido")

print(f"Elegiste: {movimiento_usuario}")
print(f"El ordenador eligio: {movimiento_ia}")

if movimiento_usuario.lower() == "piedra":
    if movimiento_ia == "piedra":
        print("Empate")
    elif movimiento_ia == "papel":
        print("Has perdido")
    elif movimiento_ia == "tijera":
        print("Has ganado")
elif movimiento_usuario.lower() == "papel":
    if movimiento_ia == "piedra":
        print("Has ganado")
    elif movimiento_ia == "papel":
        print("Empate")
    elif movimiento_ia == "tijera":
        print("Has perdido")
elif movimiento_usuario.lower() == "tijera":
    if movimiento_ia == "piedra":
        print("Has perdido")
    elif movimiento_ia == "papel":
        print("Has ganado")
    elif movimiento_ia == "tijera":
        print("Empate")