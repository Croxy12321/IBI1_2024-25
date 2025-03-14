#Prompt user to enter weight and height
weight = float(input("Enter your weight（kg）："))
height = float(input("Enter your height（m）："))
#Calculate BMI
bmi = weight / (height ** 2)
#Determine weight category based on BMI
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 30:
    category = "normal"
else:
    category = "obese"
#Output the result
print(f"your BMI is {bmi:.2f}，you are {category}")
