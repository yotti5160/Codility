#From http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/

def solution(A):
    book = []
    for i,a in enumerate(A):
        book.append((i-a, 1))
        book.append((i+a, -1))
    
    book.sort(key=lambda x: (x[0], -x[1]))
 
    intersections, active_circles = 0, 0
 
    for _, isLeft in book:
        if isLeft==1:
            intersections += active_circles
        active_circles += isLeft
        if intersections > 10E6:
            return -1
 
    return intersections
