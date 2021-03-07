def toStr(num):
    if(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    if(num % 3 == 0):
        return "Fizz"
    if(num % 5 == 0):
        return "Buzz"
    return str(num)

def printFizzBuzz():
    for x in range(1, 101):
        print(toStr(x))