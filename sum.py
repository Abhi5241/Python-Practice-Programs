num=int(input("Enter the number:\n"))
sum=0
length=len(str(num))
for i in range(length):
    digit=num%10
    sum=sum+digit
    num=num//10

print("sum is :",sum)