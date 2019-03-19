def solution(A):
    def vecPlus(x, y):
        return [x[0]+y[0], x[1]+y[1]]
    def trans(n):
        if n==0:
            return [float('inf'), float('inf')]
        r2, r5=0,0
        while n&1==0:
            r2+=1
            n=n>>1
        while n%5==0:
            r5+=1
            n=n//5
        return [r2, r5]
    l=len(A)
    contZero=False
    for i in range(l):
        for j in range(l):
            if A[i][j]==0:
                contZero=True
            A[i][j]=trans(A[i][j])
    dp=[[0]*l for _ in range(l)]
    tmp1, tmp2=[0,0], [0,0]
    for i in range(l):
        tmp1, tmp2=vecPlus(tmp1, A[0][i]), vecPlus(tmp2, A[i][0])
        dp[0][i], dp[i][0]=tmp1, tmp2
    for i in range(1,l):
        for j in range(1,l):
            vec1, vec2=vecPlus(dp[i-1][j], A[i][j]), vecPlus(dp[i][j-1], A[i][j])
            dp[i][j]=[min(vec1[0], vec2[0]), min(vec1[1], vec2[1])]
    if contZero:
        return min(1, dp[-1][-1][0], dp[-1][-1][1])
    return min(dp[-1][-1][0], dp[-1][-1][1])
