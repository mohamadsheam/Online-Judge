#__author__ = 'Boss_is_Boss'
def main():
    T=int(input())
    while(T>0):
        x=int(input())
        sum=0
        for i in range(1,x):
            if(x%i==0):
                sum+=i
        if (sum==x):
            print("{} eh perfeito".format(x))
        else:
            print("{} nao eh perfeito".format(x))
        T-=1
if __name__=="__main__":
    main()

