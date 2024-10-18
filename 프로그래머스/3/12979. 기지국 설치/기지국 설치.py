import math
def solution(n, stations, w):
    answer = 0
    width=w*2+1
    if stations[0]-w>1:
        answer+=math.ceil((stations[0]-w-1)/width)
        print("start")
    for i in range(1,len(stations)):
        if stations[i]-w-stations[i-1]-w>1:
            answer+=math.ceil((stations[i]-w-stations[i-1]-w-1)/width)
            print("a")
    if stations[-1]+w<n:
        answer+=math.ceil((n-stations[-1]-w)/width)
        print("b")

    return answer