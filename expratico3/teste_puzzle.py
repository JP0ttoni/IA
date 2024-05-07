from collections import deque

# Representação do estado do tabuleiro como uma string
# Exemplo: '123456780' representa o tabuleiro
# 1 2 3
# 4 5 6
# 7 8 0

# Função para encontrar os movimentos possíveis
def get_neighbors(state):
    moves = []
    i = state.index('0')
    if i % 3 > 0:  # Pode mover para a esquerda
        moves.append(state[:i - 1] + '0' + state[i - 1] + state[i + 1:])
    if i % 3 < 2:  # Pode mover para a direita
        moves.append(state[:i] + state[i + 1] + '0' + state[i + 2:])
    if i // 3 > 0:  # Pode mover para cima
        moves.append(state[:i - 3] + '0' + state[i - 2:i] + state[i - 3] + state[i + 1:])
    if i // 3 < 2:  # Pode mover para baixo
        moves.append(state[:i] + state[i + 3] + state[i + 1:i + 3] + '0' + state[i + 4:])
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
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

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
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

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
    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = dfs_recursive_limit(neighbor, goal, depth_limit - 1, path + [neighbor])
            if result:
                return result
    return None

# Função para imprimir o tabuleiro formatado
def print_board(state):
    for i in range(0, 9, 3):
        print(' '.join(state[i:i+3]))

# Estado inicial e meta
start_state = '123456708'
goal_state = '123456780'

print("Estado Inicial:")
print_board(start_state)
print("\nEstado Final:")
print_board(goal_state)

# Resolvendo o quebra-cabeça com BFS
solution_bfs = bfs(start_state, goal_state)
print("\nSolução encontrada com BFS:")
if solution_bfs:
    for step, state in enumerate(solution_bfs):
        print("\nPasso", step + 1)
        #print_board(state)
else:
    print("Não há solução para este quebra-cabeça.")

# Resolvendo o quebra-cabeça com DFS
solution_dfs = dfs(start_state, goal_state)
print("\nSolução encontrada com DFS:")
if solution_dfs:
    for step, state in enumerate(solution_dfs):
        print("\nPasso", step + 1)
        #print_board(state)
else:
    print("Não há solução para este quebra-cabeça.")

# Resolvendo o quebra-cabeça com IDFS
solution_idfs = idfs(start_state, goal_state)
print("\nSolução encontrada com IDFS:")
if solution_idfs:
    for step, state in enumerate(solution_idfs):
        print("\nPasso", step + 1)
        #print_board(state)
else:
    print("Não há solução para este quebra-cabeça.")
