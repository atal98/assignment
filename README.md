## Installation setup

create a folder open that directory in vscode by write in directory

```bash
  cmd

  -- in terminal
  code .
```

vscode will write in terminal to fetch git clone

```bash
  git clone https://github.com/atal98/assignment.git
```

write in that vscose termial

```bash
  cd .\assignment\

  -- open that directory in vscode terminal
  code.
```

create python enviroment

```bash
  python -m venv {your_env_name}
```

create a db in postgresql and add that creds in django setting.py file

```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name_of_your_db',
        'USER': 'name_of_your_user',
        'PASSWORD': 'name_of_your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
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
  python manage.py drf_create_token admin
```

Start server

```bash
  python manage.py runserver
```

## Testing API

To test any api first fetch generated token by hit this url

```bash
  http://127.0.0.1:8000/api/token/
```

Open postman go to header and put there

![](/img/img2.png)

First need to create vendor profile

```bash
  http://localhost:8000/api/vendors/
```

![](/img/img3.png)

Then create PO

```bash
  http://localhost:8000/api/purchase_orders/
```

![](/img/img4.png)

acknowlage the PO

```bash
  http://localhost:8000/api/purchase_orders/1/acknowledge/
```

![](/img/img5.png)

check the vendor get update or not as Signals are create whenever PO update or delete

```bash
  http://localhost:8000/api/vendors/
```

![](/img/img6.png)

update the PO status to complete

```bash
  http://localhost:8000/api/purchase_orders/1/
```

![](/img/img7.png)

As the result beacuse of the signals created it update dynamically

```bash
  http://localhost:8000/api/vendors/
```

![](/img/img8.png)
