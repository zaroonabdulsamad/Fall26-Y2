passed=0
failed=0
highest_marks=0
total=0
student=1

for i in range(1,11):
    while True:
        marks=int(input(f"Enter Marks for Student {student}: "))

        if marks >= 0 and marks <= 100:
            break
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")
    student += 1
    total+=marks

    if marks>=90 and marks<=100:
        print("A")
        passed+=1
    elif marks>=80 and marks<=89:
        print("B")
        passed+=1
    elif marks>=70 and marks<=79:
        print("C")
        passed+=1
    elif marks>=60 and marks<=69:
        print("D")
        passed+=1
    elif marks>=50 and marks<=59:
        print("F")
        passed+=1
    else:
        print("F")
        failed+=1

    if marks>highest_marks:
        highest_marks=marks


print("Highest Marks are",highest_marks)
print("Total Passed students are: ",passed)
print("Total Failed Students are: ",failed)

print("Average Marks of Class are: ",total/10)