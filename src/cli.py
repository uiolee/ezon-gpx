import argparse
from os import listdir
from os.path import join, isdir

from main import convert


def cli():
    parser = argparse.ArgumentParser(prog="ezon-gpx")

    parser.add_argument(
        "path",
        nargs="+",
    )
    parser.add_argument("-o", "--out", help="the filename of output")
    parser.add_argument(
        "-d", "--dir", help="the dest dir of output", type=str, default="dist"
    )
    parser.add_argument("--hour", help="hour offset", type=int, default=-8)
    parser.add_argument(
        "--indent", help="output file with indent", type=bool, default=False
    )
    parser.add_argument("--strict", help="strict", type=bool, default=False)
    args = parser.parse_args()

    print()
    print("====== ezon-gpx cli ======")
    print(args)

    paths = []
    for path in args.path:
        if path.endswith(".gpx"):
            paths.append(path)
        elif isdir(path):
            for p in listdir(path):
                if p.endswith(".gpx"):
                    paths.append(join(path, p))

    for path in paths:
        print()
        print("[cli.py]", "processing", path)
        convert(path, args.out, args.dir, args.hour, args.indent, args.strict)

    print()
    print("[cli.py]", "processed files:", len(paths))
