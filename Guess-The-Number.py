import random
secretNumber=random.randint(1,20)
userNum=-1
print("Enter number between 1-20")
while(userNum !=secretNumber):
    userNum=int(input("Enter number: "))
    if userNum<secretNumber:
        print("Entered number is too low")
    elif userNum>secretNumber:
        print("Entered number is too high")
    else:
        print("Thank you!")
        break

