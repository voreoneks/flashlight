#!/bin/sh -e
set -x

isort app/main.py
isort app/
isort tests/

black app/main.py
black app/
black tests/