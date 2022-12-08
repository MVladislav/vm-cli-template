#!/usr/bin/env bash
set -x

python3 -m mypy vm_edata_lht_nks --cache-dir ./scripts/logs/.mypy_cache
python3 -m black vm_edata_lht_nks --check
python3 -m isort --recursive --check-only vm_edata_lht_nks
python3 -m flake8 vm_edata_lht_nks --count --select=E9,F63,F7,F82 --show-source --statistics
python3 -m flake8 vm_edata_lht_nks --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
python3 -m pylint --rcfile=setup.cfg "$(find vm_edata_lht_nks -regextype egrep -regex '(.*.py)$')"
# python3 -m tox --workdir ./scripts/logs/.tox
