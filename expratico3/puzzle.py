from collections import deque
import time
import psutil

# Representação do estado do tabuleiro como uma string
# Exemplo: '123456780' representa o tabuleiro
# 1 2 3
# 4 5 6
# 7 8 0

dire = []
start_time = time.time()
# Função para encontrar os movimentos possíveis
def get_neighbors(state):
    moves = []
    i = state.index('0')
    if i % 3 > 0:  # Pode mover para a esquerda
        moves.append(('left', state[:i - 1] + '0' + state[i - 1] + state[i + 1:]))
    if i % 3 < 2:  # Pode mover para a direita
        moves.append(('right', state[:i] + state[i + 1] + '0' + state[i + 2:]))
    if i // 3 > 0:  # Pode mover para cima
        moves.append(('up', state[:i - 3] + '0' + state[i - 2:i] + state[i - 3] + state[i + 1:]))
    if i // 3 < 2:  # Pode mover para baixo
        moves.append(('down', state[:i] + state[i + 3] + state[i + 1:i + 3] + '0' + state[i + 4:]))
    return moves

# Algoritmo de busca em largura (BFS)
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        for direction, neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [(direction, neighbor)]))

    return None

# Algoritmo de busca em profundidade (DFS)
def dfs(start, goal):
    visited = set()
    stack = [(start, [])]

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        visited.add(state)
        for direction, neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [(direction, neighbor)]))

    return None

# Algoritmo de busca em profundidade iterativa (IDFS)
def idfs(start, goal):
    depth = 0
    while True:
        result = dfs_recursive_limit(start, goal, depth)
        if result:
            return result
        depth += 1

# Função auxiliar para busca em profundidade iterativa
def dfs_recursive_limit(state, goal, depth_limit, path=[]):
    if state == goal:
        return path
    if depth_limit == 0:
        return None
    for direction, neighbor in get_neighbors(state):
        if neighbor not in path:
            result = dfs_recursive_limit(neighbor, goal, depth_limit - 1, path + [(direction, neighbor)])
            if result:
                return result
    return None

# Função para imprimir o tabuleiro formatado
def print_board(state):
    for i in range(0, 9, 3):
        print(' '.join(state[i:i+3]))

input_solve = input("")
# Estado inicial e meta
lista = input_solve.split() 
input_string = lista[1]
start_state = input_string.replace(",", "")

goal_state = '123456780'

print("Estado Inicial:")
print_board(start_state)
print("\nEstado Final:")
print_board(goal_state)


# Resolvendo o quebra-cabeça com BFS
if(lista[0] == 'bfs'):
    solution_bfs = bfs(start_state, goal_state)
    #print("\nSolução encontrada com BFS:")
    if solution_bfs:
        for step, (direction, state) in enumerate(solution_bfs):
            dire.append(direction)
            print("step", step + 1)
    else:
        print("Não há solução para este quebra-cabeça.")

# Resolvendo o quebra-cabeça com DFS
if(lista[0] == 'dfs'):
    solution_dfs = dfs(start_state, goal_state)
    #print("\nSolução encontrada com DFS:")
    if solution_dfs:
        for step, (direction, state) in enumerate(solution_dfs):
            print(", ", direction)
            #print_board(state)
    else:
        print("Não há solução para este quebra-cabeça.")

# Resolvendo o quebra-cabeça com IDFS
if(lista[0] == 'idfs'):
    solution_idfs = idfs(start_state, goal_state)
    #print("\nSolução encontrada com IDFS:")
    if solution_idfs:
        for step, (direction, state) in enumerate(solution_idfs):
            dire.append(direction)
            print("step", step)
            #print_board(state)
    else:
        print("Não há solução para este quebra-cabeça.")

for i in range(step + 1):
    
    if i == 0:
        print('path_to_goal: [', end='')
    if i == len(dire) - 1:
        print("'", dire[i], "']")
    else:
        print("'", dire[i], "', ", end='')

print('cost_of path: ', step + 1)

end_time = time.time()
execution_time = end_time - start_time
print("running_time: ", execution_time)

used_ram = psutil.virtual_memory().used
print('max_ram_usage: ', used_ram)

