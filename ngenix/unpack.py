import csv
import multiprocessing as mp
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile


@dataclass
class XmlResult:
    id: str
    level: int
    objects: list[str]


def parse_xml(f) -> "XmlResult":
    tree = ET.ElementTree()
    tree.parse(f)

    id = tree.find("./var[@name='id']").attrib.get("value")
    level = tree.find("./var[@name='level']").attrib.get("value")
    objects = [el.attrib.get("name") for el in tree.findall("./objects/object")]

    return XmlResult(id, level, objects)


def process_file(filepath: Path) -> list[XmlResult]:
    xml_results = []

    with ZipFile(filepath, "r") as zf:
        for name in zf.namelist():
            with zf.open(name) as f:
                xml_result = parse_xml(f)
                xml_results.append(xml_result)

    return xml_results


def main():
    pool = mp.Pool(mp.cpu_count())

    results = []
    in_path = Path("./zipfiles")

    for f in in_path.glob("**/*.zip"):
        result = pool.apply_async(process_file, (f,))
        results.append(result)

    with (
        open("levels.csv", "w", newline="") as csvlevels,
        open("objects.csv", "w", newline="") as csvobjects,
    ):

        levels_writer = csv.DictWriter(csvlevels, fieldnames=["id", "level"])
        objects_writer = csv.DictWriter(csvobjects, fieldnames=["id", "object_name"])

        levels_writer.writeheader()
        objects_writer.writeheader()

        for result in results:
            for chunk in result.get():
                levels_writer.writerow({"id": chunk.id, "level": chunk.level})
                objects_writer.writerows(
                    {"id": chunk.id, "object_name": object} for object in chunk.objects
                )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
