# Ask

This is a question-and-answer website where questions are asked and answered by users .

<img src="details/header.png" alt="image-20200909182311345" />



# Dependencies

To successfully run the project, you need to install:

* [Python 3.6+](https://www.python.org/downloads/)
* [Django 3.1](https://www.djangoproject.com/download/)
* [python-dotenv 0.15](https://pypi.org/project/python-dotenv/)



# Running The Project

1. Clone or download the repository.

2. Go to `website-ask/ask` folder and run `feed_data_win.bat` script.

   The script makes migrations and feeds initial data to database. For Linux read `README.md` inside `websire/ask/data` folder.

3. Run Django server with command `manage.py runserver --insecure [port]`.

Now you can open the site by link `http://localhost:[port]/`.



# Directories

```
.
├── ...
├── ask				# Django project
│   ├── ask 			# Configuration package	
│   ├── core 			# Additional functions 
│   ├── data			# Initial data for database
│   ├── qa 			# Django application
│   ├── feed_data_win.bat 		# A script for data loading
└── ...
```



# About

The project was created for educational purposes. The project took its start in the course of [Web Technologies](https://stepik.org/course/154) from Mail.ru Group.

