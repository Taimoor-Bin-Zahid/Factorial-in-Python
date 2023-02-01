def FactorialOfNum(number):

    factorial = 1

    if (number < 0):
        print("Factorial of a negative number is not defined please enter a positive number!")

    elif(number == 0):
        print("1")

    else:
        for i in range(1, number+1):
            factorial = factorial* i
        return factorial

if __name__ == '__main__':
    print("Enter the Number: ")
    number = int(input())
    print("The Factorial of ", number, " is ", FactorialOfNum(number))