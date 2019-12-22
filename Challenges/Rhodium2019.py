from collections import defaultdict
def solution(T):
    l = len(T)
    result = 0
    for i in range(l-1):
        bad = defaultdict(int)
        count = 1
        if T[i] != i:
            bad[T[i]] = 1
        
        for j in range(i+1, l):
            if j in bad:
                count -= bad.pop(j)
            if not i <= T[j] <= j:
                bad[T[j]] += 1
                count += 1 
            elif T[j] == j:
                count += 1
            
            if count <= 1:
                result += 1
    return result + l
