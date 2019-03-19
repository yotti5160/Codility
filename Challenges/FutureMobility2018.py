def solution(A, B):
    
    def go(arr):
        check=0
        for i in range(l):
            if check+arr[i]>0:
                tmp=check+arr[i]
                if i+1<l and arr[i+1]<0:
                    if tmp>=-arr[i+1]:
                        solution.count+=(-arr[i+1])
                        arr[i]+=arr[i+1]
                        tmp+=arr[i+1]
                        arr[i+1]=0
                    else:
                        solution.count+=tmp
                        arr[i]-=tmp
                        arr[i+1]+=tmp
                        tmp=0
                if i+2<l and tmp>0:
                    arr[i+2]+=tmp
                    solution.count+=tmp
                    arr[i]-=tmp
                check=0
            else:
                check+=arr[i]
        return arr
    
    arr=[A[i]-B[i] for i in range(len(A))]
    if sum(arr)!=0:
        return -1
    solution.count, l=0, len(arr)
    retArr=go(arr)
    go(retArr[::-1])
    
    return solution.count%1000000007
