n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
if a[-1]==a[-2]:
    a.pop()
a.pop()
print(max(a))