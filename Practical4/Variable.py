a=15
b=75
c=a+b
d=90
e=5
f=d+e
if c<f:
  print("bus is faster")
else:
    print("driving is faster")
print(f"bus：{c}min")
print(f"driving：{f}min")

X = True
Y = False
W = X and Y
print(f"X: {X}, Y: {Y}, W (X and Y): {W}")
print("X\tY\tW (X and Y)")
print(f"{True}\t{True}\t{True and True}")
print(f"{True}\t{False}\t{True and False}")
print(f"{False}\t{True}\t{False and True}")
print(f"{False}\t{False}\t{False and False}")
print("the first ten triangular number：")
