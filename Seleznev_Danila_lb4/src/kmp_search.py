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

def kmp_search(pattern, text):
    if not pattern or not text:
        return []
    
    m = len(pattern)
    n = len(text)

    pi = compute_prefix_function(pattern)
    
    matches = []
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]
    
    return matches

if __name__ == "__main__":
    pattern = input().strip()
    text = input().strip()

    matches = kmp_search(pattern, text)

    if matches:
        print(','.join(map(str, matches)))
    else:
        print(-1)
