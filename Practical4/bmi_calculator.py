weight = float(input("Enter your weight（kg）："))
height = float(input("Enter your height（m）："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 30:
    category = "normal"
else:
    category = "obese"

print(f"your BMI is {bmi:.2f}，you are {category}")
