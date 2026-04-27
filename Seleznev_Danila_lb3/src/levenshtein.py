def levenshtein_distance(S, T):
    n = len(S)
    m = len(T)
    
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        curr[0] = i
        char_a = S[i - 1]
        
        for j in range(1, m + 1):
            char_b = T[j - 1]
            
            if char_a == char_b:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j - 1], curr[j - 1], prev[j])
        
        prev, curr = curr, prev
    
    return prev[m]

if __name__ == "__main__":
    S = input()
    T = input()
    
    print(levenshtein_distance(S, T))
