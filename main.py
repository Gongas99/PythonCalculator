def printMenu():
    print('Welcome to Python Calculator!\n'
          'Choose your option:\n'
          '1. Sum Numbers\n'
          '2. Subtract Numbers\n'
          '3. Multiply Numbers\n'
          '4. Divide Numbers\n'
          '5. Exit\n')

def checkIfIsNumber(input):
    try:
        val = int(input)
        return int(val)
    except ValueError:
        try:
            val = float(input)
            return float(val)
        except ValueError:
            return 'error'

def getValidInput():
    while True:
        n = checkIfIsNumber(input('>'))
        try:
            n.isnumeric()
            print('Please insert a number!')
        except AttributeError:
            return n


def readOption():
    while True:
        n = getValidInput()
        if isinstance(n, float):
            print('Please select a valid option!')
        elif n <= 0 or n > 5:
            print('Please select a valid option!')
        else:
            return n

def getValidParameters():
    while True:
        n = getValidInput()
        if isinstance(n, float):
            print('Please enter a valid number!')
        elif n < 2:
            print('Please enter a value greater than 2!')
        else:
            return n

def execFunction(opt, list):
    if opt == 1:
        result = 0
        for i in list:
            result += i
        return result
    elif opt == 2:
        result = list[0]
        list.remove(list[0])
        for i in list:
            result -= i
        return result
    elif opt == 3:
        result = list[0]
        list.remove(list[0])
        for i in list:
            result *= i
        return result
    elif opt == 4:
        result = list[0]
        list.remove(list[0])
        for i in list:
            result /= i
        return result


def get_numbers(opt):
    print('Insert the number of parameters: ')
    # get a valid number of parameters
    n = getValidParameters()
    # auxiliar value to stop the while loop
    aux = 0
    list = []
    while aux < n:
        print('Insert a number: ')
        val = getValidInput()
        list.append(val)
        aux += 1
    return execFunction(opt, list)

if __name__ == '__main__':
    while True:
        printMenu()
        opt = readOption()
        if opt == 5:
            raise SystemExit()
        else:
            result = get_numbers(opt)
            print(f'Result is: {result}')
