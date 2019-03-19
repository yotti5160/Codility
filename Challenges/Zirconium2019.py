def solution(A, B, F):
    l, c=len(A), []
    for i in range(l):
        c.append([A[i], B[i], A[i]-B[i]])
    c.sort(key=lambda x:x[2], reverse=True)
    ret=0
    for i in range(F):
        ret+=c[i][0]
    for i in range(F, l):
        ret+=c[i][1]
    return ret
