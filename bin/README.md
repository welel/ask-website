Preferred execution order of scripts:

1. create_venv.sh		[the script creates virtual environment]
2. create_database.sh	[the script creates an user and a database, and gives permissions to the user]
3. mirgrations.sh		[the script makes migrations]
4. gunicorn_start.sh	[the script starts an application server]
5. nginx_start.sh		[the script starts a proxy server]

After execution these scripts you are ready to use the website.
Follow the link from your configuration if you changed it,
or default link: http://127.0.0.1:8000
