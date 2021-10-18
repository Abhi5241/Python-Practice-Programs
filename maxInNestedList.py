list1=[[2,44],3,1,5,8]
list2=[]
def get_max(list1):
    for i in list1:
        if type(i)==list:
            get_max(i)
        else:
            list2.append(i)
    return max(list2)
print(get_max(list1))