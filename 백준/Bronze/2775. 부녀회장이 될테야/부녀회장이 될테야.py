count=int(input())
for i in range(count):
    k=int(input())
    n=int(input())
    temp = [[0] * n for _ in range(k + 1)]
    if k>=1:
        for j in range(n):
            temp[0][j]=j+1
    for row in range(1,k+1):
        for col in range(n):
            sums=0
            for j in range(col+1):
                sums=sums+temp[row-1][j]
            temp[row][col]=sums
    print(temp[k][n-1])