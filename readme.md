# Django To-Do List Project

This is Django To-Do List App installation process.

## Installation

First of clone this [repository](https://github.com/AARdacca/To-Do.git) and make sure migration folder has only "__init__" named file, all pycache folder needs to be deleted if it is there, db.sqlite3 should be deleted from root.

```powershell
git clone https://github.com/AARdacca/To-Do.git
```
Then
```powershell 
cd To-Do
```

Secondly install and upgrade pip.
```powershell
python -m pip install --upgrade pip
```
Make sure to install virtualenv

```powershell
pip install virtualenv
```

Then create virtual environment

```powershell
python -m venv env
```

Then activate the env

```powershell
.\env\Scripts\activate
```

At the 6th step, install the requirements

```powershell
pip install -r requirements.txt
```

Now ready the migrations

```powershell
python manage.py makemigrations
```

Now migrate

```powershell
python manage.py migrate
```

Now Runserver

```powershell
python manage.py runserver
```

Now click the link [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

[//]: <> (## License)