num=int(input("enter the number"))
a=num
result=0
n=len(str(num))
while(a!=0):
    digit=a%10
    result=result+digit**n
    a=a//10

if num==result:
    print("yes it is the armstrong number")
else:
    print(f"No,it is not an armstrong number : {result}")