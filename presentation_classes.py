# ------------------------------------------------------------------------------------------------- #
# Title: presentation_classes
# # Description: Presentation classes of a program to collect Employee rating data
# ChangeLog: (Who, When, What)
#   RRoot,1.5.2030,Created Script
#   Rebecca Bergh,8/15/2024,Split the main file into multiples
#   Rebecca Bergh,8/16/2024,Created the print_confirmation function
#   Rebecca Bergh,8/17/2024,Created sort employees function

# ------------------------------------------------------------------------------------------------- #

from datetime import date
from data_classes import Employee
from rich.console import Console
from playsound3 import playsound

# Constants -------------------------------------------- #
MENU: str = '''
╔═════ Employee Ratings ════════════════════╗
║  Select from the following menu:          ║
║    1. Enter new employee rating data.     ║
║    2. Show current employee rating data.  ║
║    3. Save data to a file.                ║
║    4. Exit the program.                   ║
╚═══════════════════════════════════════════╝
'''
EXIT_MSG: str = '''

    ╔════════════════ « ♦ » ═══╗
          Closing program...    
    ╚═══ « ♦ » ════════════════╝ 
'''

WELCOME: str = '''
\t\t█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\t\t▌  Welcome to the Employee Ratings app      ▐
\t\t▌  for the Best Company Ever, LLC           ▐
\t\t▌               « ∙∙∙∙∙ »                   ▐
\t\t▌   Please wait while the menu loads...     ▐
\t\t▌              ♪ audio on ♪                 ▐
\t\t█═════════╤═══════════════════════╤═════════█
\t\t          ├———————————————————————┤
'''

# Variables -------------------------------------------- #
menu_choice = ''


# Classes -------------------------------------------- #

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            message = error.__doc__
            print("-- Technical Error Message -- ")
            print(error, message, type(error), sep='\n')
            playsound('error.mp3')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param: string to display menu
        :return: None
        """
        console = Console()
        print()
        console.print("[bold bright_white]" + menu + "[/bold bright_white]")
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list[Employee]):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        message: str = ''
        sorted_employees = IO.sort_employees(employee_data)
        print()
        print("-" * 16 + " Sorted by rating " + "-" * 16)

        for employee in sorted_employees:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"

            print(message.format(employee.first_name,
                                 employee.last_name,
                                 employee.review_date,
                                 employee.review_rating))
        print("-" * 50)
        print()

    @staticmethod
    def sort_employees(employee_data: list[Employee]) -> list[Employee]:
        """
        Function sorts the employee data by rating, in descending order

        ChangeLog: (Who, When, What)
        Rbergh,8.17.2024,Created function

        :param employee_data: list of Employee objects
        :return: sorted employee data
        """
        return sorted(employee_data, key=lambda employee: employee.review_rating, reverse=True)

    @staticmethod
    def input_employee_data(employee_data: list[Employee], employee_type: Employee) -> list[Employee]:
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of dictionary rows to be filled with input data
        :param employee_type: Employee objects

        :return: list
        """
        e = None  # Initializing e before the try
        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)
            IO.print_confirmation(employee_object)
        except ValueError as e:
            IO.output_error_messages("Something went wrong with the data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error.", e)

        return employee_data

    @staticmethod
    def print_confirmation(employee_type: Employee):
        """
        This function creates a message to the end user to confirm an employee's rating was added to the data,
        and it converts the rating to a string value, and calculates how long ago their review was

        ChangeLog: (Who, When, What)
        Rbergh,8.16.2024,Created function

        :param employee_type: Employee object
        :return: None
        """
        console = Console()
        print(' ')
        employee_object = employee_type
        # string version of rating
        if employee_object.review_rating == 5:
            rating_str = "(Leading)"
        elif employee_object.review_rating == 4:
            rating_str = "(Strong)"
        elif employee_object.review_rating == 3:
            rating_str = "(Solid)"
        elif employee_object.review_rating == 2:
            rating_str = "(Building)"
        elif employee_object.review_rating == 1:
            rating_str = "(Not Meeting Expectations)"
        # days since review date
        today = date.today()
        days_since_review = today - date.fromisoformat(employee_object.review_date)
        if days_since_review == 0:
            days_since_review_str = 'today'
        elif days_since_review.days > 0:
            days_since_review_str = f'{days_since_review.days} days ago'
        # A fancy message in a box
        message = f'{employee_object.first_name} {employee_object.last_name}\'s review of \
{employee_object.review_rating} {rating_str} from {days_since_review_str} was saved.'
        # find the length of the message by itself
        message_length = len(message)
        # creates a box the size of the message
        console.print('╔' + ('═' * message_length) + '══╗', style="cyan")
        console.print('[cyan]║ [/cyan]' + '[magenta]' + message + '[/magenta]' + '[cyan] ║[/cyan]')
        console.print('╚' + ('═' * message_length) + '══╝', style="cyan")
        playsound('success.mp3')
