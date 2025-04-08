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