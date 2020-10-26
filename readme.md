# Comandos utilizados

- Instalar os pacotes:

`pip install -r requirements.txt`

- Criar um projeto do Django:

`django-admin startproject proj .`

- Executar o servidor:

`python manage.py runserver --settings=proj.settings_dev`

- Configurar o runserver para rodar/debug direto pelo Pycharm.

- Criar um novo app:

`django-admin startapp cadastros`

- Criar as migrações para serem executadas no BD:

`python manage.py makemigrations --settings=proj.settings_dev`

- Executar as alterações no BD:

`python manage.py migrate --settings=proj.settings_dev`

- Criar um superusuário:

`python manage.py createsuperuser --settings=proj.settings_dev`


- Configurar o pycharm para rodar o python console com suporte ao django:

```
import sys, os, django
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings_dev")
django.setup()
```

- Instalar o ipython (para um console mais poderoso): `pip install ipython`

- Utilizar o proxy para dar build na imagem:

```
docker build -t sidia/local:1.0 --build-arg http_proxy=http://PROXY_IP:PROXY_PORT --build-arg https_proxy=http://PROXY_IP:PROXY_PORT .
docker image pull mdillon/postgis (+proxy)
docker image ls
```

Para leitura
===

 - https://12factor.net/pt_br/
 - https://wiki.python.org.br/GuiaDeEstilo
 
 
Atividade
===

Desenvolvimento de um sistema de ticket.

- (ADMIN) O usuário do sistema pode pegar o ticket para si. Ao fazer isso, registrar uma interação, colocar o ticket em ANDAMENTO e avisar o cliente por email.
- (ADMIN) O usuário pode enviar uma resposta ao cliente, registrando a resposta na interação e enviando por email ao cliente.
- (ADMIN) O usuário poderá cancelar ou finalizar o ticket, informando um motivo/resolução. Registrar Interação e enviar email.
- (FRONT) O cliente poderá acessar uma área do ticket onde verá o histórico e poderá enviar uma resposta/mensagem.
- (API) Disponibilizar informações do chamado via API.

- Dicas: actions do admin, signals..


