from collections import deque

def solution(n, computers):
    answer = 0
    q=deque()
    visit=[0 for i in range(n)]
    while(1):
        status=0
        for i in range(n):
            if visit[i]==0:
                q.append(i)
                status=1
                answer+=1
                break
        if status==0:
            return answer
        while(q):
            temp=q.popleft()
            if visit[temp]==1:
                continue
            else:
                visit[temp]=1
            for j in range(0,n):
                if computers[temp][j]==1 and visit[j]==0:
                    q.append(j)
