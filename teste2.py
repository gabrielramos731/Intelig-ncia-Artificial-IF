from math import inf as infinity
import numpy as np
import random

def copia_matriz(estado):  # OK testada
    return [linha[:] for linha in estado]

def jogador(no):  # OK testada
    if no.pai == None:
        return -1 if sum([sum(line) for line in no.estado]) == 1 else 1
    else:
        return -1 * no.pai.player

def acoes(estado):  # OK testada
    indices = []
    for i, linha in enumerate(estado):
        for j, elemento in enumerate(linha):
            if elemento == 0:
                indices.append((i, j))
    return indices

def resultado(no, acao):  # OK testada
    linha, coluna = acao
    estado_aux = copia_matriz(no.estado)
    estado_aux[linha][coluna] = no.player
    return No(estado_aux, no.pai)

def ganhador(no):  # OK testada
    for linha in no.estado:  # verifica linhas
        if sum(linha) == 3:
            no.utilidade = 1
            return 1
        elif sum(linha) == -3:
            no.utilidade = -1
            return -1
    
        for j in range(3):  # verifica colunas
            soma_coluna = 0
            for i in range(3):
                soma_coluna += no.estado[i][j]  # Some o elemento atual da coluna à soma da coluna
            if soma_coluna == 3:
                no.utilidade = 1
                return 1
            elif soma_coluna == -3:
                no.utilidade = -1
                return -1
            
        diagonal_principal = 0
        diagonal_secundaria = 0
        for i in range(3):  # verifica diag. pricipal
            diagonal_principal += no.estado[i][i]
        if diagonal_principal == 3:
            no.utilidade = 1
            return 1
        if diagonal_principal == -3:
            no.utilidade = -1
            return -1
            
        for i in range(3):  # verifica diag. secundária
            diagonal_secundaria += no.estado[i][3 - 1 - i]
        if diagonal_secundaria == 3:
            no.utilidade = 1
            return 1
        if diagonal_secundaria == -3:
            no.utilidade = -1
            return -1
    no.utilidade = 0
    return 0  # não acabou ou empate

def final(no):  # OK
    if(ganhador(no) == 1 or ganhador(no) == -1):
        return True
    cont = 0
    if(ganhador(no) == 0):
        for linha in no.estado:
            cont += linha.count(0)
        return True if cont == 0 else False

def custo(no):  # OK (já tinha feito como ganhador)
    return ganhador(no)

def utility(no):
    """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
    return no.utilidade if no.player == 1 else -no.utilidade

def minimax(no):
    print(no.acoes)
    print(max(no.acoes, key=lambda a: min_value(resultado(no, a))))
    return max(no.acoes, key=lambda a: min_value(resultado(no, a)))

def max_value(no):
    if no.terminal:
        return ganhador(no)
    v = -np.inf
    for a in no.acoes:
        v = max(v, min_value(resultado(no, a)))
    return v

def min_value(no):
    if no.terminal:
        return ganhador(no)
    v = np.inf
    for a in no.acoes:
        v = min(v, max_value(resultado(no, a)))
    return v

def imprime_estado(no):
    for linha in no.estado:
        print(linha)

# 1 = x | -1 = o | 0 = vazio
class No:
    def __init__(self, estado: list, pai: 'No'):
        self.estado = estado
        self.pai = pai
        self.player = jogador(self)
        self.acoes = acoes(estado)
        self.terminal = final(self)
        self.utilidade = ganhador(self)  # OK


# ini_l = random.randint(0, 2)
# ini_c = random.randint(0, 2)
estado_ini = [[0,1,1],
              [0,0,0],
              [0,0,0]]
# estado_ini[ini_l][ini_c] =  1
no_inicial = No(estado_ini, None)



# no_aux = no_inicial
# no_aux = No(resultado(no_aux, minimax(no_aux)).estado, no_inicial)  # jogada minimax
# imprime_estado(no_aux)
# terminal = False
# while(terminal == False):
#     print("Escolha uma posicao para -1")
#     entrada = input()
#     l, c = entrada.split()
#     no_aux = No(resultado(no_aux, (int(l),int(c))).estado, no_aux)
#     imprime_estado(no_aux)
#     no_aux = No(resultado(no_aux, minimax(no_aux)).estado, no_aux)  # jogada minimax
#     print("Jogada minimax")
#     imprime_estado(no_aux)
#     terminal = no_aux.terminal
