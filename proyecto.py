import random

jugadorGana = 0
computadorGana = 0
#Definicion de opciones del juego

while jugadorGana < 3 and computadorGana < 3:
    print("-----------------------------------------------")
    options = ("piedra", "papel", "tijeras")
    print("OPCIONES")
    print(f"1. {options[0]}")
    print(f"2. {options[1]}")
    print(f"3. {options[2]}")
    print("***")
    print(f"Puntaje jugador {jugadorGana}")
    print(f"Puntaje computador {computadorGana}")

    # se le pide la opcion al usuario
    number = int(input("Ingrese su opción => "))
    user_option = options[number-1]
    print(f"Usted sacó {user_option}")

    # se genera la opcion del computador
    num = int(random.random() * 10) % 3
    computer_option = options[num]

    print(f"El compujtador sacó {computer_option}")

    # se evalua el ganador
    if user_option == computer_option:
        print("Es un empate")
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print("El jugador gana")
            jugadorGana += 1
        else :
            print("El computador gana")
            computadorGana += 1
    elif user_option == 'piedra':
        if computer_option == 'tijeras':
            print("El jugador gana")
            jugadorGana += 1
        else :
            print("El computador gana")
            computadorGana += 1
    elif user_option == 'tijeras':
        if computer_option == 'papel':
            print("El jugador gana")
            jugadorGana += 1
        else :
            print("El computador gana")
            computadorGana += 1

print("FIN DEL JUEGO")
if(jugadorGana == 3):
    print("El jugador ganó")
else:
    print("El computador ganó")
