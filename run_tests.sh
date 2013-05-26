#!/usr/bin/env sh
coverage run --source=api.py tests.py
coverage report -m
