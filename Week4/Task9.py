n=int(input("Enter number of terms: "))
a=0
b=1
total=0
even=0
odd=0
if n<1:
    print("Invalid number of terms!")
else:
    print("Fibonacci Sequence:")
    for i in range(n):
        print(a,end=" ")
        total+=a
        if a % 2 == 0:
            even += 1
        else:
            odd += 1

        next_num=a+b
        a=b
        b=next_num

    print()
    print("Sum:", total)
    print("Even terms:", even)
    print("Odd terms:", odd)
