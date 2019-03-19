def solution(S):
    def check(headList, tailList, sign, index, nowLength, headSet, tailSet):
        if nowLength>600000 or (sign==1 and (headList[-1], index) in headSet) or (sign==-1 and (tailList[-1], index) in tailSet):
            return None
        if sign==1:
            tmpWord=headList[-1][index:]
            ltmp=len(tmpWord)
            for s in S:
                s, ls=s[::-1], len(s)
                if tmpWord==s:
                    return ' '.join(headList)+' '+' '.join(tailList+[s])[::-1]
                elif ltmp>ls and tmpWord[:ls]==s:
                    end=tmpWord[ls:]
                    # if what left is a palindrome
                    if end==end[::-1]:
                        return ' '.join(headList)+' '+' '.join(tailList+[s])[::-1]
                    result=check(headList, tailList+[s], 1, index+ls, nowLength+ls, headSet|{(headList[-1], index)}, tailSet)
                    if result: return result
                elif ltmp<ls and tmpWord==s[:ltmp]:
                    end=s[ltmp:]
                    # if what left is a palindrome
                    if end==end[::-1]:
                        return ' '.join(headList)+' '+' '.join(tailList+[s])[::-1]
                    result=check(headList, tailList+[s], -1, ltmp, nowLength+ls, headSet|{(headList[-1], index)}, tailSet)
                    if result: return result
        else:
            tmpWord=tailList[-1][index:]
            ltmp=len(tmpWord)
            for s in S:
                ls=len(s)
                if tmpWord==s:
                    return ' '.join(headList+[s])+' '+' '.join(tailList)[::-1]
                elif ls<ltmp and s==tmpWord[:ls]:
                    end=tmpWord[ls:]
                    # if what left is a palindrome
                    if end==end[::-1]:
                        return ' '.join(headList+[s])+' '+' '.join(tailList)[::-1]
                    result=check(headList+[s], tailList, -1, index+ls, nowLength+ls, headSet, tailSet|{(tailList[-1], index)})
                    if result: return result
                elif ls>ltmp and s[:ltmp]==tmpWord:
                    end=s[ltmp:]
                    # if what left is a palindrome
                    if end==end[::-1]:
                        return ' '.join(headList+[s])+' '+' '.join(tailList)[::-1]
                    result=check(headList+[s], tailList, 1, ltmp, nowLength+ls, headSet, tailSet|{(tailList[-1], index)})
                    if result: return result
        return None
    def run(head, revTail):
        lh, lrt=len(head), len(revTail)
        if head==revTail:
            return head+' '+revTail[::-1]
        elif lh>lrt and revTail==head[:lrt]:
            result=check([head], [revTail], 1, lrt, lh+lrt, set(), set())
            if result: return result
        elif lh<lrt and head==revTail[:lh]:
            result=check([head], [revTail], -1, lh, lh+lrt, set(), set())
            if result: return result
        return None
    S=S.split()
    # check if any word is palindromic
    for s in S:
        if s==s[::-1]:
            return s
    # check composites
    l=len(S)
    for i in range(l):
        for j in range(l):
            result=run(S[i], S[j][::-1])
            if result: return result
    return 'NO'
