# input the strength of paracetamol and the weight of the child
strength = float(input("Enter the strength of paracetamol in mg/5ml(enter 120 or 250):"))
weight = float(input("Enter the weight of the child in kg(in 10~100):"))
# check if the strenghth and weight are in the range
if strength not in [120, 250]:
    print("Invalid strength. Please enter 120 or 250.")
    exit()
if weight < 10 or weight > 100:
    print("Invalid weight. Please enter a weight between 10 and 100 kg.")
    exit()
# caculate the dosage of paracetamol
dosage = weight * 15
# define the function
def calculate_volume(strength, weight):
    if strength == 120:
        volume = dosage / 24
    elif strength == 250:
        volume = dosage / 50
    return volume
# call the function
volume = calculate_volume(strength, weight)
# print the result
print(f"The dosage of paracetamol for a child weighing {weight} kg is {dosage} mg.")
print(f"The volume of paracetamol to be given is {volume} ml.")
