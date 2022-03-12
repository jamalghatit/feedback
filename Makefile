initial:
	python manage.py makemigrations --merge --noinput
	python manage.py makemigrations
	python manage.py migrate