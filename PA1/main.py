import sys
import csv
import re
import pickle

from Employee import Employee


# main function
def main():
    # check if the user has entered a path
    if len(sys.argv) < 2:
        print("Please enter a path to a csv file")
        return
    # read a csv file given a path in the sysarg and store it in a list
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        # call the file_processor function excluding the first row(header)
        d = file_processor(data[1:])
        print("\n")

    # save the dictionary to a pickle file
    pickle.dump(d, open("employee.p", "wb"))

    # read the pickle file
    dict_in = pickle.load(open("employee.p", "rb"))
    print("Employee list:\n")
    display_employee(dict_in)


# process the data
def file_processor(data):
    # initialize a dictionary
    employee_dict = {}
    print(data)
    print()
    # loop through the data
    for row in data:
        first_name = row[0].capitalize()
        last_name = row[1].capitalize()
        # if no middle initials are given, set it to 'X'
        if row[2] == '':
            middle_initials = 'X'
        else:
            middle_initials = row[2].upper()

        employee_id = validate_id(row[3])
        phone_number = validate_phone_number(row[4])

        # check if the employee id is already in the dictionary
        while employee_id in employee_dict:
            # if it is, print an error message
            print("Employee id already exists")
            employee_id = input("Enter employee id: ")
            # validate the id
            employee_id = validate_id(employee_id)

        employee = Employee(last_name, first_name, middle_initials, employee_id, phone_number)
        # add the employee to the dictionary
        employee_dict[employee_id] = employee

    return employee_dict


# validate the employee id
def validate_id(employee_id):
    # check if id is 2 letters followed by 4 digits
    if re.match(r'[a-zA-Z]{2}\d{4}', employee_id):
        employee_id = employee_id[:2].upper() + employee_id[2:]
        return employee_id
    else:
        # Error message and prompt user to enter a valid id
        print("ID invalid: " + employee_id)
        print("ID is two letters followed by four digits")
        employee_id = input("Please enter a valid id: ")
        # call the function again
        return validate_id(employee_id)


# validate the phone number. Make sure it is in the format xxx-xxx-xxxx
def validate_phone_number(phone_number):
    # check if phone number is in the correct format
    if re.match(r'\d{3}-\d{3}-\d{4}', phone_number):
        return phone_number
    else:
        # Error message and prompt user to enter a valid phone number
        print("Phone number " + phone_number + " is invalid")
        print("Enter phone number in the format xxx-xxx-xxxx:")
        phone_number = input("Enter phone number: ")
        # call the function again
        return validate_phone_number(phone_number)


def display_employee(employee_dict):
    # loop through the dictionary
    for employee_id, employee in employee_dict.items():
        # call the display function
        employee.display()
        print()


# initialize the main function
if __name__ == "__main__":
    main()
