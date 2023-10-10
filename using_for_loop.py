for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*"),
    print

def sum(n):
    s=0
    for i in range (1,n+1):
        for j in range(1,i+1):
            s+=j
        return sum