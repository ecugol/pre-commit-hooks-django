import argparse
import tempfile
import shutil
from contextlib import closing
from typing import Optional
from typing import Sequence


LOCATION_START = "#: "
FILE = "file"
NEVER = "never"


def _extract_location_file_name(line):
    file_names = line.rstrip().replace(LOCATION_START, "").split(" ")
    return sorted({n.split(":")[0] for n in file_names})


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to process")
    parser.add_argument("--add-location", choices=[FILE, NEVER], required=True)
    args = parser.parse_args(argv)
    add_location = args.add_location
    for filename in args.filenames:
        with tempfile.NamedTemporaryFile() as temp_file:
            with closing(open(filename, "r")) as source_file:
                location = set()
                for line in source_file:
                    print(line)
                    if line.startswith(LOCATION_START):
                        if add_location == FILE:
                            location.update(_extract_location_file_name(line))
                    else:
                        if add_location == FILE:
                            for name in sorted(location):
                                temp_file.write(f"{LOCATION_START}{name}\n".encode())
                            location = set()
                        temp_file.write(line.encode())
            temp_file.seek(0)
            shutil.copyfile(temp_file.name, filename)
    return 1


if __name__ == "__main__":
    exit(main())
