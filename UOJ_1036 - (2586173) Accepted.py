import math
line=input().split(" ")
w,x,y=line
a=float(w)
b=float(x)
c=float(y)
s=float(b*b-4*a*c)

if((a>0) & (s>0)):
    r1=(-b+math.sqrt(s))/(2*a)
    r2=(-b-math.sqrt(s))/(2*a)
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)
else:
   print("Impossivel calcular")
1