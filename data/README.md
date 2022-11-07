# Data for the site

There is 3 files with data for database.
Data stores in **json** format, where one dict of list represents one row in database.

#### Examples: 

​	User:

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

​	Question:

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

​	Answer:

```json
    {
        "model": "qa.answer",
        "pk": 243,
        "fields": {
            "text": "There are a variety of reasons for getting a tattoo. You can ... time.",
            "added_at": "2020-12-29T10:14:26.857Z",
            "question": 123845,
            "author": 1012
        }
    }
```



To fill database with that data you should feed it to **manage.py** with commands (consider the order of commands):

```cmd
python manage.py loaddata data/users.json
python manage.py loaddata data/questions.json
python manage.py loaddata data/answers.json
```

