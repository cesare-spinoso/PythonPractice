import random
import string

tryAgain = True

while(tryAgain):
    print("Welcome to the password generator.\n")
    length = int(input("How long would you like your password to be?\n"))
    if length <= 0 or type(length) is not int:
        print("That can't be!")
        continue

    passwordStrength = input("How strong would you like your password to be? Weak, medium or strong\n")
    if passwordStrength.upper() == "STRONG":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        letterListUpperCase = [list(string.ascii_uppercase)]
        symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '\'', '\"']
        totalList = set([numberList, leterListUpperCase, letterListLowerCase, symbolsList])
        passList = [random.sample(totalList, length)]
        password = str(passList)

    elif passwordStrength.upper() == "MEDIUM":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        letterListUpperCase = [list(string.ascii_uppercase)]
        totalList = set([numberList, leterListUpperCase, letterListLowerCase])
        passList = [random.sample(totalList, length)]
        password = str(passList)

    elif passwordStrength.upper() == "WEAK":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        totalList = [numberList, letterListLowerCase]
        totalSet = set()
        for i in totalList:
            totalSet.add(i)
        passList = [random.sample(totalSet, length)]
        password = str(passList)
    else:
        print("Choose out of weak, medium and strong.")
        continue

    print("You password is {}".format(password))
    if (input("Would you like to go again (yes/no)?")).casefold() != "yes":
        tryAgain = False

print("Bye now!")



