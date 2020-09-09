# Data Base Filler

There is 3 files with data for database.
Data stores in `.csv` format, where one line represents one row in database.

#### Structure: 

- `users.csv` --> username, password
- `questions.csv` --> question_id, question_text, author_id
- `answers.csv` --> answer_text, author_id, question_id

To fill database with that data you should run script: `load_data_db.py`.
