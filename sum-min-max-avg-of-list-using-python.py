number = int(input('Enter The Number of Elements: '))

listOne = list()

for i in range(number):
    elements = int(input("Enter the number: "))
    listOne.append(elements)


SumOne = sum(listOne) # default function to find sum of all elements inside list
MinimumOne = min(listOne) # default function to find minimum number inside a list
MaximumOne = max(listOne) # default function to find maximum number inside a list
AverageOne = SumOne / len(listOne) # len() default function to find number of elements inside a list


print("Sum of numbers is: ", SumOne)
print("Minimum of Numbers is: ", MinimumOne)
print("Maximum of Numbers is: ", MaximumOne)
print("Average of Numbers is: ", AverageOne)
