#__author__ = 'Boss_is_Boss'
def main():
    sum=0
    i=0
    while (True):
        x=int(input())
        if (x>=0):
            sum+=x
            i+=1
        else:
            break
    print("%.2f"%(sum/i))

if __name__=="__main__":
    main()