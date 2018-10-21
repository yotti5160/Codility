# Award link: https://app.codility.com/cert/view/certGU5JT9-7C8B9BP3PX4J7GWE/

def solution(A):
    def containZero(A):
        for i in range(l):
            for j in range(l):
                if A[i][j]==0:
                    return True
        return False
    def vecPlus(x, y):
        return [x[0]+y[0], x[1]+y[1]]
    def small(x, y):
        if min(x[0], x[1])<=min(y[0], y[1]):
            return x
        return y
    def trans(n):
        r2, r5=0,0
        while n%5==0:
            r5+=1
            n=n//5
        while n%2==0:
            r2+=1
            n=n//2
        return [r2, r5]
    def trans2(n):
        if n==0:
            return [float('inf'), float('inf')]
        r2, r5=0,0
        while n%5==0:
            r5+=1
            n=n//5
        while n%2==0:
            r2+=1
            n=n//2
        return [r2, r5]
    l=len(A)
    contZero=containZero(A)
    if contZero:
        for i in range(l):
            for j in range(l):
                A[i][j]=trans2(A[i][j])
    else:
        for i in range(l):
            for j in range(l):
                A[i][j]=trans(A[i][j])
    dp=[[0]*l for _ in range(l)]
    tmp=[0,0]
    for i in range(l):
        tmp=vecPlus(tmp, A[0][i])
        dp[0][i]=tmp
    tmp=[0,0]
    for i in range(l):
        tmp=vecPlus(tmp, A[i][0])
        dp[i][0]=tmp
    for i in range(1,l):
        for j in range(1,l):
            dp[i][j]=small(vecPlus(dp[i-1][j], A[i][j]), vecPlus(dp[i][j-1], A[i][j]))
    if contZero:
        return min(1, dp[-1][-1][0], dp[-1][-1][1])
    return min(dp[-1][-1][0], dp[-1][-1][1])
