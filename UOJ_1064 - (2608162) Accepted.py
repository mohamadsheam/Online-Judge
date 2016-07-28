a=[]
s=0
f=0
for i in range(0,6):
    n=float(input())
    a.append(n)
    if(a[i]>=0):
        s+=1
        f=float(f+a[i])
g=float(f/s)
print("%d valores positivos" %s)
print("%.1f"%g)
1