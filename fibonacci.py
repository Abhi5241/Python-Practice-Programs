num=int(input("enter the number"))
first=0
second=1
for i in range(num):
    print(first,end=" ")
    temp=first
    first=second
    second=temp+second
print()