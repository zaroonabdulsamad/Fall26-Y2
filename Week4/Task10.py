even=0
odd=0
largest_number=0
total=0

while True:
    user=int(input("Enter Integer: "))

    if user==0:
        break

    elif user<0:
        print("Invalid Number, Try Again!")
        continue

    if user%2==0:
        print("It is Even Number")
        even+=1
    else:
        print("It is Odd Number")
        odd+=1
    if user>largest_number:
        largest_number=user

    total+=user
    count=even+odd

    if count==0:
        print("No positive numbers entered!")
    else:
        average=total/count

    print("Even Numbers:",even)
    print("Odd Numbers:",odd)
    print("Largest Number:",largest_number)
    print("Sum:",total)
    print("Average:",average)