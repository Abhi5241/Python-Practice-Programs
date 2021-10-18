#using inbuilt method we can find the gcd
#import math
#a=math.gcd(4,18)
#a=int(input("enter the value of a"))
#print(a)


def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

num1=int(input("Enter the first number:\n"))
num2=int(input("enter the second number:\n"))
print(GCD(num1,num2))