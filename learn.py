


def num():
    
    sum=0
    while True:
        i=int(input("enter a num: "))
        if i==0:
            break
            
        elif i%2==0:
            continue
            
        else:
            sum=sum+i
    print(sum)
            

            
        

def main():
    num()

if __name__=="__main__":
    main()
            