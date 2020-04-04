.PHONY: format test

format:
	poetry run black splatoon2_buki_roulette tests

test:
	poetry run pytest
	poetry run mypy splatoon2_buki_roulette tests
	poetry run pylint splatoon2_buki_roulette tests
