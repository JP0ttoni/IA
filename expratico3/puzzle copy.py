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

method = input("Escolha o método de resolução (BFS, DFS ou IDFS): ").strip().lower()
# Solicita ao usuário o estado inicial do quebra-cabeça
start_state = input("Digite o estado inicial do quebra-cabeça (9 dígitos de 0 a 8 sem repetição): ")

# Validação do estado inicial
if len(start_state) != 9 or not all(char.isdigit() and char in '012345678' for char in start_state):
    print("Entrada inválida. Certifique-se de inserir exatamente 9 dígitos de 0 a 8 sem repetição.")
else:
    # Estado final padrão
    goal_state = '123456780'

    # Método de resolução escolhido pelo usuário

    if method == 'bfs':
        solution = bfs(start_state, goal_state)
    elif method == 'dfs':
        solution = dfs(start_state, goal_state)
    elif method == 'idfs':
        solution = idfs(start_state, goal_state)
    else:
        print("Método de resolução inválido. Escolha entre BFS, DFS ou IDFS.")

    if solution:
        print("\nSolução encontrada com {}:".format(method.upper()))
        for step, (direction, state) in enumerate(solution):
            print("\nPasso", step + 1, "- Movimento:", direction)
            print_board(state)
    else:
        print("Não há solução para este quebra-cabeça.")
