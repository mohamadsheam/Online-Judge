a=[]
s=0
for i in range(0,5):
    n=int(input())
    a.append(n)
    if(a[i]%2==0):
        s+=1
print("%d valores pares" %s)
1