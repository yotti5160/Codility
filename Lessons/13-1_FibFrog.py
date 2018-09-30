def solution(A):
    l=len(A)
    fib=[1,2]
    while fib[-1]<=l:
        fib.append(fib[-1]+fib[-2])
    canGo={i for i in range(l) if A[i]}
    canGo.add(l)
    step, on=0, {-1}
    while True:
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
        on=nextOn
    return -1
