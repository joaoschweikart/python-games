import os
import random

jogarNovamente = "s"
jogadas = 0
jogador = 1  # 1 = JOGADOR, 2 = CPU
vitoria = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def screen():
    global velha
    global jogadas
    os.system("cls")
    print("   0   1   2")
    print("0  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("  -----------")
    print("1  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("  -----------")
    print("2  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("")
    print("Boa sorte! Você é o jogador X!")
    print("")


def playerPlay():
    global jogadas
    global jogador
    if jogador == 1 and jogadas < 9:
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        try:
            while velha[linha][coluna] != " ":
                print('O campo selecionado já foi marcado! Tente novamente.')
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
            velha[linha][coluna] = "X"
            jogador = 2
            jogadas += 1
        except:
            print('Linha e/ou coluna inválida! Tente novamente.')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))


def cpuPlay():
    global jogadas
    global jogador
    if jogador == 2 and jogadas < 9:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)
        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        velha[linha][coluna] = "O"
        jogador = 1
        jogadas += 1


def verifyVictory():
    global velha
    global vitoria
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # verificar linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria == s:
            break
        # verificar colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if vitoria == s:
            break
        # verificar diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria == s
            break
        if vitoria == s:
            break
        # verificar diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria == s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global jogador
    global vitoria
    jogadas = 0
    jogador = 1  # 1 = JOGADOR, 2 = CPU
    vitoria = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogarNovamente == "s":
    while True:
        screen()
        playerPlay()
        screen()
        vitoria = verifyVictory()
        if vitoria != "n" or jogadas == 9:
            break
        cpuPlay()
        screen()
        vitoria = verifyVictory()
        if vitoria != "n" or jogadas == 9:
            break
    if vitoria == "X" or vitoria == "O":
        print(f'FIM DE JOGO! O GANHADOR FOI O JOGADOR {vitoria}!')
    else:
        print('FIM DE JOGO! EMPATE!')
    jogarNovamente = str(input('Você deseja jogar novamente? [s/n]: '))
    redefinir()
