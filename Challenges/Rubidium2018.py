def solution(x, y):
    tmpX, tmpY=[], []
    for i in range(len(x)):
        tmpX.append((x[i], y[i]))
        tmpY.append((x[i], y[i]))
    tmpX.sort(key=lambda x:(x[0], x[1]))
    tmpY.sort(key=lambda x:(x[1], x[0]))
    def dist(p1, p2):
        return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
    def brute(x):
        l, ret=len(x), float('inf')
        for i in range(l):
            for j in range(i+1, l):
                ret=min(ret, dist(x[i], x[j]))
        return ret
    def run(x, y):
        l=len(x)
        firstPartLen=l//2
        if l<=3:
            return brute(x)
        x1, x2=x[:firstPartLen], x[firstPartLen:]
        x1Set=set(x1)
        y1, y2=[], []
        for point in y:
            if point in x1Set:
                y1.append(point)
            else:
                y2.append(point)
        d1=run(x1, y1)
        d2=run(x2, y2)
        d=min(d1, d2)
        strip=[]
        midX=x[firstPartLen][0]
        lower, upper=midX-d, midX+d
        for tmpY in y:
            if lower<=tmpY[0]<=upper:
                strip.append(tmpY)
        ls, d3=len(strip), float('inf')
        for i in range(ls):
            for j in range(1, 6):
                if i+j<ls:
                    d3=min(d3, dist(strip[i], strip[i+j]))
        return min(d, d3)
    return run(tmpX, tmpY)//2
