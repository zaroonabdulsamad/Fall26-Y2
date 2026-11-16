n = int(input("Enter a positive number: "))
if n<0:
    print("Invalid Number!")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
#Inverted Pattern
n = int(input("Enter a positive number: "))
if n<0:
    print("Invalid Number!")
else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()

for i in range(1,n+1):
    print("Table of ",i)
    for j in range(1,11):
        print(f"{i}*{j}=",i*j)
    print()