#!/bin/sh -e
set -x

python3 -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place vm_cli --exclude=__init__.py
python3 -m black vm_cli
python3 -m isort --src vm_cli .
