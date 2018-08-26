def solution(N, A):
    r=[0]*N
    nowFloor, nowMax=0, 0
    for a in A:
        if a==N+1:
            nowFloor=nowMax
        else:
            r[a-1]=max(nowFloor+1, r[a-1]+1)
            if r[a-1]>nowMax:
                nowMax=r[a-1]
    for i in range(N):
        if r[i]<nowFloor:
            r[i]=nowFloor
    return r
