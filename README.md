# BJJ QUIZ

## Introduction

This is a simple quiz application that tests your knowledge of Brazilian Jiu Jitsu (BJJ). The application is implemented in Python and interacts with the Google Sheets API to store and retrieve quiz questions and scores.

A live version of the game can be found [here](https://bjjquiz.herokuapp.com/).



## Features

- Multiple-choice quiz questions: The quiz consists of a set of questions related to BJJ, with three possible answers for each question.
- Answer validation: User input is validated to ensure that only valid answers are accepted.
- Highest score tracking: The application keeps track of the highest score achieved and displays it to the user.
- Score saving: Users have the option to save their scores, including their name and timestamp, to a Google Sheets document.
- Restart functionality: After completing the quiz, users can choose to restart and play the quiz again.



## How to use 

- Follow the instructions provided on the console to answer the quiz questions. Enter the corresponding number (1, 2, or 3) for your answer and press Enter. If you want to quit the quiz, enter 'q' and press Enter.

- At the end of the quiz, you will have the option to save your score. Enter 'y' to save your score and provide a name for the score entry.

- The application will display the highest score recorded in the "Score" worksheet, along with the corresponding name and timestamp.


## Testing

I performed manual testing continuously as the application was being developed.

- Verify that the quiz questions are displayed correctly.
- Test user input validation to handle incorrect input (e.g., entering a non-numeric value).
- Test the score calculation to ensure that it accurately reflects the user's performance.
- Check if the user is prompted to save their score at the end of the quiz.
- Test the restart functionality to ensure that the quiz can be played again.



## Technologies Used
The BJJ Quiz application utilizes the following technologies:
- Python: The core programming language used to develop the application.
- Heroku: A cloud platform that enables deployment and hosting of the application.
- GitHub: A version control platform used for code repository and collaboration.
- Codeanywhere: An online integrated development environment (IDE) used for code editing and tutering 
- gspread: A Python library for accessing the Google Sheets API.
- oauth2client: A Python library for handling OAuth 2.0 authentication.




## Credits

- love sandwiches walkthrough project 
- GitHub Python Template 
- Heroku deployment instructions from Code Institute
