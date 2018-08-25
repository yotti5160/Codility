#This is a codility challenge, and I got gold award.
#Here is the link to my award page:
#https://app.codility.com/cert/view/certMS4YQA-ZE3FTH4ST49YCHMY/

def solution(N, M, X, Y):
    K=len(X)
    if K&1==1:
        return 0
    targetSum=K//2
    def check(size,array):
        book=[0]*size
        for a in array:
            book[a]+=1
        left, right, tmpSum=None, None, 0
        for i in range(size):
            tmpSum+=book[i]
            if tmpSum==targetSum and left==None:
                left=i
                right=i
            elif tmpSum==targetSum:
                right=i
            elif tmpSum>targetSum:
                break
        if left!=None and right!=None:
            return right-left+1
        return 0
    return check(N, X)+check(M, Y)
