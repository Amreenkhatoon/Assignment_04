# define function to a triple number

def triple_number(x):return x*3

#sample list of inetgers
numbers = [1,2,3,4,5,6,7]

#use map to triple
tripled_numbers = list(map(triple_number,numbers))

#print
print("Triple of list numbers:")
print(tripled_numbers)

