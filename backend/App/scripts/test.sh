#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=.

python ./app/tests_pre_start.py

#pytest --cov=app --cov-report=term-missing app/tests "${@}"
