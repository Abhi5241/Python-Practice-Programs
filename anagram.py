s1=input("enter string 1\n")
s2=input("enter string 2\n")
ss1=sorted(s1)
ss2=sorted(s2)
if ss1==ss2:
    print("This is anagram")
else:
    print("Not an anagram")