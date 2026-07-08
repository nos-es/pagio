#!/bin/bash
PYTHONPATH=src python -m pagio.main
cd docs && python3 -m http.server 8888
