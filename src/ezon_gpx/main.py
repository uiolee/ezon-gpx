import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from os.path import join, basename, exists, dirname
from os import makedirs

NAMESPACE = "{http://www.topografix.com/GPX/1/1}"
N = NAMESPACE


def _p(v):
    return N + str(v)


def _f(s: str):
    return sep.join([_p(x) for x in s.split(sep) if x]) if (sep := "//") in s else _p(s)


def convert(
    gpx_path: str,
    out: str = "",
    outDir: str = ".",
    hour_offset=-8,
    indent: bool = False,
    strict: bool = False,
):
    def wpt_has_loc():
        return "lat" in wpt.attrib and "lon" in wpt.attrib

    def get_first_point():
        pot = trkpts[0]
        return {
            "lat": pot.get("lat"),
            "lon": pot.get("lon"),
            "time": pot.find(_f("time")).text,
        }

    def set_loc_for_wpt():
        def _set():
            lat, lon = pot["lat"], pot["lon"]
            print("INFO:", "set wpt's location to first point's.", lat, lon)
            wpt.set("lat", lat)
            wpt.set("lon", lon)

        pot = get_first_point()
        if wpt_time.text == pot["time"]:
            _set()
        else:
            print("WARN:", "first point's time not equals to wpt's")
            if not strict:
                _set()

    def delete_zero_point():
        trkseg = root.findall(_f("trk//trkseg"))[0]
        for z in zeropts:
            trkseg.remove(z)

    def convert_tz():
        def _set(time_elem):
            a = datetime.fromisoformat(time_elem.text) + timedelta(hours=hour_offset)
            time_elem.text = a.strftime("%Y-%m-%dT%H:%M:%SZ")

        _set(wpt_time)

        for elem in trkpts:
            _set(elem.find(_f("time")))

        print("INFO:", "fix timezone:", wpt_time.text)

    print()
    print("INFO: start parse: ", gpx_path)
    gpx_name = basename(gpx_path)
    ET.register_namespace("", N[1:-1])
    tree = ET.parse(gpx_path)
    root = tree.getroot()

    creator = root.get("creator") or ""
    if strict and ("ezon" not in creator):
        err = "It looks like this gpx was not created by ezon"
        print("WARN:", err)
        raise Exception(err)

    wpt = root.findall(_f("wpt"))[0]
    wpt_time = wpt.find(_f("time"))
    trkpts = root.findall(_f("trk//trkseg//trkpt"))
    zeropts = root.findall(_f("trk//trkseg//trkpt[@lat='0.0']"))
    num_trk = len(trkpts)
    num_zero = len(zeropts)

    print(
        "INFO:",
        "name: {}".format(root.find(_f("trk//name")).text),
        "creator: {}".format(creator),
        "start: {}".format(wpt_time.text or ""),
        "pkts: {}".format(num_trk),
        "zero: {}".format(num_zero),
        sep="\n  ",
    )

    if not wpt_has_loc():
        print("INFO:", "Missing location in 'wpt'")
        set_loc_for_wpt()

    if num_zero:
        delete_zero_point()
        print("INFO:", "deleted zero points:", num_zero)

    trkpts = root.findall(_f("trk//trkseg//trkpt"))
    num_trk2 = len(trkpts)

    print(
        "INFO:",
        "trkpts:",
        num_trk,
        "-->",
        num_trk2,
        "({})".format(num_trk2 - num_trk),
    )

    convert_tz()

    if indent:
        ET.indent(tree, space=" " * 4)

    if (not out) and outDir == ".":
        out = ".".join((ls := gpx_name.split(".")).insert(-1, "output") or ls)
    else:
        out = gpx_name

    path = join(outDir, out)
    if not exists((dir := dirname(path))):
        makedirs(dir)

    tree.write(path, "utf-8", xml_declaration=True, short_empty_elements=False)
    print(
        "INFO:",
        "output gpx file {} indent: {}".format("with" if indent else "without", path),
    )


if __name__ == "__main__":
    convert("test/test.gpx", outDir="dist", indent=True)
