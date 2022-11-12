# Backend for AV website and application

## Development

Project is being developed in Python and as such it requires Python virtual environment to be set up for development. 

It's recommended to use the newest Python 3.11, but 3.10 would work as well.  

🔧 Clone project repository:
```shell
$ git clone git@github.com:vkh-cr/av-backend.git
```

🔧 Switch to project directory: 
```bash
$ cd av-backend/av_backend
```

🔧 Create virtual environment. Here, Python 3 module `venv` is used, but you may use anything else to create environment (`virtualenv` package, `virtualenvwrapper`, `pipenv`, `PyCharm` integration etc.):
```shell
$ python -m venv --prompt av_backend .venv
```

🔧 Activate virtual environment:
```shell
$ . .venv/bin/activate

# Check Python
(av_backend) $ python -V
Python 3.11.x  # or Python 3.10.x

$ which python
/directory/with/project/avecko/av_backend/.venv/bin/python 
```

🔧 In virtual environment, install dev requirements and the project itself in dev mode:  
```shell
(av_backend) $ pip install -r requirements.dev.txt 
(av_backend) $ pip install -e . 
```

🔧 Check that Django project is initialised correctly and `manage.py` works:
```shell
(av_backend) $ ./manage.py --help 
```

The project is now installed in development mode in your virtual environment. Several initial configuration choices have been made:
* default DB is SQLite (but runs with PostgreSQL in production)

🔧 Run all DB migrations to initialise tables and such. You'll need to run this command again in the future when there are some new DB schema or data migrations: 
```shell
(av_backend) $ ./manage.py migrate
```

🔧 Create superuser as a first user of your system: 
```shell
(av_backend) $ ./manage.py createsuperuser
```

🔧 Run local development server: 
```shell
(av_backend) $ ./manage.py runserver
```

```shell
# Response
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 12, 2022 - 11:05:57
Django version 4.1.2, using settings 'av_backend.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The project is now set up and running. It's available on the URL you can find in the response of `runserver` command. Copy the URL in your browser. Project is available:
* http://127.0.0.1:8000/ - frontend
* http://127.0.0.1:8000/admin/ - administration