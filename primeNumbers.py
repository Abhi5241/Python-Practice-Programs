
upper=int(input("enter the upper interval:\n"))
for num in range(0,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)