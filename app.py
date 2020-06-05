# ---------------------------------------------------------------
# To-Do:
# -> There is a problem, try solve it (search about #TO-DO_257) #Solved
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Updates:
# -> I think problem #TO-DO_257 was solved, I don't know how but I think it's because i changed this line (| if int(manager): |) --> (| if manager: |)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Notes:
# -> This project is not completed 100% but still you can use it
# -> I know there are some bugs (I'm beginner :3)
# -> You can link the project with database, but you have edit the code :$
# --> github: https://github.com/MrHoora
# --> Linkedin: https://www.linkedin.com/in/%D8%B3%D9%84%D9%85%D8%A7%D9%86-%D8%A2%D9%84-%D8%B9%D9%8A%D8%B3%D9%89-a04930170/?locale=en_US
# ---------------------------------------------------------------

# arg_list
# -> 0 = all
# -> 1 = full name
# -> 2 = salary
# -> 3 = years
# -> 4 = MANAGER [1 = yes, 0 = no]

# default_arg
# Change it to what you want!
default = {
    'fullName': "null null",
    'salary':   0,
    'years':    0,
    'MANAGER':  0,       # No
    'set':{
        'years':[0, 40], # [min, max]
        'salary': [0, 80000] # [min, max] max = 0 --> unlimited 
    }
}

# PLEASE DO NOT REMVOE OR EDIT UNDER THIS LINE !!!!
employees = [];import colorama;colorama.init();config = {'color':{'rest': '\033[0m','red': '\033[0;31m','green': '\033[0;32m','black': '\033[0;30m','blue': '\033[0;34m','cyan': '\033[0;36m','purple': '\033[0;35m','yellow': '\033[0;33m'}}
def color(text, color = ''):
    col = config['color']['rest'] if color == '' else config['color']['red'] if color == 'red' else config['color']['green'] if color == 'green' else config['color']['black'] if color == 'black' else config['color']['blue'] if color == 'blue' else config['color']['cyan'] if color == 'cyan' else config['color']['purple'] if color == 'purple' else config['color']['yellow'] if color == 'yellow' else config['color']['rest']
    return col+""+text+""+config['color']['rest']
# PLEASE DO NOT REMOVE OR EDIT ABOVE THIS LINE !!!!

# import os package to ues system commands 
# in this app it will be uesd for os.system('cls') only!
import os

# Class EMPLOYEE
class employee():
    # constructor
    def __init__(self, fullName, salary, years, MANAGER):
        super().__init__()
        
        if fullName == "": fullName = default['fullName']
        if salary == "": salary = default['salary']
        # Check if salary is less than max default or more than min default
        else: 
            if int(salary) > default['set']['salary'][1]: salary = default['set']['salary'][1]
            elif int(salary) < default['set']['salary'][0]: salary = default['set']['salary'][0]
        if years == "": years = default['years']
        # Check if years is less than max default or more than min default
        else: 
            if int(years) > default['set']['years'][1]: years = default['set']['years'][1]
            elif int(years) < default['set']['years'][0]: years = default['set']['years'][0]
        if MANAGER == "": MANAGER = default['MANAGER']
        
        self.fullName = fullName
        self.salary = salary
        self.years = years
        self.MANAGER = int(MANAGER)
    
    # return values by using V
    # get([arg_list])
    def get(self, arg = 0):
        
        # arg_list
        if arg == 0:
            return self.fullName, self.salary, self.years, self.MANAGER
        if arg == 1:
            return self.fullName
        if arg == 2:
            return self.salary
        if arg == 3:
            return self.years
        if arg == 4:
            return self.MANAGER
    
    # Set new value and check it
    # How? set([arg_list], newValue)
    def set(self, arg, newValue = 0):
        # Check if values are empty or NOT!
        if arg == "" or newValue == "":
            print(color("\tValues must NOT be empty!!\n\tset(id, arg = {1}, newValue = {2}) ".format(arg, newValue), "red"))
            # print("\tValues must NOT be empty!!\n\tset(id, arg = {1}, newValue = {2}) ".format(arg, newValue))
            return 0
        
        # if arg was 0 then all args will be reset to default values!
        # you can change default values in default_arg
        if int(arg) == 0:
            self.fullName = default['fullName']
            self.salary = default['salary']
            self.years = default['years']
            self.MANAGER = default['MANAGER']
            return 1
            
        if int(arg) == 1: # full name
            self.fullName = str(newValue)
            return 1
        
        if int(arg) == 2: # salary
            if default['set']['salary'][1] == 0:
                if int(newValue) >= default['set']['salary'][0]:
                    self.salary = int(newValue)
                else:
                    print(color("\tSalary must be more than {0}!".format(default['set']['salary'][0]), 'red'))
                    return 0
            else:
                if int(newValue) >= default['set']['salary'][0] and int(newValue) <= default['set']['salary'][1]:
                    self.salary = int(newValue)
                else:
                    print(color("\tSalary must be between {0} and {1}".format(default['set']['salary'][0],default['set']['salary'][1]), 'red'))
                    return 0
            
        if int(arg) == 3: # years
            if int(newValue) >= default['set']['years'][0] and int(newValue) <= default['set']['years'][1]:
                self.years = int(newValue)
                return 1
            else:
                print(color("\tYears must be between {0} and {1}!".format(default['set']['years'][0], default['set']['years'][1]), 'red'))
                return 0
            
        if int(arg) == 4: # MANGAER
            if int(newValue) == True:
                self.MANAGER = 1
                return 1
            elif int(newValue) == False:
                self.MANAGER = 0
                return 1
            else: 
                print(color("\tTo change manager value, you must ues (True or False in newValue)!", 'red'))
                return 0
            
    def info(self, id = -1, type = 0):
        if type == 0:
            if self.MANAGER == 1: isManager = 'Yes'
            else: isManager = 'No'
            print(color("\t[{}] ".format(id), 'yellow') + color("\tFull name: {0}\n\t\tSalary: {1}\n\t\tYears: {2}\n\t\tIs manager? {3}".format(self.fullName, self.salary, self.years, isManager), 'cyan'))

