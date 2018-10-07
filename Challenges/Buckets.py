# Award link: https://app.codility.com/cert/view/cert4URQR8-RBY9NCWXXFUPUCK6/

import collections
def solution(N, Q, B, C):
    l=len(B)
    book=collections.defaultdict(int)
    for i in range(l):
        book[(B[i], C[i])]+=1
        if book[(B[i], C[i])]==Q:
            return i
    return -1
