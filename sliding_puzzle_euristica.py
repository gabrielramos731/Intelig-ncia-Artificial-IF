import numpy as np
import time
from queue import PriorityQueue

def casos(estado):
    '''Recebe um estado do tabuleiro e retorna as possíveis jogadas'''
    
    idx_min = np.unravel_index(estado.argmin(), estado.shape)  # índice bi-dim do menor valor '0'
    movs = list(((idx_min[0], idx_min[1]-1),  
                 (idx_min[0], idx_min[1]+1),
                 (idx_min[0]-1, idx_min[1]),
                 (idx_min[0]+1, idx_min[1])))  # lista de possíveis posições de troca
    return [tuple([idx_min, mov]) for mov in movs if (mov[0] in range(3) and mov[1] in range(3))]

def novo_estado(estado, acao):
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

def expande(no_pai):
    '''Expande um no gerando nós resultantes'''

    return [No(novo_estado(no_pai.estado, acao), no_pai) for acao in no_pai.acoes]
      
def calcula_custo(estado):
    '''
    Calcula o custo de um estado com base na distância de cada elemento
    com o elemento de sua respectiva posição na matriz alvo
    '''

    estado_alvo = np.array([[1,2,3],[4,5,6],[7,8,0]])
    return np.sum(np.abs(np.subtract(estado, estado_alvo)))

class No:
    def __init__(self, estado: np.array, pai: 'No'):
        self.estado = estado
        self.pai = pai
        self.acoes = casos(estado)
        self.custo = calcula_custo(estado)

inicio = time.time()

no_inicial = No(estado = np.array([[7,2,4],[5,0,6],[8,3,1]]), pai = None)
estado_alvo = np.array([[1,2,3],[4,5,6],[7,8,0]])
estados_visitados = set((np.array2string(no_inicial.estado)))  # armazena os estados já visitados
fronteira = PriorityQueue()  # armazena todos nós a serem explorados em fila de prioridade
fronteira.put((no_inicial.custo, 0, no_inicial))

res = False
prior_aux = 0
const_total = 0
while(res == False and ~fronteira.empty()):
    _, _, no_atual = fronteira.get(block=False)  # recebe o estado de maior prioridade (menor custo)
    if(np.array_equal(estado_alvo, no_atual.estado)):  # verifica se no_atual == no_alvo
        print(f"{no_atual.estado} RESPOSTA")
        print(f"{conta_caminho(no_atual)} Passos")
        res = True
    for novo_no in expande(no_atual):  # percorre nós gerados
        if(np.array2string(novo_no.estado) in estados_visitados):  # verifica se o novo no já foi gerado anteriormente
            continue  
        prior_aux += 1  # critério de desempate de prioridade
        fronteira.put((novo_no.custo, prior_aux, novo_no))  # adiciona "no" na fila | prior_aux faz pegar o primeiro nó de menor prioridade adicionado em caso de empate, se multiplicado por -1, passa a pegar o último
        estados_visitados.add(np.array2string(novo_no.estado))
    
fim = time.time()
print(f"{const_total} Acoes testadas")
print(f"{fim - inicio:.3f}s Tempo decorrido")
