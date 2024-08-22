# ------------------------------------------------------------------------------------------------- #
# Title: processing_classes
# # Description: Processing classes of a program to collect Employee rating data
# ChangeLog: (Who, When, What)
#   RRoot,1.5.2030,Created Script
#   Rebecca Bergh,8/15/2024,Split the main file into multiples
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee

# Constants -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

# Variables -------------------------------------------- #
employees: list = []  # a table of employee data


# Classes -------------------------------------------- #

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list[Employee]:
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RBergh,8/15/2024,Added reference to Employee object in parameters

        :type employee_type: Employee

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: a reference to the Employee class

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                file_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in file_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("JSON file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list[Employee]):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Rbergh,8/15/2024,Renamed temp var to file_data

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            file_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                file_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(file_data, file, indent=1)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
