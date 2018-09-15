def solution(H):
    hi=[]
    count=0
    for h in H:
        if not hi:
            hi.append(h)
            count+=1
        else:
            while hi and hi[-1]>h:
                hi.pop()
            if hi and hi[-1]==h:
                pass
            else:
                hi.append(h)
                count+=1
    return count
