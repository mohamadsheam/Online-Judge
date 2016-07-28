line=input().split(" ")
x1,x2=line
a=int(x1)
n=int(x2)
if(a==1):
    p=float(4.00*n)
    print("Total: R$ %.2f"%p)
elif(a==2):
    p=float(4.50*n)
    print("Total: R$ %.2f"%p)
elif(a==3):
    p=float(5.00*n)
    print("Total: R$ %.2f"%p)
elif(a==4):
    p=float(2.00*n)
    print("Total: R$ %.2f"%p)
elif(a==5):
    p=float(1.50*n)
    print("Total: R$ %.2f"%p)
1