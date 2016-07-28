n=float(input())

if((n>0) & (n<=400)):
    p=float(n*.15)
    s=n+p
    print("Novo salario: %.2f"%s)
    print("Reajuste ganho: %.2f"%p)
    print("Em percentual: 15 %")
elif((n>400) & (n<=800)):
    p=float(n*.12)
    s=n+p
    print("Novo salario: %.2f"%s)
    print("Reajuste ganho: %.2f"%p)
    print("Em percentual: 12 %")
elif((n>800) & (n<=1200)):
    p=float(n*.10)
    s=n+p
    print("Novo salario: %.2f"%s)
    print("Reajuste ganho: %.2f"%p)
    print("Em percentual: 10 %")
elif((n>1200) & (n<=2000)):
    p=float(n*.07)
    s=n+p
    print("Novo salario: %.2f"%s)
    print("Reajuste ganho: %.2f"%p)
    print("Em percentual: 7 %")
elif(n>2000):
    p=float(n*.04)
    s=n+p
    print("Novo salario: %.2f"%s)
    print("Reajuste ganho: %.2f"%p)
    print("Em percentual: 4 %")1