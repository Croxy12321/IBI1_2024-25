#Initialize variables with given values
a=15
b=75
c=a+b
d=90
e=5
f=d+e
#Compare the values of c and f to determine which is faster and print the result
if c<f:
  print("bus is faster")
else:
    print("driving is faster")
#Print the time taken for bus and driving
print(f"bus：{c}min")
print(f"driving：{f}min")

#Initialize variables with boolean values
X = True
Y = False
W = X and Y
#Print the values of X, Y, and the result of X AND Y
print(f"X: {X}, Y: {Y}, W (X and Y): {W}")
#Print the column headers
print("X\tY\tW (X and Y)")
#Print the results of logical operations with tab separation
print(f"{True}\t{True}\t{True and True}")
print(f"{True}\t{False}\t{True and False}")
print(f"{False}\t{True}\t{False and True}")
print(f"{False}\t{False}\t{False and False}")
