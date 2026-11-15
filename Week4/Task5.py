import random
max_attempt=7
countvalid=0

secret=random.randint(1,100)

while True:
    user=int(input("Enter Guessed Number in range of 1,100: "))
    if user<1 or user>100:
        print("Invalid number")
        continue
    countvalid+=1
    max_attempt-=1

    if user==secret:
        if countvalid==1:
            print("Welldone u have guessed in first attempt")
        else:
            print(f"Well done! You guessed in {countvalid} attempts")
            break

    elif user<secret:
        print("The guessed number is smaller")

    elif user>secret:
        print("Guessed number is larger")

    if max_attempt == 0:
        print(f"You failed to guess and secret number is {secret}")
        break