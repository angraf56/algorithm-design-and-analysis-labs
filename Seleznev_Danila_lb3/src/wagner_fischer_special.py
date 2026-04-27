def wagner_fischer_special(A, B, replace_cost, insert_cost, delete_cost,
                          special_replace_char, special_replace_cost,
                          special_delete_char, special_delete_cost):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if A[i - 1] == special_delete_char:
            dp[i][0] = dp[i - 1][0] + special_delete_cost
        else:
            dp[i][0] = dp[i - 1][0] + delete_cost

    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + insert_cost

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if B[j - 1] == special_replace_char:
                    current_replace_cost = special_replace_cost
                else:
                    current_replace_cost = replace_cost

                if A[i - 1] == special_delete_char:
                    current_delete_cost = special_delete_cost
                else:
                    current_delete_cost = delete_cost

                dp[i][j] = min(
                    dp[i - 1][j - 1] + current_replace_cost,
                    dp[i][j - 1] + insert_cost,
                    dp[i - 1][j] + current_delete_cost
                )
    
    return dp[n][m]

if __name__ == "__main__":
    costs = list(map(int, input().split()))
    replace_cost = costs[0]
    insert_cost = costs[1]
    delete_cost = costs[2]

    A = input().strip()
    B = input().strip()

    special_replace_char, special_replace_cost = input().split()
    special_replace_cost = int(special_replace_cost)

    special_delete_char, special_delete_cost = input().split()
    special_delete_cost = int(special_delete_cost)

    result = wagner_fischer_special(
        A, B,
        replace_cost, insert_cost, delete_cost,
        special_replace_char, special_replace_cost,
        special_delete_char, special_delete_cost
    )
    
    print(result)
