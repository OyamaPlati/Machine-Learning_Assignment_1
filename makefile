
PYTHON = python3

.PHONY = help setup install venv run clean

FILES = input output

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

setup:
	
	@echo "Checking if project files are generated..."
	[ -d project_files.project ] || (echo "No directory found, generating..." && mkdir project_files.project)
	for FILE in ${FILES}; do \
		touch "project_files.project/$${FILE}.txt"; \
	done

install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv:
	test -d venv || python3 -m venv venv
	
run:
	${PYTHON} kmeans_clustering.py

clean:
	rm -rf *.project
	rm -rf venv
	find -iname "*.pyc" -delete
