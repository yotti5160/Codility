def solution(S, P, Q):
    l=len(S)
    book=[[0]*4 for i in range(l)]
    score={'A':0, 'C':1, 'G':2, 'T':3}
    nowCount=[0,0,0,0]
    for i in range(l):
        nowCount[score[S[i]]]+=1
        for j in range(4):
            book[i][j]=nowCount[j]
    ret=[]
    for i in range(len(P)):
        if P[i]==0:
            for j in range(4):
                if book[Q[i]][j]>0:
                    ret.append(j+1)
                    break
        else:
            for j in range(4):
                if book[Q[i]][j]-book[P[i]-1][j]>0:
                    ret.append(j+1)
                    break
    return ret
