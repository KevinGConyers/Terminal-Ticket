#!/bin/bash
CUR=$(pwd)
cp "$CUR/.ttktconfig_example.json" "$HOME/.ttktconfig.json"
sudo pip install  -r requirements.txt
sudo pip install  -e .
