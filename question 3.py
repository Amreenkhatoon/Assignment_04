#define function square a number

def square_number(x):return x **2

#sample list of integers
numbers = [4,5,2,9]

#use map
squared_numbers = list(map(square_number,numbers))

#print
print("Square the elements of the list:")
print(squared_numbers)