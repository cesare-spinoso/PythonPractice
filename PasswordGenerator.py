import random
import string

tryAgain = True

while tryAgain:
    print("Welcome to the password generator.\n")
    # Pwd length and strength
    try:
        length = int(input("How long would you like your password to be?\n"))
    except Exception:
        print("Invalid input type. Restarting.")
        continue
    if length < 0:
        print("Cannot have negative length. Restarting.")
        continue
    passwordStrength = input("How strong would you like your password to be? Weak, medium or strong\n")
    # Symbols to go in password
    numberList = [str(i) for i in range(1,10)]
    letterListLowerCase = list(string.ascii_lowercase)
    letterListUpperCase = list(string.ascii_uppercase)
    symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '\'', '\"']
    # Match password strength
    if passwordStrength.upper() == "STRONG":
        totalList = numberList.copy()
        totalList.extend(letterListUpperCase)
        totalList.extend(letterListLowerCase)
        totalList.extend(symbolsList)

    elif passwordStrength.upper() == "MEDIUM":
        totalList = numberList.copy()
        totalList.extend(letterListUpperCase)
        totalList.extend(letterListLowerCase)

    elif passwordStrength.upper() == "WEAK":
        totalList = numberList.copy()
        totalList.extend(letterListLowerCase)

    else:
        print("Choose out of weak, medium and strong.")
        continue

    # Convert to a string password
    print(totalList)
    passList = random.sample(totalList, length)
    print(passList)
    password = ''.join(passList)

    print("You password is {}".format(password))
    if (input("Would you like to go again (yes/no)?")).casefold() != "yes":
        tryAgain = False

print("Bye now!")



