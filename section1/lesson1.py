#!/usr/bin/python3
'''
simple program to
- read in a list if up to twenty elements
- print elements in list
- print out number of unique elements
- print out the frequency of each element
- print maximum value
- print minimum value
- Print average element value
- print the standard deviation of the unique elements in the list
'''
import math
print("Hi please enter 20 integers or -1 to stop inputting numbers ")
# read in a list if up to twenty elements
list_0f_number = []
number = 0
count = 1
while count <= 20 and number >= 0:
    try:
        number = int(input("enter number {}:  ".format(count)))
        count += 1
    except ValueError:
        print("Value entered is not a valid number")
    else:
        if number >= 0:
            list_0f_number.append(number)
# print elements in list
output_string = "elements in list = {}".format(list_0f_number)
print(output_string)

# print out number of unique elements
unique_elements = set(list_0f_number)
number_of_unique_elements = len(unique_elements)
print("list contains {} elements".format(number_of_unique_elements))

# print out the frequency of each element
print("N\tcount")
for index in unique_elements:
    uni_count = 0
    for x in list_0f_number:
        if index == x:
            uni_count += 1
    print("{}\t{}".format(index, uni_count))

# print maximum value
print("Maximum element is {}".format(max(unique_elements)))

# print minimum value
print("Minimum element is {}".format(min(unique_elements)))

# Print average element value 
average = sum(list_0f_number)/len(list_0f_number)
print("Average element value is {}".format(average))

# print the standard deviation of the unique elements in the list
temp = 0.0
for index in unique_elements:
    temp = temp + ((index - average) * (index - average))
result = temp/number_of_unique_elements
result = math.sqrt(result)
print("Standard deviation is {}".format(result))
