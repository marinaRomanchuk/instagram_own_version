# instagram_own_version

A simplified version of Instagram with the ability to add posts,
set likes or dislikes, follow other people and view your own page.

## Running the project locally

1. Clone the repository with git clone [url]. Like that
```
    $ git clone https://github.com/marinaRomanchuk/instagram_own_version.git
```

2. Ensure that you have
[Poetry](https://python-poetry.org/docs/) available.
After that, you should:

Install the requirements of the project template by running
    ```
    poetry install
    ```

Activate the virtualenv created by _poetry_:
    ```
    poetry shell
    ```

3. Create a new PostgreSQL database. For this, I’m assuming you
already have pgAdmin and postgres installed. Apologies for the
lack of detail here.

In terminal:
```
   $ sudo -u postgres psql

   =# CREATE DATABASE instagram_project;

   =# CREATE USER admin WITH PASSWORD 'admin';

   =# ALTER USER admin SUPERUSER;

   =# GRANT ALL PRIVILEGES ON DATABASE "instagram_project" to admin;
```

If you have created user with another parameters, change dict DATABASES in file settings.py.

4. Make your migrations

```
    $ python manage.py migrate
```

5. Create a new superuser

```
    $ python manage.py createsuperuser
```

6. To run the project make in terminal
```
   $ python3 manage.py runserver
```

## Tests
To run tests make in terminal

```
    $ python3 manage.py test
```
