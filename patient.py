'''
Create a class to represent a patient of a doctor's office. 
The Patient class will accept the following information during initialization

Social security number
Date of birth
Health insurance account number
First name
Last name
Address
The first three properties should be read-only. 
First name and last name should not be exposed as properties at all, 
but instead expose a calculated property of full_name. 
Address should have a getter and setter.
'''
class Patient:
    def __init__(self, ssn, dob, insur_num, f_name, l_name, addr):
        self.__ssn = ssn
        self.__dob = dob
        self.__insur_num = insur_num
        self.full_name = f'{f_name} {l_name}'
        self.addr = addr

    @property
    def social_security_number(self):
        try:
            return self.__ssn
        except AttributeError:
            return 0

    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0

    @property
    def insur_num(self):
        try:
            return self.__insur_num
        except AttributeError:
            return 0
    
    def first_name(self):
        return 0

    def last_name(self):
        return 0


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
