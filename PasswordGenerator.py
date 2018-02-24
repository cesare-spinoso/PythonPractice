import random
import string

tryAgain = True

while(tryAgain):
    print("Welcome to the password generator.\n")
    length = int(input("How long would you like your password to be?\n"))
    if length <= 0:
        print("That can't be!")
        continue

    passwordStrength = input("How strong would you like your password to be? Weak, medium or strong\n")
    if passwordStrength.casefold() == "strong":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        letterListUpperCase = [list(string.ascii_uppercase)]
        symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '\'', '\"']
        totalList = set([numberList, leterListUpperCase, letterListLowerCase, symbolsList])
        passList = [random.sample(totalList, length)]
        password = str(passList)

    elif passwordStrength.casefold() == "medium":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        letterListUpperCase = [list(string.ascii_uppercase)]
        totalList = set([numberList, leterListUpperCase, letterListLowerCase])
        passList = [random.sample(totalList, length)]
        password = str(passList)

    elif passwordStrength.casefold() == "weak":
        numberList = [1,2,3,4,5,6,7,8,9]
        letterListLowerCase = [list(string.ascii_lowercase)]
        totalList = [numberList, letterListLowerCase]
        totalSet = set()
        for i in totalList:
            totalSet.add(i)

        passList = [random.sample(totalSet, length)]
        password = str(passList)

    print("You password is {}".format(password))
    if (input("would you like to go again")).casefold() != "yes":
        tryAgain = False




