import sys

INF = float('inf')

def read_input():
    lines = sys.stdin.read().strip().split('\n')
    start_vertex = int(lines[0])
    
    matrix = []
    for i in range(1, len(lines)):
        row = []
        for value in map(float, lines[i].split()):
            if value < 0:
                row.append(INF)
            else:
                row.append(value)
        matrix.append(row)
    
    return start_vertex, matrix

def prim_mst(matrix, n):
    visited = [False] * n
    mst = [[] for _ in range(n)]

    min_edge = [(None, INF)] * n

    min_edge[0] = (None, 0)
    
    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v][1] < min_edge[u][1]):
                u = v
        
        if min_edge[u][1] == INF:
            break
        
        visited[u] = True

        if min_edge[u][0] is not None:
            parent = min_edge[u][0]
            weight = min_edge[u][1]
            mst[parent].append((u, weight))
            mst[u].append((parent, weight))

        for v in range(n):
            if not visited[v] and matrix[u][v] < min_edge[v][1]:
                min_edge[v] = (u, matrix[u][v])
    
    return mst

def dfs_preorder(mst, start, n):
    visited = [False] * n
    path = []
    
    def dfs(v: int):
        visited[v] = True
        path.append(v)

        neighbors = sorted(mst[v], key=lambda x: (x[1], x[0]))
        
        for neighbor, weight in neighbors:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start)
    return path

def calculate_path_length(path, matrix):
    total = 0.0
    for i in range(len(path) - 1):
        total += matrix[path[i]][path[i + 1]]
    return total

def tsp_2approximation(start_vertex, matrix):
    n = len(matrix)

    mst = prim_mst(matrix, n)
    
    path = dfs_preorder(mst, start_vertex, n)
    
    path.append(start_vertex)
    
    length = calculate_path_length(path, matrix)
    
    return length, path

def main():
    start_vertex, matrix = read_input()
    length, path = tsp_2approximation(start_vertex, matrix)
    
    print(f"{length:.2f}")
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()
