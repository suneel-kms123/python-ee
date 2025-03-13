.ONESHELL:

.DEFAULT_GO:= run

VENV:= venv

(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)
	chmod +x $(VENV)/Scripts/activate
	. ./$(VENV)/Scripts/activate
	./$(VENV)/Scripts/pip install -r requirements.txt

venv: $(VENV)/Scripts/activate

run: venv 
	venv/Scripts/python main.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: run clean