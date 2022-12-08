#!/bin/sh -e
set -x

python3 -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place vm_edata_lht_nks --exclude=__init__.py
python3 -m black vm_edata_lht_nks
python3 -m isort --recursive --apply vm_edata_lht_nks
