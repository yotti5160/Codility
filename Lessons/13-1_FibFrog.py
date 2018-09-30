def solution(A):
    l=len(A)
    fib=[1,1]
    while fib[-1]<=l:
        fib.append(fib[-1]+fib[-2])
    fib=set(fib)
    canGo={l}
    for i in range(l):
        if A[i]:
            canGo.add(i)
    step, on=0, {-1}
    while canGo:
        step+=1
        nextOn=set()
        for nowPoint in on:
            for f in fib:
                if nowPoint+f in canGo:
                    nextOn.add(nowPoint+f)
        if not nextOn:
            return -1
        if l in nextOn:
            return step
        canGo=canGo-nextOn
        on=nextOn
    return -1
