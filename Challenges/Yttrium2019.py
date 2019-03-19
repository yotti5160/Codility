def solution(S, K):
    def check(A):
        return 26-A.count(0)
    A=[0]*26
    for s in S:
        A[ord(s)-97]+=1
    tmp=check(A)
    if tmp<K: return -1
    if tmp==K: return 0
    l=len(S)
    result, head, tail=l, -1, -1
    while head<l:
        tmp=check(A)
        if tmp>K:
            head+=1
            if head==l: return result
            A[ord(S[head])-97]-=1
        elif tmp==K:
            result=min(result, head-tail)
            tail+=1
            A[ord(S[tail])-97]+=1
    return result
