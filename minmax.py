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
    return 0

def final(no):
    if(ganhador(no) == 1 or ganhador(no) == -1):
        return True
    try:
        [linha.index(0) for linha in no.estado]
    except:
        pass
    return False

# 1 = x | -1 = o | 0 = vazio
class No:
    def __init__(self, estado: list, pai: 'No'):
        self.estado = estado
        self.pai = pai
        self.player = jogador(self)
        self.acoes = acoes(estado)
        self.terminal: final(self)  # resolver isso

list.index
estado_ini = [[1,0,-1],[0,-1,0],[-1,0,1]]

no_inicial = No(estado_ini, None)  # p 1
no = No([[1,-1,1],[-1,1,0],[0,0,0]], no_inicial)

# print(no_inicial.estado)
# print(resultado(no_inicial, (0,0)).estado)
# print(no_inicial.estado)

# [print(aux.estado) for aux in expande_no(no_inicial)]
print(final(no_inicial))
