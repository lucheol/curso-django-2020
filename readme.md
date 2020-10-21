# Comandos utilizados

- Instalar os pacotes:

`pip install -r requirements.txt`

- Criar um projeto do Django:

`django-admin startproject proj .`

- Executar o servidor:

`python manage.py runserver`

- Configurar o runserver para rodar/debug direto pelo Pycharm.

- Criar um novo app:

`django-admin startapp cadastros`

- Criar as migrações para serem executadas no BD:

`python manage.py makemigrations`

- Executar as alterações no BD:

`python manage.py migrate`

- Criar um superusuário:

`python manage.py createsuperuser`


- Configurar o pycharm para rodar o python console com suporte ao django:

```
import sys, os, django
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()
```

- Instalar o ipython (para um console mais poderoso): `pip install ipython`


Para leitura
=============

 - https://12factor.net/pt_br/
 - https://wiki.python.org.br/GuiaDeEstilo
