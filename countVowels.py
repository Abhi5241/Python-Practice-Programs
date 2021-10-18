sentence=input("enter the sentence:\n")
string=sentence.lower()
count=0
list1=["a","e","i","o","u"]
for char in string:
    for i in list1:
        if char==i:
            count=count+1
print(count)