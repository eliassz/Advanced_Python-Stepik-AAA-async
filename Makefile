init:
	python3 -m pip install poetry
	poetry install --no-root

test:
	poetry run pytest -sv homework/tests
