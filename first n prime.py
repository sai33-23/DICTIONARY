i=1
c=0
n=int(input("enter a number"))
while c<n:
    f=0
    j=1
    while j<=i:
        if i%j==0:
            f=f+1
        j=j+1
    if f==2:
        print(i)
        c=c+1
    i=i+1
