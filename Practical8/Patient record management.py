# The first part of the code is an input system that allows users to freely enter patient information and simply identify whether the input conforms to the requirements. 
# The second part is defining functions and class
# In the last part, I added an example

import re
name=input("Enter the patient's name: ")
age=input("Enter the patient's age: ")
admission_date=input("Enter the patient's admission date(ex.20060312): ")
history=input("Enter the patient's history(If there is no past medical history, please enter 'None'): ")
# check if the age is in the range
if not age.isdigit() or int(age) < 0:
    print("Invalid age. Please enter a valid age.")
    exit()
# check if the admission date is in the format of YYYYMMDD
if not re.match(r'^\d{8}$', admission_date):
    print("Invalid admission date. Please enter a valid date in the format YYYYMMDD.")
    exit()
# check if the history is not empty
if not history:
    print("Invalid history. Please enter a valid history.")
    exit()
# check if the name is not empty
if not name:
    print("Invalid name. Please enter a valid name.")
    exit()

# create a class of patient's record
class patients(object):
    def __init__(self, name, age, admission_date, history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.history = history
    # create a funtion to list the patient's record
    def print_details(self):
        print(f"{self.name}, {self.age}, {self.admission_date}, {self.history}")
# call the class and the function
patient = patients(name, age, admission_date, history)
patient.print_details()

# create an example and call the function and the class
example_name = 'Alice'
example_age = 25
example_admission_date = 20060312
example_history = None
example_patient = patients(example_name, example_age, example_admission_date, example_history)
# explain the example
print(f'Example: The patient\'s name is {example_name}, age is {example_age}, admission date is {example_admission_date}, and history is {example_history}.')
# use the function to deal with the example
example_patient.print_details()
