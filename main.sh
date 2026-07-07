#!/bin/bash
PYTHONPATH=src python -m pagio.main
cd public && python3 -m http.server 8888
