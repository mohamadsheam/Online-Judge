line=input().split(" ")
a,b=line
x=int(a)
y=int(b)
if(x>=y):
    h=(24-x)+y
else:
    h=y-x
print("O JOGO DUROU %d HORA(S)" %h)1