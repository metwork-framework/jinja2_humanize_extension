.PHONY: all develop install clean test

all:
	python setup.py build

develop:
	python setup.py develop

install:
	python setup.py install

clean:
	rm -Rf *.egg-info
	rm -Rf jinja2_humanize_extension/__pycache__
	rm -Rf tests/__pycache__
	rm -Rf .pytest_cache

test:
	flake8 --max-line-length 88 --ignore=D100,D101,D102,D103,D104,D107,D106,D105,W503,E203 jinja2_humanize_extension
	black --check jinja2_humanize_extension
	pylint --errors-only jinja2_humanize_extension
	pytest


black:
	black jinja2_humanize_extension
