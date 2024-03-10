def copia_matriz(estado):  # OK
    return [linha[:] for linha in estado]

def jogador(no):  # OK
    if no.pai == None:
        return -1 if sum([sum(line) for line in no.estado]) == 1 else 1
    else:
        return -1 * no.pai.player

def acoes(estado):  # OK
    indices = []
    for i, linha in enumerate(estado):
        for j, elemento in enumerate(linha):
            if elemento == 0:
                indices.append((i, j))
    return indices

def resultado(no, acao):  # OK
    linha, coluna = acao
    estado_aux = copia_matriz(no.estado)
    estado_aux[linha][coluna] = no.player
    return No(estado_aux, no.pai)

def expande_no(no):  # OK
    nos_gerados = list()
    for acao in no.acoes:
        nos_gerados.append(resultado(no, acao))
    return nos_gerados

def ganhador(no):  # OK
    for linha in no.estado:  # verifica linhas
        if sum(linha) == 3:
            return 1
        elif sum(linha) == -3:
            return -1
    
        for j in range(3):  # verifica colunas
            soma_coluna = 0
            for i in range(3):
                soma_coluna += no.estado[i][j]  # Some o elemento atual da coluna à soma da coluna
            if soma_coluna == 3:
                return 1
            elif soma_coluna == -3:
                return -1
            
        diagonal_principal = 0
        diagonal_secundaria = 0
        for i in range(3):  # verifica diag. pricipal
            diagonal_principal += no.estado[i][i]
        for i in range(3):  # verifica diag. secundária
            diagonal_secundaria += no.estado[i][3 - 1 - i]
        if diagonal_principal == 3:
            return 1
        elif diagonal_secundaria == -3:
            return -1
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

def minimax(no):
    no.utilidade, acao = max_valor(no)
    return acao

def max_valor(no):
    if(no.terminal):
        return custo(no), None
    v = -2  # valor ref. para máximo
    for a in no.acoes:
        v2, a2 = min_valor(resultado(no, a))
        if(v2 > v):
            v, mov = v2, a
    return v, mov

def min_valor(no):
    if(no.terminal):
        return custo(no), None
    v = 2  # valor ref. para mínimo
    for a in no.acoes:
        v2, a2 = max_valor(resultado(no, a))
        if(v2 < v):
            v, mov = v2, a
    return v, mov


# 1 = x | -1 = o | 0 = vazio
class No:
    def __init__(self, estado: list, pai: 'No'):
        self.estado = estado
        self.pai = pai
        self.player = jogador(self)
        self.acoes = acoes(estado)
        self.terminal = final(self)
        self.utilidade = int

estado_ini = [[0,0,0],[0,1,0],[0,0,0]]

no_inicial = No(estado_ini, None)  # p 1
no = No([[1,-1,1],[-1,1,0],[0,0,0]], no_inicial)

# [print(aux.estado) for aux in expande_no(no_inicial)]
# print(final(no_inicial))

print(minimax(no_inicial))
