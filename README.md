# ezon-gpx

converter for Ezon gpx file.

## Feat

convert Ezon gpx files

- add location info to `wpt`.
- delete empty point.
- fix timezone to UTC.

## Usage

### Source

#### Python

see [./src/main.py](./src/main.py#L141)

#### CLI

```bash
./src/cli.py test/test.gpx [path]
```

```bash
./src/cli.py --help
```

## Develop Env

```plain
Python 3.11.8
```
