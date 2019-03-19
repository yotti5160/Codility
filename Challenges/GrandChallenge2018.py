import collections
def solution(S):
    # help function    
    def longTwo(S):
        ls=len(S)
        char, tmp=S[0], 0
        index=[0]*(ls+1)
        for i in range(ls):
            if S[i]==char:
                tmp+=1
            else:
                tmp-=1
            index[i+1]=tmp
        left, right, ret=collections.defaultdict(), collections.defaultdict(),0
        for i in range(ls+1):
            right[index[i]]=i
        for i in range(ls,-1,-1):
            left[index[i]]=i
        for i in left:
            ret=max(ret, right[i]-left[i])
        return ret
    l=len(S)
    front, end, ret=0,0,0
    contain, book=set(), collections.defaultdict(int)
    while front<l:
        #need to call longTwo
        if len(contain)==2 and (S[front] not in contain):
            if front-end>ret+1: #S[end:front]
                ret=max(ret, longTwo(S[end:front]))
            contain.add(S[front])
            book[S[front]]+=1
            front+=1
        elif len(contain)<=2:
            contain.add(S[front])
            book[S[front]]+=1
            front+=1
        else:
            book[S[end]]-=1
            if book[S[end]]==0:
                contain.remove(S[end])
            end+=1
            if len(contain)==2 and front-end>ret+1:
                ret=max(ret, longTwo(S[end:front]))
    if len(contain)==2 and front-end>ret+1:
        ret=max(ret, longTwo(S[end:front]))            
    while end<l:
        book[S[end]]-=1
        if book[S[end]]==0:
            contain.remove(S[end])
        end+=1
        if len(contain)==2 and front-end>ret+1:
            ret=max(ret, longTwo(S[end:front]))
    
    return ret
