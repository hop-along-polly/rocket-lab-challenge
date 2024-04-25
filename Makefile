PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt

seed-db: .venv
	${VENV_PYTHON} seeder/seed.py seeder/seedData.json

clean:
	rm -rf .venv
	docker volume rm rocket-labs-challenge_dbdata
