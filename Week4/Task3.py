count=0
sum=0

sn=int(input("Enter Starting Number for range: "))
en=int(input("Enter Ending Number for range: "))
print("Primary Numbers: ")
for i in range(sn,en):
    if i<2:
        continue
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break

    if prime:
        print(i)
        count+=1
        sum+=i

print("Total Primary Number are: ",count)
print("Sum of Primary Number are: ",sum)