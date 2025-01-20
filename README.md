# getref
 
## HOW TO START
# Create Env
python -m venv env
env\scripts\activate
pip install -r requirements.txt

# Create Migrations
python manage.py makemigrations referral
python manage.py makemigrations affiliate
python manage.py makemigrations dashboard
python manage.py migrate

python manage.py collectstatic

# Populate Cities and Sectors
python manage.py populate_cities
python manage.py populate_sectors


# Start Web-Project
env\scripts\activate
python manage.py runserver

