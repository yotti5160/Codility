def solution(words):
    book=[[0,0,0,0,-1,-1] for _ in range(26)]
    pure=[0]*26
    for i, word in enumerate(words):
        l=len(word)
        if len(set(word))==1:
            pure[ord(word[0])-97]+=l
        else:
            headL, tailL=1, 1
            for i in range(1, l):
                if word[i]==word[0]:
                    headL+=1
                else:
                    break
            for i in range(l-2, -1, -1):
                if word[i]==word[-1]:
                    tailL+=1
                else:
                    break
            #head1, head2, tail1, tail2, indexHead, indexTail
            firstIndex, lastIndex=ord(word[0])-97, ord(word[-1])-97
            if headL>book[firstIndex][0]:
                book[firstIndex][1]=book[firstIndex][0]
                book[firstIndex][0]=headL
                book[firstIndex][4]=i
            elif headL>book[firstIndex][1]:
                book[firstIndex][1]=headL
            if tailL>book[lastIndex][2]:
                book[lastIndex][3]=book[lastIndex][2]
                book[lastIndex][2]=tailL
                book[lastIndex][5]=i
            elif tailL>book[lastIndex][3]:
                book[lastIndex][3]=tailL
    ret=0
    for i in range(26):
        tmp=pure[i]
        if book[i][4]!=book[i][5]:
            tmp+=book[i][0]+book[i][2]
        else:
            tmp+=max(book[i][0]+book[i][3], book[i][1]+book[i][2])
        ret=max(ret, tmp)
    for word in words:
        if len(word)<=ret:
            continue
        letter, l, nowl=word[0], 1, 1
        for i in range(1, len(word)):
            if word[i]==letter:
                l+=1
            else:
                letter=word[i]
                nowl=max(nowl, l)
                l=1
        ret=max(ret, nowl)
    return ret
