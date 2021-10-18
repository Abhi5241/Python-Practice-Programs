data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
marks = data[input("marks")]
print("%.2f" % (sum(marks)/len(marks)))