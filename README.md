# Ask

This is a question-and-answer website where questions are asked and answered by users.

<img src="details/header.png" alt="image-20200909182311345" />


# Running The Project

1. Clone or download the repository.

2. Create virtual environment and install requirements from `requirements.txt`.

3. Make migrations and migrate.

4. Go to `scripts/` folder and run `load_data.sh` script.

   The script feeds initial data from `data/` to sqlite database.

5. Run Django server with command `python manage.py runserver`.

Now you can open the site by link `http://127.0.0.1:8000/`.



# Directories

```
.
├── ask/			# Django project
│   ├── ask/			# Configuration package	
│   ├── core/ 			# Additional functions 
│   └── qa/ 		   # Django application
├── data/			# Initial data for database
├── scripts/		# Scripts for a project
└── ...
```


# About

The project was created for educational purposes. The project took its start in a course [Web Technologies](https://stepik.org/course/154) made by Mail.ru Group.
