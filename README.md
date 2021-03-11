____
Installation steps if you want to try it out

```bash
git clone https://github.com/explorin-tech/portfolio-boilerplate.git
virtualenv -p python venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver # starts the server
```
---