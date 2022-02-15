import random
import string
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


def random_string(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def random_number(min: int = 1, max: int = 100) -> int:
    return random.randint(min, max)


class XMLData:
    def __init__(self, xml: ET.Element):
        self._xml = xml

    @classmethod
    def generate(cls) -> "XMLData":
        root = ET.Element("root")

        var_id = ET.Element("var", name="id", value=random_string())
        var_level = ET.Element("var", name="level", value=str(random_number()))

        objects = ET.Element("objects")

        for _ in range(random_number(max=10)):
            objects.append(ET.Element("object", name=random_string()))

        root.append(var_id)
        root.append(var_level)
        root.append(objects)

        return cls(root)

    def to_bytes(self) -> bytes:
        xml_str = ET.tostring(self._xml, encoding="utf-8", method="xml")
        return xml_str.decode(encoding="utf-8")


def main():
    
    out_path = Path("./zipfiles")
    out_path.mkdir(parents=True, exist_ok=True)

    for i in range(1, 51):
        zipfile_path = out_path.joinpath(f"{i}.zip")

        with ZipFile(zipfile_path, mode="w") as zf:
            for fname_id in range(100):
                xml_data = XMLData.generate()
                zf.writestr(f"{fname_id}.xml", xml_data.to_bytes())


if __name__ == "__main__":
    main()
