# Prompts the user for a certain number of fibonacci numbers
# Outputs that number of fibonacci numbers and identifies the numbers that are prime
# Gives the user the runtime of the program.
import time

def fibonacciSequence(lengthOfSequence):
    baseCase = [1,1]
    recursive = []
    if lengthOfSequence <= 0:
        return None
    elif lengthOfSequence == 1:
        return [1]
    elif lengthOfSequence == 2:
        return [1, 1]
    else:
        recursive = [1,1]
        for j in range(2, lengthOfSequence):
            j = recursive[j-1] + recursive[j-2]
            recursive.append(j)
        return recursive

def isPrime(input):
    if input <= 0:
        return False
    array1 = range(1, input + 1)
    divisors = [i for i in array1 if input % i == 0]
    if len(divisors) == 2 and divisors[0] == 1 and divisors[1] == input:
        return True
    else:
        return False


def listPrimes(fibList):
    newList = []
    for i in fibList:
        if isPrime(i):
            newList.append(i)
    return newList

length = -1
while length < 0 or type(length) is not int:
    length = int(input("Enter your desired number of fibonacci numbers.\n"))
# Start timer
start = time.time()
arrayFib = fibonacciSequence(length)
listPrimeAndFib = listPrimes(arrayFib)
end = time.time()
print("The list of the first {} fibonacci number(s) is {}".format(length, arrayFib))
print("Of those fibonacci numbers the following are prime {}".format(listPrimeAndFib))
# End timer and print result
print("Your prgrams run time period was: {}".format(end - start))
#Displaying a goodbye message
print("Thank you for using the Fibonnaci numbers generator")

