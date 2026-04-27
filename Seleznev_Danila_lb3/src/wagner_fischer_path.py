def wagner_fischer_with_path(replace_cost, insert_cost, delete_cost, A, B):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i * delete_cost
    
    for j in range(m + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + replace_cost,
                    dp[i][j - 1] + insert_cost,
                    dp[i - 1][j] + delete_cost
                )

    operations = []
    i, j = n, m
    
    while i > 0 or j > 0:
        if i == 0:
            operations.append('I')
            j -= 1
        elif j == 0:
            operations.append('D')
            i -= 1
        elif A[i - 1] == B[j - 1]:
            operations.append('M')
            i -= 1
            j -= 1
        else:
            replace_val = dp[i - 1][j - 1] + replace_cost
            insert_val = dp[i][j - 1] + insert_cost
            delete_val = dp[i - 1][j] + delete_cost
            
            min_val = min(replace_val, insert_val, delete_val)
            
            if min_val == insert_val:
                operations.append('I')
                j -= 1
            elif min_val == delete_val:
                operations.append('D')
                i -= 1
            else:
                operations.append('R')
                i -= 1
                j -= 1

    operations = operations[::-1]
    
    return ''.join(operations)

if __name__ == "__main__":
    costs = list(map(int, input().split()))
    replace_cost = costs[0]
    insert_cost = costs[1]
    delete_cost = costs[2]
    
    A = input().strip()
    B = input().strip()

    path = wagner_fischer_with_path(replace_cost, insert_cost, delete_cost, A, B)
    print(path)
    print(A)
    print(B)
