import argparse
import re
from typing import Optional
from typing import Sequence

from .utils import get_current_branch
from .utils import get_untracked_files


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--branches", nargs="*", help="Choose which branches to work on"
    )
    args = parser.parse_args(argv)
    current_branch = get_current_branch()
    if args.branches and current_branch not in args.branches:
        print(f"{current_branch} is not present in --branches arg")
        return 1
    found = False
    for filename in get_untracked_files():
        if re.match(r".*/migrations/.*\.py", filename):
            found = True
            print(f"Untracked migration file found: {filename}")
    if found:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
