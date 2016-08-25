def main():
    while(True):
        line=input().split(" ")
        a,b=line
        x=int(a)
        y=int(b)
        maxx=max(x,y)
        minn=min(x,y)
        total=0

        if x>0 and y>0:

            for i in range(minn,maxx+1):
                total+=i
                print(i,end=' ')
            print("Sum={}".format(total))
        else:
            break
if __name__=="__main__":
    main()

