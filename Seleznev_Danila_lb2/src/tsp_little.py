INF = float('inf')

def copy_matrix(matrix):
    return [row[:] for row in matrix]

def reduce_matrix(matrix):
    size = len(matrix)
    cost = 0

    for i in range(size):
        row_min = min(matrix[i])
        if row_min != INF and row_min > 0:
            cost += row_min
            for j in range(size):
                if matrix[i][j] != INF:
                    matrix[i][j] -= row_min

    for j in range(size):
        col_min = INF
        for i in range(size):
            if matrix[i][j] < col_min:
                col_min = matrix[i][j]

        if col_min != INF and col_min > 0:
            cost += col_min
            for i in range(size):
                if matrix[i][j] != INF:
                    matrix[i][j] -= col_min

    return cost

def find_best_zero(matrix):
    size = len(matrix)

    best_penalty = -1
    best_pos = None

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                row_min = INF
                for k in range(size):
                    if k != j and matrix[i][k] < row_min:
                        row_min = matrix[i][k]

                col_min = INF
                for k in range(size):
                    if k != i and matrix[k][j] < col_min:
                        col_min = matrix[k][j]

                penalty = row_min + col_min

                if penalty > best_penalty:
                    best_penalty = penalty
                    best_pos = (i, j)

    return best_pos, best_penalty

def find_chain_endpoints(edges, u, v):
    next_map = {}
    prev_map = {}

    for a, b in edges:
        next_map[a] = b
        prev_map[b] = a

    next_map[u] = v
    prev_map[v] = u

    start = u
    while start in prev_map:
        start = prev_map[start]

    end = v
    while end in next_map:
        end = next_map[end]

    return start, end

def creates_small_cycle(edges, u, v, total_n):
    next_map = {}

    for a, b in edges:
        next_map[a] = b

    next_map[u] = v

    cur = v
    length = 1

    while cur in next_map:
        cur = next_map[cur]
        length += 1

        if cur == u:
            return length < total_n

    return False

def remove_row_col(matrix, rows, cols, row_idx, col_idx):
    new_matrix = []
    
    for i in range(len(matrix)):
        if i != row_idx:
            new_row = []
            for j in range(len(matrix)):
                if j != col_idx:
                    new_row.append(matrix[i][j])
            new_matrix.append(new_row)
    
    new_rows = [rows[i] for i in range(len(rows)) if i != row_idx]
    new_cols = [cols[j] for j in range(len(cols)) if j != col_idx]
    
    return new_matrix, new_rows, new_cols

def forbid_edge(matrix, rows, cols, from_city, to_city):
    row_idx = -1
    col_idx = -1
    
    for i in range(len(rows)):
        if rows[i] == from_city:
            row_idx = i
            break
    
    for j in range(len(cols)):
        if cols[j] == to_city:
            col_idx = j
            break
    
    if row_idx != -1 and col_idx != -1:
        matrix[row_idx][col_idx] = INF

def reconstruct_path(edges, n):
    next_map = {}

    for u, v in edges:
        next_map[u] = v

    path = [0]
    cur = 0

    for _ in range(n - 1):
        cur = next_map[cur]
        path.append(cur)

    return path

def calculate_cost(path, original):
    total = 0
    n = len(path)

    for i in range(n):
        total += original[path[i]][path[(i + 1) % n]]

    return total

def little_algorithm(matrix):
    n = len(matrix)

    original = copy_matrix(matrix)

    reduced = copy_matrix(matrix)
    initial_bound = reduce_matrix(reduced)

    rows = list(range(n))
    cols = list(range(n))

    best_cost = INF
    best_path = None

    def little_recursive(matrix, rows, cols, edges, bound):
        nonlocal best_cost, best_path
        
        total_n = len(original)

        if bound >= best_cost:
            return

        if len(matrix) == 1:
            u = rows[0]
            v = cols[0]

            final_edges = edges + [(u, v)]

            path = reconstruct_path(final_edges, total_n)
            total_cost = calculate_cost(path, original)

            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path

            return

        result = find_best_zero(matrix)

        if result[0] is None:
            return

        (i, j), penalty = result

        u = rows[i]
        v = cols[j]

        force_left = penalty >= INF / 2

        if not force_left:
            right_matrix = copy_matrix(matrix)
            right_matrix[i][j] = INF

            right_bound = bound + reduce_matrix(right_matrix)

            little_recursive(
                right_matrix,
                rows,
                cols,
                edges,
                right_bound
            )

        if not creates_small_cycle(edges, u, v, total_n):
            left_matrix = copy_matrix(matrix)

            start, end = find_chain_endpoints(edges, u, v)

            left_matrix, left_rows, left_cols = remove_row_col(
                left_matrix, rows, cols, i, j
            )

            forbid_edge(left_matrix, left_rows, left_cols, end, start)

            left_bound = bound + reduce_matrix(left_matrix)

            little_recursive(
                left_matrix,
                left_rows,
                left_cols,
                edges + [(u, v)],
                left_bound
            )

    little_recursive(reduced, rows, cols, [], initial_bound)

    return best_path, float(best_cost)

def main():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        row = [INF if x == -1 else x for x in row]
        matrix.append(row)

    path, cost = little_algorithm(matrix)

    print(*path)
    print(cost)

if __name__ == "__main__":
    main()