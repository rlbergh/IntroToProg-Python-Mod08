# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes
# # Description: Test data classes of a program to collect Employee rating data
# ChangeLog: (Who, When, What)
#   RRoot,1.5.2030,Created Script
#   Rebecca Bergh,8/15/2024,Split the main file into multiples
# ------------------------------------------------------------------------------------------------- #

import json
from datetime import date

today = date.today()

value = "2024-08-18"

review_date = date.fromisoformat(value)

if review_date > today:
    print("The date cannot be in the future")
