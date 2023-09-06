print("Ingresa tu Nombre: ")
nombre = input()
print(f"Hola {nombre} Bienvenido al juego")



from readchar import readkey, key
print(f"Ingresaste a un bucle {nombre}")

while True:
    res = readkey()
    print(f"{nombre} Para salir presiona  ↑  ")
    if res == key.UP:
        print("Saliste del Bucle")
        break