import gspread
from google.oauth2.service_account import Credentials
import time
from datetime import datetime

"""
Load credentials for accessing the Google Sheets API
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BJJ quiz')


def validate_input(input_value):
    """
    Validates answers provided by the user.
    """
    valid_inputs = ['1', '2', '3', 'q']
    if input_value not in valid_inputs:
        raise ValueError('Invalid input! Select (1, 2, 3, or q)! Try again.')

    return input_value


def get_highest_score():
    """
    Get the highest score from the score sheet and display the column values.
    """
    print("Checking highest score...")
    score_worksheet = SHEET.worksheet("Score")

    """
    Get all the values from the score sheet
    """
    score_data = score_worksheet.get_all_values()

    highest_score = 0
    highest_score_rows = []

    """
     Iterate over the score data to find the highest score
    """
    for row in score_data[1:]:
        score = int(row[1])
        if score > highest_score:
            highest_score = score
            highest_score_rows = [row]
        elif score == highest_score:
            highest_score_rows.append(row)
        print("Highest Score so far is :")
        for row in highest_score_rows:
            name = row[0]
            score = row[1]
            timestamp = row[2]
            print(f"Score: {score}")
            print(f"Name: {name}")
            print(f"Timestamp: {timestamp}")
            print("---")
    
    
def update_score_worksheet(username, score):
    """
    Update score worksheet with the user's score, username, and timestamp
    """
    print("Updating score worksheet...\n")
    score_worksheet = SHEET.worksheet("Score")

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score_worksheet.append_row([username, score, timestamp])
    
    print("Result was saved successfully.\n")
    
    get_highest_score()
    
    # Append a new row with the username, score, and timestamp
    

def quiz():
    """
    Start the quiz and ask the questions.
    """
    
    questions_worksheet = SHEET.worksheet('Quiz Questions')
    
    # Open the worksheet containing the questions
    
    
    questions_data = questions_worksheet.get_all_values()[1:]
    # Read the questions, options, and answers from the worksheet

    score = 0
    total_questions = len(questions_data)
    question_index = 1

    for question_row in questions_data:
        question = question_row[0]
        options = [question_row[1], question_row[2], question_row[3]]
        correct_answer = int(question_row[4])

        print('----------------')
        print(question)
        print('[1] ' + options[0])
        print('[2] ' + options[1])
        print('[3] ' + options[2])
         
        while True:
            answer = input('Enter your answer (1, 2, 3) or press q to quit: ')
            print(f"User input: {answer}")

            try:
                validate_input(answer)
                if answer == 'q':
                    print('You Tapped out ')
                    return 
                break
            except ValueError as e:
                print(str(e))

        if int(answer) == correct_answer:
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')

        time.sleep(1)
        question_index += 1

    print('Quiz Complete!')
    print('----------------')
    print('Score: ' + str(score) + '/' + str(total_questions))

    save_score = input("Do you want to save your score? [y/n]: ")
    if save_score.lower() == "y":
        save_as = input("Save this score as: ")
        update_score_worksheet(save_as, score)


def restart():
    """
    Restart the quiz by calling the quiz function.
    """
    while True:
        quiz()

        play_again = input("Do you want to restart? [y/n]: ")
        if play_again.lower() != "y":
            return


print("Welcome to BJJ Quiz")
print("This is a quiz to check your knowledge on Brazilian Jiu Jitsu")
print("Select 1, 2, or 3 and press enter to proceed to the next question")

restart()
