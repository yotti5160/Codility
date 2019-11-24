from collections import defaultdict as dfd 
def solution(A, K):
    l = len(A)
    book = dfd(int)
    book[A[0]] += 1
    big = 1
    left, right = 0, 0
    while right < l-1:
        right += 1
        book[A[right]] += 1
        big = max(big, book[A[right]])
        if right-left+1-big > K: # overstride
            book[A[left]] -= 1
            left += 1
    return right - left + 1
