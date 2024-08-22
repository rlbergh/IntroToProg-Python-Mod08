# ------------------------------------------------------------------------------------------------- #
# Title: main
# # Description: Main code of a program to collect Employee rating data
# ChangeLog: (Who, When, What)
#   RRoot,1.5.2030,Created Script
#   Rebecca Bergh,8/15/2024,Split the file into multiples and import functions/modules
#   Rebecca Bergh,8/20/2024,Fixed "cannot find variable" message with Kelly's help
#   Rebecca Bergh,8/21/2024,Added more sounds
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor, FILE_NAME, employees
from presentation_classes import IO, EXIT_MSG, MENU, WELCOME
from playsound3 import playsound


employees = FileProcessor.read_employee_data_from_file(
    file_name=FILE_NAME,
    employee_data=employees,
    employee_type=Employee)  # Note this is the class name (ignore the warning)

# Beginning of the main body of this script

# Welcome messagev
print(WELCOME)
playsound('intro-sound.mp3')

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    e = None  # establish e variable before try
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Enter new employee data
        try:
            employees = IO.input_employee_data(
                employee_data=employees,
                employee_type=Employee
            )  # Note this is the class name (ignore the warning)
        except Exception as e:
            IO.output_error_messages(e)

        continue
    elif menu_choice == "2":  # show current employee data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(
                file_name=FILE_NAME,
                employee_data=employees
            )
            print(f"Data was saved to the {FILE_NAME} file.")
            playsound('success2.mp3')
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

print(EXIT_MSG)
playsound("bells-exit.mp3")
