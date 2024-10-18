def solution(routes):
    camera=[]
    routes.sort(key=lambda x:(x[1]))
    lenth=len(routes)
    camera.append(routes[0][1])
    answer=1
    for i in range(1,lenth):
        if camera[-1]<routes[i][0]:
            camera.append(routes[i][1])
            answer+=1
    return answer