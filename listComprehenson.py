




if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list=[[i,j,k] for i in [i for i in range(x+1)] for j in [j for j in range(y+1)] for k in [k for k in range(z)] if x+y+z!=n ]
    print(list)