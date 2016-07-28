t=int(input())
a=[]
n=0
out=0
for i in range(0,t):
    k=int(input())
    a.append(k)
for i in range(0,t):
    if((a[i]>=10) & (a[i]<=20) ):
        n+=1
    else:
        out+=1
print("%d in" %n)
print("%d out" %out)
1