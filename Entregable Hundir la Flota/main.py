import random

eslora = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
tab_jug = [[" "] * 10 for i in range(10)]
tab_compu = [[" "] * 10 for i in range(10)]
tab_tiro_jug = [[" "] * 10 for i in range(10)]
tab_tiro_compu = [[" "] * 10 for i in range(10)]
letras_a_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

def imprimir_tablero(tablero):
    print("  " + " ".join(letras_a_num))
    print("  +" + "-+" * 10)
    num_fila = 1
    for fila in tablero:
        print(f"{num_fila}|{'|'.join(fila)}|")
        num_fila += 1

def colocar_barcos(tablero): #Para colocar los barcos de manera aleatoria y asegurar que no se superpongan
    for longitud in eslora:
        while True:
            orientacion, fila, columna = random.choice(["H", "V"]), random.randint(0, 9), random.randint(0, 9)
            if comprobar_barcos(longitud, fila, columna, orientacion):
                if not sobrebarco(tablero, fila, columna, orientacion, longitud):
                    if orientacion == "H":
                        for i in range(columna, columna + longitud):
                            tablero[fila][i] = "X"
                    else:
                        for i in range(fila, fila + longitud):
                            tablero[i][columna] = "X"
                    break

def comprobar_barcos(longitud, fila, columna, orientacion): #Para comprobar que efectivamente el barco sea cual sea el tamaño cabe por posición y orientación en el tablero.
    if orientacion == "H":
        return columna + longitud <= 10
    else:
        return fila + longitud <= 10

def sobrebarco(tablero, fila, columna, orientacion, longitud): #Para asegurar de que los barcos creados no se superponen según la posición y orientación.
    if orientacion == "H":
        for i in range(columna, columna + longitud):
            if tablero[fila][i] == "X":
                return True
    else:
        for i in range(fila, fila + longitud):
            if tablero[i][columna] == "X":
                return True
    return False

def disparar():
    while True:
        fila = input("Introduzca a qué fila quiere disparar: ")
        if fila.isdigit() and 1 <= int(fila) <= 10:
            fila = int(fila) - 1
            break
    while True:
        columna = input("Introduzca a qué columna quiere disparar (A-J): ").upper()
        if columna in letras_a_num:
            columna = letras_a_num[columna]
            break
    return fila, columna

def game(): #Esta ya llama al juego, hace que se pongan los tableros, lleva cuenta de los barcos que quedan y si quedan, sigue funcionando. Comprueba si toca o agua y actualiza el tablero.
    colocar_barcos(tab_jug)
    colocar_barcos(tab_compu)
    barcos_restantes = len(eslora)
   
    while barcos_restantes > 0:
        imprimir_tablero(tab_tiro_jug)
        fila, columna = disparar()

        if tab_compu[fila][columna] == "X":
            print("¡Tocado!")
            tab_tiro_jug[fila][columna] = "X"
            tab_compu[fila][columna] = " "
            barcos_restantes -= 1
        else:
            print("¡Agua!")
            tab_tiro_jug[fila][columna] = "-"

game()