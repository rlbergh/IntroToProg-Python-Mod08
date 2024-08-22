# ------------------------------------------------------------------------------------------------- #
# Title: test_presentation_classes
# # Description: Test presentation classes of a program to collect Employee rating data
# ChangeLog: (Who, When, What)
#   RRoot,1.5.2030,Created Script
#   Rebecca Bergh,8/15/2024,Split the main file into multiples
# ------------------------------------------------------------------------------------------------- #

from datetime import date
from rich import print as rprint
from playsound3 import playsound3
from rich.console import Console

print(' ')

message = f' Rebecca Bergh\'s review of 4 from 2024-08-12 was saved.'
message_length = len(message)
print('╔'+('═' * message_length)+'══╗')
print('║ ' + message + ' ║')
print('╚'+('═' * message_length)+'══╝')

review_date = date.fromisoformat("2024-08-12")
today = date.today()
days_since_review: int = today - review_date
if days_since_review == 0:
    days_since_review_str = 'today'
elif days_since_review.days > 0:
    days_since_review_str = f'{days_since_review.days} days ago'

print(days_since_review_str)

rprint("Welcome to the Employee Ratings program for [bold]Best Company Ever[/bold]!")
rprint("Please wait while the menu loads...")
playsound3.playsound('intro-sound.mp3')

console = Console()
console.print("Welcome to the Employee Ratings program for [bold]Best Company Ever[/bold]!")
console.print("Use the [bold spring_green3]menu[/bold spring_green3] below to make a selection.")

wait = input('Please wait...')
