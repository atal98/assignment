## Installation setup

Fetch git respo.

```bash
  git clone --fetch-all https://github.com/atal98/assignment.git
```

create python enviroment

```bash
  python -m venv {your_env_name}
```

create a db in postgresql and create name .env file and put your creds in that file
![](/img/img1.png)

```bash
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME={your_db_name}
  DB_USER=postgres
  DB_PASSWORD={your_password}
  DB_HOST=localhost
  DB_PORT=5432
```

Activate your env

```bash
  .\{your_name_env}\Scripts\activate
```

Install all packages

```bash
  pip install -r .\requirements.txt
```

Save and Execuate models into db

```bash
  python manage.py makemigrations

  python manage.py migrate
```

Create superuser for to create authentication and Tokenization

```bash
  python manage.py createsuperuser

  -- add name as admin
  -- add password and email

```

Generate token for that user

```bash
  python manage.py drf_crate_token admin
```

Start server

```bash
  python manage.py runserver
```

To test any api first fetch generated token by hit this url

```bash
  http://127.0.0.1:8000/api/token/
```

Open postman go to header and put there

![](/img/img2.png)
