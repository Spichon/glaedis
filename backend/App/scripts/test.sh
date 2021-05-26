#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=.

python ./app/tests_pre_start.py

pytest --cov-report term --cov=investpy app/tests
