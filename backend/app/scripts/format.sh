#!/bin/sh -e
set -x

isort .
yapf -r -i -p .
