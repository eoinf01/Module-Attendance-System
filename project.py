from datetime import date
divider = "-------------------"


def login():
    username = input("Username:")
    password = input("Password:")
    username_list = []
    password_list = []
    login_status = ""
    login_data = open("login_data.txt", "r")  # open login_data file and declare as variable
    for name in login_data:
        name = name.rstrip("\n")  # remove any newlines
        line_info = name.split(",")  # split into two list's when there is a comma
        username_list.append(line_info[0])
        password_list.append(line_info[1])
    for x in range(len(username_list)):   # for loop to loop through contents of lists to see if they match the input
        if username == username_list[x]:
            if password == password_list[x]:
                print(f"Welcome {username_list[x]}! ")
                login_status = "success"
            elif password != password_list[x]:
                login_status = "failure"
    return login_status




def load_modules_list():
    module_list = open("modules.txt", 'r')
    modules = []
    module_code = []
    for module_name in module_list:
        module_name = module_name.rstrip("\n")
        modulesnew = module_name.split(",")
        module_code.append(modulesnew[0])
        modules.append(modulesnew[1])
    for x in range(len(modules)):
        print(f"{x + 1}. {module_code[x]} - {modules[x]}")
    option = input(">")
    for x in range(len(modules)):
        if option == str(modules.index(modules[x]) + 1):
            number = modules.index(modules[x])
            module_code = module_code[number]
            return module_code


def get_class_attendance(module_code):
    module_file = open(f"{module_code}.txt", 'r')
    names_list = []
    present_list = []
    absent_list = []
    excuse_list = []
    for name in module_file:  # for loop used to read each line and split into different lists and assign to lists
        name = name.rstrip("\n")
        list1 = name.split(",")
        names_list.append(list1[0])
        present_list.append(list1[1])
        absent_list.append(list1[2])
        excuse_list.append(list1[3])
    return module_code, names_list, present_list, absent_list, excuse_list


def update_class_data(module_code, names_list, present_list, absent_list, excuse_list):
    updated_file = open(f"{module_code}.txt", 'w')  # open file in write mode to change values
    for x in range(len(names_list)):  # for loop to write new values to updated file
        updated_file.write(names_list[x] + ',')
        updated_file.write(str(present_list[x]) + ',')
        updated_file.write(str(absent_list[x]) + ',')
        updated_file.write(str(excuse_list[x]) + '\n')
    updated_file.close()


def take_class_attendance(module_code, names_list, present_list, absent_list, excuse_list):
    print(f"Module Record System(Attendance) - {module_code}\n{divider}")
    print(f"There are {len(names_list)} enrolled.")
    for x in range(len(names_list)):  # for loop to run through each student and take attendance
        print(f"Student #{x + 1}: {names_list[x]}")
        print(f"1. Present \n2. Absent\n 3. Excused")
        option = input(">")
        if option == '1':  # if statements used to increase values of attendance when one of three options selected
            present_list[x] = int(present_list[x]) + 1
        if option == '2':
            absent_list[x] = int(absent_list[x]) + 1
        if option == '3':
            excuse_list[x] = int(excuse_list[x]) + 1
    return module_code, names_list, present_list, absent_list, excuse_list


def calculate_total_days(present_list, absent_list, excuse_list):
    total_days = int(present_list[0]) + int(absent_list[0]) + int(excuse_list[0])
    return total_days


def calculate_attendance_rate(present_list, absent_list, excuse_list):
    attendance_rates_list = []
    for x in range(len(present_list)):
        if int(present_list[x]) > 7:
            attendance_rates_list.append(int(present_list[x]))
        elif (int(present_list[x]) < 7) & (int(present_list[x]) > 0):
            attendance_rates_list.append(int(present_list[x]))
        elif int(present_list[x]) == 0:
            attendance_rates_list.append(int(present_list[x]))
    return attendance_rates_list


def generate_and_save_stats(module_code, names_list, present_list, absent_list, excuse_list):
    attendance_rate = calculate_attendance_rate(present_list, absent_list, excuse_list)
    total_days = calculate_total_days(present_list, absent_list, excuse_list)  # getting a value from other function
    average_attendance = sum(attendance_rate) / len(attendance_rate)
    new_file = open(f"{module_code}-{date.today()}.txt", 'w')  # used imported date module to include todays date in file name
    print(f"Module: {module_code}\n", file=new_file)
    print(f"Number of Students: {len(names_list)}\n", file=new_file)
    print(f"Number of Classes: {total_days}\n", file=new_file)
    print(f"Average Attendance: {average_attendance} days\n", file=new_file)
    for x in range(len(attendance_rate)):  # attendance rate calculation
        if attendance_rate[x] / 13 * 100 < 70:
            if attendance_rate[x] / 13 * 100 > 0:
                print(f"Low Attender(s): under 70.0% \n {names_list[x]}\n", file=new_file)
        if attendance_rate[x] / 13.0 * 100.0 > 70:
            print(f"Best Attender(s): \n Attended {present_list[x]}/{total_days} \n {names_list[x]}\n", file=new_file)
        if attendance_rate[x] == 0:
            print(f"Non Attender(s): {names_list[x]}\n", file=new_file)
    new_file.close()
    file_output = open(f"{module_code}-{date.today()}.txt", 'r')
    print(file_output.read())  # read the file we just write to the screen for the user to see


def main():

    login_status = login()
    while True:
        if login_status == 'success':
            print("1.Record Attendance")
            print("2.Generate Statistics")
            print("3.Exit")
            option = input(">")
            if option == '1':
                module_code = load_modules_list()
                module_code, names_list, present_list, absent_list, excuse_list = get_class_attendance(module_code)
                module_code1, names_list1, present_list1, absent_list1, excuse_list1 = take_class_attendance(module_code, names_list, present_list, absent_list, excuse_list)
                update_class_data(module_code1, names_list1, present_list1, absent_list1, excuse_list1)
            if option == '2':
                module_code = load_modules_list()
                module_code, names_list, present_list, absent_list, excuse_list = get_class_attendance(module_code)
                calculate_total_days(present_list, absent_list, excuse_list)
                calculate_attendance_rate(present_list, absent_list, excuse_list)
                generate_and_save_stats(module_code, names_list, present_list, absent_list, excuse_list)
            if option == '3':
                break
        else:
            print("Module Record System - Login Failed")
            break


main()
