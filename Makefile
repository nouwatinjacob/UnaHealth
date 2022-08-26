PYTHON_MANAGE := python manage.py


makemigrations:
	$(PYTHON_MANAGE) makemigrations

migrate:
	$(PYTHON_MANAGE) migrate

runserver:
	$(PYTHON_MANAGE) runserver

seed_csv_data:
	$(PYTHON_MANAGE) user_creation_command && $(PYTHON_MANAGE) patient_readings

test:
	$(PYTHON_MANAGE) test