def solution(m, n, puddles):
    answer = 0
    count=[[1]*(m+1) for i in range(n+1)]
    for i,j in puddles:
        count[j][i]=0
        if i==1:
            for k in range(j,n+1):
                count[k][1]=0
        if j==1:
            for k in range(i,m+1):
                count[1][k]=0
    for i in range(2,n+1):
        for j in range(2,m+1):
            if count[i][j]==0:
                continue
            else: count[i][j]=(count[i][j-1]+count[i-1][j])%1000000007
    return count[-1][-1]%1000000007