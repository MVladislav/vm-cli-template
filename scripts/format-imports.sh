#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
python3 -m isort --recursive --force-single-line-imports --apply vm_cli
sh ./scripts/format.sh
