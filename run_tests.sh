#!/usr/bin/env sh
coverage run --source=api.py --branch tests.py
coverage report -m
