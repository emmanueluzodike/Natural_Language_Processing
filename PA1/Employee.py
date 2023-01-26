class Employee:
    # initialize the class
    def __init__(self, last_name, first_name, middle_initials, employee_id, office_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_initials = middle_initials
        self.employee_id = employee_id
        self.office_phone = office_phone

    # display attributes of the class
    def display(self):
        print("Employee id: ", self.employee_id + "\n \t "
              + self.last_name + " " + self.middle_initials + " " + self.first_name + "\n \t "
              + self.office_phone)
