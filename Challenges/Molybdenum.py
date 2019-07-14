def solution(K, M, A):
    N = len(A)
    ret = set()
    count = [0]*(M+2)
    for i in range(K):
        A[i] += 1
    for a in A:
        count[a] += 1
    for i in range(1, M+2):
        if count[i] > N//2:
            ret.add(i)
            break
    for i in range(0, N-K):
        count[A[i]] -= 1
        A[i] -= 1
        count[A[i]] += 1
        
        count[A[i+K]] -= 1
        A[i+K] += 1
        count[A[i+K]] += 1
        
        if count[A[i]] > N//2:
            ret.add(A[i])
        if count[A[i+K]] > N//2:
            ret.add(A[i+K])
    ret = list(ret)
    return sorted(ret)
