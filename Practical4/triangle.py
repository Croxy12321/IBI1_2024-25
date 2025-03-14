#Print the title of the program
print("the first ten triangular number:")
#Loop through numbers 1 to 10
for n in range(1, 11):
    #Calculate the triangular number for the current n
    triangle_number = sum(range(1, n + 1))
    #Print the calculated triangular number
    print(triangle_number)
