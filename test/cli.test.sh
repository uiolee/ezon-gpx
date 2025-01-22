#!/bin/bash

python --version
pipx --version
pipx run --python python"$python_version" --spec . ezon-gpx test
