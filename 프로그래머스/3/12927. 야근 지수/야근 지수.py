import heapq

def solution(n, works):
    answer = 0
    sums=0
    hp=[]
    for i in (works):
        heapq.heappush(hp,(-1)*i)
        sums+=i
    if sums-n<=0:
        return 0
    for i in range(n):
        temp=heapq.heappop(hp)
        temp+=1
        if temp<0:
            heapq.heappush(hp,temp)
    for i in hp:
        answer+=(i)**2
    return answer