#!/usr/bin/env bash

set -e

PYTHONPATH=src python3 -m unittest discover \
    -s tests \
    -p "test_*.py"
