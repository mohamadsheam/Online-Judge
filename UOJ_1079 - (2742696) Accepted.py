n=int(input())
for i in range(0,n):
    
    line=input().split(" ")
    x,y,z=line
    a=float(x)
    b=float(y)
    c=float(z)
    s=a*2+b*3+c*5
    d=2.0+3.0+5.0
    f=float(s/d)
    print("%.1f"%f)
1