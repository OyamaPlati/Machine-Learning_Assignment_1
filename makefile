
PYTHON = python

.PHONY = help install venv run clean

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make install"
	@echo "To setup the environment type make venv"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"

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
