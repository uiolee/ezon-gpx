# ezon-gpx

[![CI](https://github.com/uiolee/ezon-gpx/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/uiolee/ezon-gpx/actions/workflows/ci.yml)
[![Publish](https://github.com/uiolee/ezon-gpx/actions/workflows/publish.yml/badge.svg)](https://github.com/uiolee/ezon-gpx/actions/workflows/publish.yml)

converter for Ezon gpx file.

## Feat

convert Ezon gpx files

- add location info to `wpt`.
- delete empty point.
- fix timezone to UTC.

## Usage

![PyPI - Version](https://img.shields.io/pypi/v/ezon-gpx)
![PyPI - Status](https://img.shields.io/pypi/status/ezon-gpx)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/ezon-gpx)
![PyPI - Format](https://img.shields.io/pypi/format/ezon-gpx)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ezon-gpx)
![PyPI - License](https://img.shields.io/pypi/l/ezon-gpx)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ezon-gpx)

### pipx

#### Install

```bash
pipx install ezon-gpx
```

####

```bash
ezon-gpx -h
```

### source

#### Python

see [./src/main.py](./src/main.py#L141) for more.

#### CLI

```bash
./src/cli.py --help
```

see [./src/cli.py](./src/cli.py) for more.

## Develop Env

```plain
Python 3.11.8
```
