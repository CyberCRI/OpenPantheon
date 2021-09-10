#!/usr/bin/env bash

set -x

mypy app

MYPY_EXIT_CODE=$?

flake8 app

exit $(( $? + $MYPY_EXIT_CODE ))
