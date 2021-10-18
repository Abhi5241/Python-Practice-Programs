string=input("enter the string:")
print(string[::-1])
if string==string[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")