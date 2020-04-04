.PHONY: format test

format:
	poetry run black splatool2-buki-roulette tests

test:
	poetry run pytest
	poetry run mypy splatool2-buki-roulette tests
	poetry run pylint splatool2-buki-roulette tests
