PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip

.PHONY: tests clean  

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt

# TODO run all tests not just models
tests: .venv requirements-dev.txt
	${VENV_PIP} install -r requirements-dev.txt
	${VENV_PYTHON} -m pytest tests/test_models.py -s

clean:
	rm -rf .venv
	docker-compose down && docker volume rm rocket-labs-challenge_dbdata
