#!/bin/bash
CUR=$(pwd)
cp "$CUR/.ttktconfig_example.json" "$HOME/.ttktconfig.json"
pip install --user -r requirements.txt
pip install --user -e .
