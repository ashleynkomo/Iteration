#Ashley Nkomo
#16-10-14
#Task 2-3 Iteration Class exercises

total = 0
numbers_av = int(input("Please enter the number of numbers to be averaged: "))

for average in range(numbers_av):
    number = int(input("Please enter a number to average: "))
    total += number
    average = total / numbers_av


print("The average of the numbers you entered is {0}".format(average))

#finished
