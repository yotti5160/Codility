# Award link: https://app.codility.com/cert/view/cert646E5S-D4UKRMYFRHPH26Q2/

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
        xc, yc=min(x[0], x[1]), min(y[0], y[1])
        if xc<=yc:
            return x
        return y
    def trans(n):
        if n==0:
            return [0,0,1]
        r2, r5=0,0
        while n%5==0:
            r5+=1
            n=n//5
        while n%2==0:
            r2+=1
            n=n//2
        return [r2, r5, 0]
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
    if containZero(A):
        for i in range(l):
            for j in range(l):
                A[i][j]=trans2(A[i][j])
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
        if min(dp[-1][-1][0], dp[-1][-1][1])==0:
            return 0
        return 1
    # if A does't contain 0
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
    return min(dp[-1][-1][0], dp[-1][-1][1])
