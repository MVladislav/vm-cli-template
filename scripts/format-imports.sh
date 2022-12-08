#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
python3 -m isort --recursive --force-single-line-imports --apply vm_edata_lht_nks
sh ./scripts/format.sh
