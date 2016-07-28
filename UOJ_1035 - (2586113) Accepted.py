line=input().split(" ")
w,x,y,z=line
a=int(w)
b=int(x)
c=int(y)
d=int(z)
if((b>c) & (d>a) & ((c+d)>(a+b)) & (c>=0) & (d>=0) & (a%2==0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
1