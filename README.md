# ezon-gpx

[![CI](https://github.com/uiolee/ezon-gpx/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/uiolee/ezon-gpx/actions/workflows/ci.yml)
[![Publish](https://github.com/uiolee/ezon-gpx/actions/workflows/publish.yml/badge.svg)](https://github.com/uiolee/ezon-gpx/actions/workflows/publish.yml)

## Feat

normalize Ezon gpx files.

- add location info to `wpt`.
- remove redundant empty points.
- delete invalid `ele` data.
- fix wrong timezone to UTC.

## Usage

[![PyPI - Version](https://img.shields.io/pypi/v/ezon-gpx)](https://pypi.org/p/ezon-gpx/#history)
[![PyPI - Status](https://img.shields.io/pypi/status/ezon-gpx)](https://pypi.org/p/ezon-gpx)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/ezon-gpx)](https://pypi.org/p/ezon-gpx)
[![PyPI - Format](https://img.shields.io/pypi/format/ezon-gpx)](https://pypi.org/p/ezon-gpx/#files)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/ezon-gpx)](https://pypi.org/p/ezon-gpx/#files)
[![PyPI - License](https://img.shields.io/pypi/l/ezon-gpx)](./LICENSE)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ezon-gpx)](https://pypi.org/p/ezon-gpx)

### Run with installation

```sh
uv tool install ezon-gpx
```

```sh
ezon-gpx -h
```

### Run without installation

```sh
uvx ezon-gpx -h
# uv tool run ezon-gpx -h
```

### Examples

```sh
ezon-gpx -d ./outdir/ --hour '-8' ./test/test.gpx
```
