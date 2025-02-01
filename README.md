# getref
 # Referral Code System

## Description
> Questo progetto è un sistema di codici referral sviluppato con Django e Bootstrap, che permette agli utenti di generare e gestire codici referral per incentivare la condivisione e l'espansione della rete utente.

## Features
- **Registrazione e accesso degli utenti**
- **Generazione e gestione dei codici referral**
- **Tracciamento delle referenze e statistiche**
- **Dashboard interattiva per amministratori e utenti**
- **Supporto per settori e città multiple**

## Tech Stack
- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django, Python
- **Database:** MySQL
- **Version Control:** Git
- **Deployment:** PythonAnywhere

## Prerequisites
Assicurati di avere questi strumenti installati:
- Python 3.x
- pip
- MySQL

## Installation
### Create Env (on PythonAnywhere)
```bash
python -m venv /home/getcall/.virtualenvs/getcall.pythonanywhere.com
source /home/getcall/.virtualenvs/getcall.pythonanywhere.com/bin/activate
```
### Clean Cache and Temporany folder (on on PythonAnywhere)
```bash
rm -rf /home/getcall/.cache/*
rm -rf /home/getcall/tmp/*

```
### Cheeck file log (on on PythonAnywhere)
```bash
ls -lh /home/getcall/logs

```
### Cheeck Space after cleaning (on on PythonAnywhere)
```bash
df -h
```
### Find Big Files (on on PythonAnywhere)
```bash
find /home/getcall -type f -size +50M -exec ls -lh {} \;
```
### Create Env
```bash
python -m venv env
env\scripts\activate
pip install -r requirements.txt
```
## Create Migrations
```bash
python manage.py makemigrations referral
python manage.py makemigrations affiliate
python manage.py makemigrations dashboard
python manage.py migrate
python manage.py collectstatic
```
## Populate Cities and Sectors
```bash
python manage.py populate_cities
python manage.py populate_sectors
python manage.py populate_cities
python manage.py populate_sectors
```
## Start Web-Project
```bash
env\scripts\activate
python manage.py runserver
```

```bash
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'Questa è una mail di test.',
    settings.EMAIL_HOST_USER,  # Mittente
    ['<email>@gmail.com'],  # Destinatario
    fail_silently=False,
)
```

## Usage
Registra un nuovo utente.

Accedi con le credenziali create.

Genera un codice referral dal dashboard utente.

Condividi il codice referral con amici e familiari.

Monitora le referenze e le statistiche dal tuo dashboard.

## Contributing
Accettiamo contributi da parte di chiunque sia interessato a migliorare questo progetto. Segui questi passaggi per contribuire:

## Forka il repository.

# Crea un nuovo branch con una descrizione significativa:

```bash
git checkout -b feature/my-new-feature
```

# Commit delle modifiche: 

```bash
git commit -m 'Add some feature'
```

# Push al branch:
```bash
git push origin feature/my-new-feature
```
# Apri una Pull Request.

## License
Questo progetto è distribuito sotto la licenza MIT. Vedi il file LICENSE per i dettagli.

## Acknowledgements
Grazie a tutti i contributori.

## Ringraziamenti speciali a AnySolution.

## Contact
Se hai domande o suggerimenti, puoi contattarmi a info@getcall.it o attraverso https://www.linkedin.com/company/anysolution-it.

## Connect with me
<p align="left"> </p>

## Languages and Tools
<p align="left"><a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>