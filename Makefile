
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval src/*.ipynb
	python -m pytest -vv --cov=src.lib

format:	
	black src/*.py 

lint:
	ruff check src/*.py
	nbqa ruff src/*.ipynb
		
all: install lint test format
