from collections import deque

def solution(begin, target, words):
    lenth=len(begin)
    q=deque()
    q.append([begin,0])
    while(q):
        temp=q.popleft()
        if temp[0]==target:
            return temp[1]
        if temp[1]>len(words):
            return 0
        for i in words:
            status=0
            for k in range(lenth):
                if i[k]!=temp[0][k]:
                    status+=1
            if status==1:
                q.append([i,temp[1]+1])
    return 0