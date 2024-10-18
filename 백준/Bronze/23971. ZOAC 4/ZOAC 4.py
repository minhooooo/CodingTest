h,w,n,m=map(int,input().strip().split())
h_count=1
h_temp=1
while(h_temp<h):
    h_temp=h_temp+n+1
    if h_temp<=h:
        h_count+=1
w_count=1
w_temp=1
while(w_temp<w):
    w_temp=w_temp+m+1
    if w_temp<=w:
        w_count+=1

print(h_count*w_count)