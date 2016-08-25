__author__ = 'Boss_is_Boss'

def main():
    total=0
    line=input().split(" ")
    a,b=line
    A=int(a)
    N=int(b)
    if (N<=0):
        N=int(input( ))
    else:
        for i in range(N):
            total+=A
            A+=1
    print(total)
if __name__=="__main__":
    main()
