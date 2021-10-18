def reverse(string):
    rev_str=""
    for i in string:
        rev_str=i+rev_str
    print("reversed string is: ",rev_str)
string=input("enter a string:\n")
print("entered string",string)
reverse(string)