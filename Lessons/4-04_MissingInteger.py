def solution(A):
    book=[0]*(len(A)+1)
    for a in A:
        if 0<a<=len(A):
            book[a]+=1
    for i in range(1,len(book)):
        if book[i]==0:
            return i
    return len(A)+1
