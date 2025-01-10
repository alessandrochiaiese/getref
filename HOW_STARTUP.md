python -m venv env
env\scripts\activate
pip install -r requirements.txt


python manage.py makemigrations referral
python manage.py makemigrations affiliate
python manage.py makemigrations dashboard
python manage.py migrate

python manage.py collectstatic

python manage.py populate_cities
python manage.py populate_sectors



env\scripts\activate
python manage.py runserver

