def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("Moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)

hanoi(2,'A','B','C')