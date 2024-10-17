def solution(triangle):
    for i in range (1,len(triangle)):
        for k in range (len(triangle[i])):
            if k==len(triangle[i])-1:
                triangle[i][k]+=triangle[i-1][k-1]
            elif k==0:
                triangle[i][k]+=triangle[i-1][k]
            else:
                triangle[i][k]+=max(triangle[i-1][k-1],triangle[i-1][k])
    return max(triangle[-1])