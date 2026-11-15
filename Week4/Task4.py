max_attempt=3
username="admin"
password = "Hassan@13"

print("Enter Your Correct Credentials, so that we can verify, is it really You: \n")
while True:
    name=input("Enter Your username: ").lower()
    passes=input("Enter Your Password: ")

    if name=="" or passes=="":
        print("Nothing is there, please try again")
        continue
    elif name==username and passes==password:
        print("You have successfully joined!.")
        break
    else:
        max_attempt-=1
        print(f"Invalid Username or Password!. and {max_attempt} remain")
        if max_attempt==0:
            print("Your account is locked as u have Tried more then 3 times.")
            break
