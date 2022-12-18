#!/bin/sh -e
set -x

flake8 app/main.py
flake8 app/

black app/main.py --check
black app/ --check