# Backend for AV website and application

TODO: Description

## Development

Project is being developed in Python and as such it requires Python virtual environment to be set up for development. 

It's recommended to use the newest Python 3.11, but 3.10 will work as well.  

🔧 Clone project repository:
```shell
$ git clone git@github.com:vkh-cr/ave.git
```

🔧 Switch to project directory: 
```bash
$ cd ave/ave
```

🔧 Create virtual environment. Here, Python 3 module `venv` is used, but you may use anything else to create environment (`virtualenv` package, `virtualenvwrapper`, `pipenv`, `PyCharm` integration etc.):
```shell
$ python -m venv --prompt ave .venv
```

🔧 Activate virtual environment:
```shell
$ . .venv/bin/activate

# Check Python
(ave) $ python -V
Python 3.11.x  # or Python 3.10.x

$ which python
/directory/with/project/ave/.venv/bin/python 
```

🔧 In virtual environment, install dev requirements and the project itself in dev mode:  
```shell
(ave) $ pip install -r requirements.dev.txt 
(ave) $ pip install -e . 
```

🔧 Check that Django project is initialised correctly and `manage.py` works:
```shell
(ave) $ ./manage.py --help 
```

The project is now installed in development mode in your virtual environment. Several initial configuration choices have been made:
* default DB is SQLite (but runs with PostgreSQL in production)

🔧 Run all DB migrations to initialise tables and such. You'll need to run this command again in the future when there are some new DB schema or data migrations: 
```shell
(ave) $ ./manage.py migrate
```

🔧 Create superuser as a first user of your system: 
```shell
(ave) $ ./manage.py createsuperuser
```

🔧 Run local development server: 
```shell
(ave) $ ./manage.py runserver
```

```shell
# Response
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 12, 2022 - 11:05:57
Django version 4.1.2, using settings 'ave.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The project is now set up and running. It's available on the URL you can find in the response of `runserver` command. Copy the URL in your browser. Project is available:
* http://127.0.0.1:8000/ - frontend
* http://127.0.0.1:8000/admin/ - administration