def isLeapYear(year):
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    else:
        return year % 4 == 0

def printIsYear(year):
    if(isLeapYear(year)):
        print(str(year) + " is a leap year!")
    else:
        print(str(year) + " is not a leap year!")