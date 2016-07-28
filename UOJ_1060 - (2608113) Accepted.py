a=[]
s=0
for i in range(0,6):
    n=float(input())
    a.append(n)
    if(a[i]>0):
        s+=1
print("%d valores positivos" %s)
1