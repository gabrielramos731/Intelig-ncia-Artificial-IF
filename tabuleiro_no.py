import numpy as np
import time

def casos(estado):
    '''Recebe um estado do tabuleiro e retorna as possíveis jogadas'''
    
    idx_min = np.unravel_index(estado.argmin(), estado.shape)  # índice bi-dim do menor valor '0'
    movs = list(((idx_min[0], idx_min[1]-1),  
                 (idx_min[0], idx_min[1]+1),
                 (idx_min[0]-1, idx_min[1]),
                 (idx_min[0]+1, idx_min[1])))  # lista de possíveis posições de troca
    return [tuple([idx_min, mov]) for mov in movs if (mov[0] in range(3) and mov[1] in range(3))]

def resultado(estado, acao):
    '''Gera um novo estado com base em um estado passado e uma acao'''

    global const_total
    const_total += 1;
    estado_tmp = estado.copy()
    estado_tmp[acao[0]], estado_tmp[acao[1]] = estado_tmp[acao[1]], estado_tmp[acao[0]]  # swap de valores
    return estado_tmp

def conta_caminho(no):
    '''Conta o número de ações até o menor caminho'''

    cont = 0
    no_pai = no.pai
    while(no_pai != None):
        no_pai = no_pai.pai
        cont += 1
    return cont

class No:
    def __init__(self, estado: np.array, pai: 'No'):
        self.estado = estado
        self.pai = pai
        self.acoes = casos(estado)

inicio = time.time()

no_inicial = No(estado = np.array([[7,2,4],[5,0,6],[8,3,1]]), 
                pai = None)
estado_alvo = np.array([[1,2,3],[4,5,6],[7,8,0]])
nos_validos = [no_inicial]  # armazena todos nós validos
estados_visitados = set((np.array2string(no_inicial.estado)))  # armazena os estados já visitados

res = False
cont = 0
const_total = 0
while(res == False):
    no_atual = nos_validos[cont]
    for acao_no_atual_aux in no_atual.acoes:  # varre ações de um estado
        estado_atual_aux = resultado(no_atual.estado, acao_no_atual_aux)
        if(np.array2string(estado_atual_aux) in estados_visitados):  # verifica se o novo no já foi gerado anteriormente
            continue  
        novo_no = No(estado_atual_aux, no_atual)
        nos_validos.append(novo_no)  # adiciona "no" na lista
        estados_visitados.add(np.array2string(novo_no.estado))
        if(np.array_equal(estado_alvo, novo_no.estado)):  # verifica se encontrou alvo
            print(f"{estado_atual_aux} RESPOSTA")
            print(f"{conta_caminho(novo_no)} Passos")
            res = True
            break
    cont += 1

fim = time.time()
print(f"{const_total} Acoes testadas")
print(f"{fim - inicio:.3f} Tempo decorrido")
