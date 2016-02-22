#!/bin/bash -e

CONFIG_FILE = ../config.json

all: install serve

serve:
	echo "Starting Flask server..."
	python run.py

install: dependencies configure

dependencies:
	echo "Resolving Python dependencies..."
	pip install --upgrade -r requirements.txt

configure:
	echo "Configuring app..."
	python configure.py $(CONFIG_FILE)
	echo "Bootstrapping app..."
	python bootstrap.py $(CONFIG_FILE)

clean:
	echo "Deleting configuration file..."
	rm -f $(CONFIG_FILE)
