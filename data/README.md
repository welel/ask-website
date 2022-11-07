# Data for the website

There are 3 files with data for the database.
Data stores in **json** format, where one object represents one row in the database.

# Data overview:

## User object:

```json
{
        "model": "auth.user",
        "pk": 1032,
        "fields": {
            "password": "PrettyGardenPrettyGardenPrettyGarden",
            "username": "PrettyGarden"
        }
}
```

## Question object:

```json
    {
        "model": "qa.question",
        "pk": 123845,
        "fields": {
            "text": "What is the point of a tattoo?",
            "added_at": "2020-12-29T10:14:26.857Z",
            "author": 1031
        }
    }
```

## Answer object:

```json
    {
        "model": "qa.answer",
        "pk": 243,
        "fields": {
            "text": "There are a variety of reasons for ...",
            "added_at": "2020-12-29T10:14:26.857Z",
            "question": 123845,
            "author": 1012
        }
    }
```

# Data loading

To fill the database with that data, you should run a script `load_data.sh` or do it manually.
Feed it to **manage.py** with commands (consider the order of commands):

```cmd
python manage.py loaddata data/users.json
python manage.py loaddata data/questions.json
python manage.py loaddata data/answers.json
```
