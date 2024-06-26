# ezon-gpx

converter for Ezon gpx file.

## Feat

convert Ezon gpx files

- add location info to `wpt`.
- delete empty point.
- fix timezone to UTC.

## Usage

### Python

see [./main.py](./main.py#L141)

### CLI

```bash
./cli.py test/test.gpx [path]
```

```bash
./cli.py --help
```

## Develop Env

```plain
Python 3.11.8
```