# def logs(file, action, text):

# This function to print main page and to allow user to choose option
def main():
    
    # Print message to user and options
    # Ask user to choose option
    print(color("\n\tEmployee data center", 'cyan'))
    print(color("\n\t[1]: Add new emplyee\n\t[2]: Remove employee\n\t[3]: Emplyee list\n\t[4]: Edit employee\n\t[5]: Exit", 'blue'))
    option = input(color("\n\tPlease choose one: ", 'yellow'))
    
    # Check if option value is digit or not
    if option.isdigit() == False:
        os.system('cls')
        if option == "": print(color("\n\tSorry, incorrect option!", 'red'))
        else: print(color("\n\t{} is not in options list!".format(option), 'red'))
        main()
    
    # If user select option number 1 [Add new employee]
    if int(option) == 1:
        os.system('cls')
        fullName = input(color("\n\tFull Name: ", 'yellow'))
        salary = input(color("\tSalary: ", 'yellow'))
        years = input(color("\tYears: ", 'yellow'))
        manager = input(color("\tIs manager? ", 'yellow') + color("[1 = Yes | 0 = No]: ", 'blue'));print("\n")
        newEmp(fullName, salary, years, manager)
        main()

    # If user select option number 2 [Remove employee]
    if int(option) == 2:
        os.system('cls')
        
        # Check if there is employees in the list or not
        if len(employees) == 0:
            print(color("\n\tThere is no employee!", 'red'))
            main()
        
        id = input(color("\n\tPlease enter employee id: ", 'purple'))
        if int(id.isdigit()) == True:
            lenOfEmp = len(employees)
            if lenOfEmp < int(id):
                os.system('cls')
                print(color("\tSorry there is no recordes!!", 'red'))
                main()

            if int(id) >= 0:
                employees[(int(id) - 1)].info(id)
                delE = input(color("Do you want to delete this employee? ", 'yellow') + color("yes/no ", 'red'))
                delE = delE.lower()
                if str(delE) == "yes":
                    os.system('cls')
                    print(color("\tEmployee {} was deleted successfuly!".format(employees[(int(id) - 1)].fullName), 'green'))
                    del employees[(int(id) - 1)]
                elif str(delE) == "no":
                    os.system('cls')
                    
        else:
            os.system('cls')
            print(color("\tPlease enter correct id number!", 'red'))
        main()

    # If user select option number 3 [Employee list]
    if int(option) == 3:
        os.system('cls')
        cont = 0
        for i in range(len(employees)):
            cont += 1
            # print(color("\n\t[{}]".format((i + 1)), 'yellow'))
            employees[i].info((i + 1));print("\n")

        input(color("\n\n{} result found!\nPress enter to continue!".format(cont), 'purple'))
        os.system('cls')
        main()

    # If user select option number 4 [Edit employee] 
    if int(option) == 4:
        os.system('cls')
        
        # Check if there is employees in the list or not
        if len(employees) == 0:
            print(color("\n\tThere is no employee!", 'red'))
            main()

        id = input(color("\n\tPlease enter employee id: ", 'purple'))

        # Check if id is digit, not Empty and it's exist! 
        if int(id.isdigit()) == True:
            lenOfEmp = len(employees)
            if lenOfEmp < int(id):
                os.system('cls')
                print(color("\tSorry there is no recordes!!", 'red'))
                main()

            if int(id) >= 0:
                os.system('cls')
                print(color("\tEmpty = no change\n", 'purple'))

                # Print employee details
                fullName = input(color("\tFull Name ({}): ".format(employees[(int(id) - 1)].get(1)), 'cyan'))
                salary = input(color("\tSalary ({}): ".format(employees[(int(id) - 1)].get(2)), 'cyan'))
                years = input(color("\tYears ({}): ".format(employees[(int(id) - 1)].get(3)), 'cyan'))
                isManager = 'Yes' if employees[(int(id) - 1)].get(4) == 1 else 'No'
                manager = input(color("\tIs manager? ({}) ".format(isManager), 'cyan') + color("1 = YES, 0 = NO: ", 'purple'))

                # THERE IS A PROBLEM HERE !!! #TO-DO_257 #Solved check updates
                # When employee was not manager (No), and want to chagne it, it showed like
                # Manager (Yes) --> (Yes): .....
                # It should be like this
                # Mangaer  (No) --> (Yes): .....
                man = 'Yes' if employees[(int(id) - 1)].get(4) == 1 else 'No'
                if manager:
                    if int(manager) == 1: man2 = 'Yes'
                    else: man2 = 'No'
                else: 
                    if employees[(int(id) - 1)].get(4) == 1: man2 = 'Yes'
                    else: man2 = 'No'
                # Until here!!! 
                
                # Print employee details to check if they correct or not
                os.system('cls')
                print("\t- - - - - - - - - - - - - - - - - - - -")
                print(color("\tFull name ({0})".format(employees[(int(id) - 1)].get(1)), 'cyan') + "\t-->\t" + color(" ({0})".format((fullName if len(fullName) > 0 else employees[(int(id) - 1)].get(1))), 'yellow'))
                print(color("\tSalary ({0})".format(employees[(int(id) - 1)].get(2)), 'cyan') + "\t-->\t" + color(" ({0})".format((salary if len(salary) > 0 else employees[(int(id) - 1)].get(2))), 'yellow'))
                print(color("\tYears ({0})".format(employees[(int(id) - 1)].get(3)), 'cyan') + "\t-->\t" + color(" ({0})".format((years if len(years) > 0 else employees[(int(id) - 1)].get(3))), 'yellow'))
                print(color("\tManager ({0})".format(man), 'cyan') + "\t-->\t" + color(" ({0})".format(man2), 'yellow'))

                # Old one
                # print(color("\tFull name \t({0}) \t\t\t--> ({1})".format(employees[(int(id) - 1)].get(1), (fullName if len(fullName) > 0 else employees[(int(id) - 1)].get(1))), 'blue'))
                # print(color("\tSalary \t\t({0}) \t\t\t\t--> ({1})".format(employees[(int(id) - 1)].get(2), (salary if len(salary) > 0 else employees[(int(id) - 1)].get(2))), 'blue'))
                # print(color("\tYears \t\t({0}) \t\t\t\t--> ({1})".format(employees[(int(id) - 1)].get(3), (years if len(years) > 0 else employees[(int(id) - 1)].get(3))), 'blue'))
                # print(color("\tManager \t({0}) \t\t\t\t--> ({1})".format(man, man2), 'blue'))
                print("\t- - - - - - - - - - - - - - - - - - - -")
                
                # Ask user to confirm to save it or not
                confirm = input(color("\tDo you want to save these?", 'cyan') + color(" yes/no: ", 'purple'))
                
                # If user choose yes (to save them)
                # Save what user change and leave the others
                if str(confirm) == "yes" or str(confirm) == "Yes": 
                    if len(fullName): employees[(int(id) - 1)].set(1, fullName)
                    if len(salary): employees[(int(id) - 1)].set(2, salary)
                    if len(years): employees[(int(id) - 1)].set(3, years)
                    if len(manager): employees[(int(id) - 1)].set(4, int(manager))
                    os.system('cls')
                    print(color("\tData was saved successfuly!", 'green'))
                    
                # If user choose no or anything else
                else:
                    os.system('cls')
                    print(color("\tData was NOT saved!", 'red'))
                    
        # If id is not digit or empty
        else:
            os.system('cls')
            print(color("\tPlease enter correct id number!", 'red'))
            
        main()

    # Exit option 
    if int(option) == 5:
        os.system('cls')
        print(color("Thank you, see you later :D", 'yellow'))
        exit()
    
    # If user enterd anything
    else:
        os.system('cls')
        print(color("\n\t{} is not in options list!".format(option), 'red'))
        main()

# Create new object and insert it into empolyees array
def newEmp(fullName = default['fullName'], salary = default['salary'], years = default['years'], manager = default['MANAGER']):
    tempEmp = employee(fullName, salary, years, manager)

    # If there is error when create new object
    if tempEmp == 0:
        os.system('cls')
        print(color("\tThere is a problem"), 'red')
        main()

    # If there is NO error
    else:
        employees.append(tempEmp)
        os.system('cls')
        print(color("\tNew employee has been recorded successfuly!", 'green'))
        main()

# To reset employees array
def resetEmp():
    employees.clear()
    
    # If employess array is empty
    if len(employees) == 0:
        os.system('cls')
        # print(color("{} employee/s was deleted!".format(s), 'green'))
        print(color("Employees list is empty now!", 'green'))
        main()

    # If employees array is NOT empty
    else:
        os.system('cls')
        print(color("There is error in reset(), array len = {len(employees)}".format(len(employees))))
        main()

# program will start from here!
os.system('cls')
main()
