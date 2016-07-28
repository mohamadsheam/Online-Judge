n=int(input())
hun,fif,tw,ten,fiv,two,one=0,0,0,0,0,0,0
hun=int (n/100)
aux=n%100
fif=int(aux/50)
aux=aux%50
tw=int(aux/20)
aux=aux%20
ten=int(aux/10)
aux=aux%10
fiv=int(aux/5)
aux=aux%5
two=int(aux/2)
aux=aux%2
one=int(aux/1)
aux=aux%1
print(n)
print("%d nota(s) de R$ 100,00"%hun)
print("%d nota(s) de R$ 50,00"%fif)
print("%d nota(s) de R$ 20,00"%tw)
print("%d nota(s) de R$ 10,00"%ten)
print("%d nota(s) de R$ 5,00"%fiv)
print("%d nota(s) de R$ 2,00"%two)
print("%d nota(s) de R$ 1,00"%one)
1