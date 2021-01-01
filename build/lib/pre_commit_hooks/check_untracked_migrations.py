import argparse
import re
import subprocess
from typing import List
from typing import Optional
from typing import Sequence

CMD = ["git", "ls-files", "--others", "--exclude-standard"]


def _get_untracked_files() -> List[str]:
    output = subprocess.check_output(CMD)
    return output.decode().split("\n")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Files to check")
    found = False
    for filename in _get_untracked_files():
        if re.match(r".*/migrations/.*\.py", filename):
            found = True
            print(f"Untracked migration file found: {filename}")
    if found:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
