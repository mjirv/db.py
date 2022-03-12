#!/bin/bash

python -m unittest discover db/tests/
pandoc -f markdown -t rst README.md > README.rst
python setup.py sdist bdist_wheel && python3 -m twine upload dist/*
