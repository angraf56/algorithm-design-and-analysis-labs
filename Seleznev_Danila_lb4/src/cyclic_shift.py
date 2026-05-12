def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    
    for i in range(1, m):
        j = pi[i - 1]
        
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        pi[i] = j
    
    return pi

def kmp_search_cyclic(A, B):
    m = len(B)
    n = len(A)

    pi = compute_prefix_function(B)
    j = 0

    for i in range(2 * n):
        current_char = A[i % n]

        while j > 0 and current_char != B[j]:
            j = pi[j - 1]
        
        if current_char == B[j]:
            j += 1

        if j == m:
            return i - m + 1

    return -1

def find_cyclic_shift(A, B):
    if len(A) != len(B):
        return -1

    if len(A) == 0:
        return 0

    index = kmp_search_cyclic(A, B)
    
    return index

if __name__ == "__main__":
    A = input().strip()
    B = input().strip()

    result = find_cyclic_shift(A, B)
    print(result)
