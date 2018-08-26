#It is suffice to check slices of length two or three.
#Since a longer slice with minimal average can be split into slices of length two or three,
#smaller slices will have the same average as the bigger slice. 
def solution(A):
    startTwo=-1
    two=float('inf')
    for i in range(0,len(A)-1):
        tmp=sum(A[i:i+2])
        if tmp<two:
            two=tmp
            startTwo=i
    two/=2
    startThree=-1
    three=float('inf')
    for i in range(0,len(A)-2):
        tmp=sum(A[i:i+3])
        if tmp<three:
            three=tmp
            startThree=i
    three/=3
    if two<=three:
        return startTwo
    return startThree
