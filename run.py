import gspread
from google.oauth2.service_account import Credentials
import time


# Load credentials for accessing the Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BJJ quiz')

# Open the worksheet containing the questions
questions_worksheet = SHEET.worksheet('Quiz Questions')

# Read the questions, options, and answers from the worksheet
questions_data = questions_worksheet.get_all_values()

questions_data = questions_data[1:]


def validate_input(input_value):
    """
    Validates answers provided by the user.
    """
    valid_inputs = ['1', '2', '3']
    if input_value not in valid_inputs:
        raise ValueError('Please select a valid option (1, 2, or 3)!')

    return input_value


def quiz():
    """
    Start the quiz and ask the questions.
    """
    score = 0
    total_questions = len(questions_data)
    question_index = 1

    for question_row in questions_data:
        question = question_row[0]
        options = [question_row[1], question_row[2], question_row[3]]
        correct_answer = int(question_row[4])

        print('----------------')
        print(question)
        print('1) ' + options[0])
        print('2) ' + options[1])
        print('3) ' + options[2])

        while True:
            answer = input('Enter your answer (1, 2, or 3): ')
            print(f"User input: {answer}")

            try:
                validate_input(answer)
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
    input('Press any key to exit: ')


quiz()
