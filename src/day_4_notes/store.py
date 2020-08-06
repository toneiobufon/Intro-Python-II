#example to create a department store 

#store will have different departments

import sys
from user import User
class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    def print_departments(self):
        for id, name in self.departments.items():
            print(f"{id}: {name}")
# user will pass in either 0 or 1 command-line arguments to the program
num_args = len(sys.argv)
# if they pass in 0, we'll default their money to 100 
if num_args == 1:
    user = User(100)
# if they pass in 1 argument (a number), set their money to that amount 
elif num_args == 2:
    user = User(int(sys.argv[1]))
else:
    print("Usage: store.py [money]")
    sys.exit(1)
departments = {
    23: "Groceries", 
    9: "Books", 
    13: "Electronics", 
    7: "Clothes", 
    15: "Toys" 
}
store = Store("Quarantine Store", departments)
while True:

    print(user)
    # print departments 
    store.print_departments()
    selection = input("Which department would you like to visit? ")
    if selection == 'quit' or selection == 'q':
        break
    # expect user to type in a number that is read in as a string 
    # parse it into an int, and then check if the int is a valid 
    dep_num = int(selection)
    if dep_num in departments:
        # if it is, go to that department
        print(f"You picked department number {dep_num}, the {departments[dep_num]} department.")
    else:
        # otherwise, print a message saying that is not a valid department 
        print("That is not a valid department.")