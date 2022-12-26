#this type of file de commands automatically
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input #generate the static files folder
python manage.py migrate #do migrations