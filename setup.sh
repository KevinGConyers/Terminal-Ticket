#!/bin/bash
CUR=$(pwd)
cp "$CUR/.ttktconfig_example.json" "$HOME/.ttktconfig.json"
sudo $CUR/install.sh
