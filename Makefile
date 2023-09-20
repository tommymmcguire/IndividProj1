install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval 
	python -m pytest -vv --cov

format:	
	black *.py

lint:
	ruff check *.py
	nbqa ruff *.ipynb
		
all: install lint test format
