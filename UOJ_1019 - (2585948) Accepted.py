n=int(input())
h=int(n/3600)
aux=n%3600
m=int(aux/60)
s=aux%60

print(h,m,s,sep=':')1