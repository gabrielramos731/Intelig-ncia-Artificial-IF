def minimax(state):
    if final(state):
        return custo(state)

    if is_maximizing_player(state):
        best_value = -1000
        best_action = None
        for action in acoes(state):
            new_state = resultado(state, action)
            value = min_valor(new_state)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    else:
        best_value = 1000
        best_action = None
        for action in acoes(state):
            new_state = resultado(state, action)
            value = max_valor(new_state)
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

def max_valor(state):
    if final(state):
        return custo(state)

    best_value = float('-inf')
    for action in acoes(state):
        new_state = resultado(state, action)
        value = min_valor(new_state)
        best_value = max(best_value, value)
    return best_value

def min_valor(state):
    if final(state):
        return custo(state)

    best_value = float('inf')
    for action in acoes(state):
        new_state = resultado(state, action)
        value = max_valor(new_state)
        best_value = min(best_value, value)
    return best_value

def final(state):
    # Check if the state is a terminal state
    # Return True or False
    if ganhador(state) or is_board_full(state):
        return True
    return False

def custo(state):
    # custo the state and return a score
    if ganhador(state) == 'X':
        return 1
    elif ganhador(state) == 'O':
        return -1
    else:
        return 0

def is_maximizing_player(state):
    # Check if it's the turn of the maximizing player
    # Return True or False
    if state.count('X') == state.count('O'):
        return False
    return True

def acoes(state):
    # Get a list of possible actions from the current state
    # Return a list of actions
    actions = []
    for i in range(len(state)):
        if state[i] == ' ':
            actions.append(i)
    return actions

def resultado(state, action):
    # Make a move in the current state based on the given action
    # Return the new state
    new_state = list(state)
    new_state[action] = 'X' if is_maximizing_player(state) else 'O'
    return ''.join(new_state)

def ganhador(state):
    # Check if there is a winner in the current state
    # Return 'X' if X wins, 'O' if O wins, or None if there is no winner
    winning_combinations = [
        [0, 1, 2, 3, 4], [5,6,7,8,9], [10,11,12,13,14], [15,16,17,18,19], [20,21,22,23,24],  # linhas
        [0, 5,10,15,20], [1,6,11,16,21], [2,6,12,17,22], [3,7,13,18,23], [4,8,14,19,24], # Colunas
        [0,6,12,18,24], [4,8,12,16,20]  # Diagonais
    ]
    for combination in winning_combinations:
        if state[combination[0]] == state[combination[1]] == state[combination[2]] == state[combination[3]] == state[combination[4]] != ' ':
            return state[combination[0]]
    return None

def is_board_full(state):
    # Check if the board is full
    # Return True or False
    return True if ' ' not in state else False

def imprime_estado(state):
    for idx, elemento in enumerate(state):
        print(f'| { elemento } |', end='') if elemento != ' ' else print(f'| - |', end='')
        if((idx+1) % 5 == 0):
            print('\n')


# estado_ini = [' ',' ',' ',' ',' ',
#               ' ',' ',' ',' ',' ',
#               ' ',' ',' ',' ',' ',
#               ' ',' ',' ',' ',' ',
#               ' ',' ',' ',' ',' ']

estado_ini = ['X','O','O',' ','X',
              ' ','X',' ','O',' ',
              'O','O','X','O','X',
              ' ',' ','X',' ','O',
              'X','O','X',' ',' ']

# Teste minimax (esta fazendo jogadas não otimizadas)
imprime_estado(estado_ini)
print(final(estado_ini))
while(not final(estado_ini)):
    pos = int(input("Escolha uma posição para 'O': "))-1
    estado_ini[pos] = 'O'
    imprime_estado(estado_ini)
    if(final(estado_ini)):
        break
    estado_ini[minimax(estado_ini)] = 'X'
    imprime_estado(estado_ini)
    if(final(estado_ini)):
        break
