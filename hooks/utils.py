import subprocess
from typing import List

UNTRACKED_CMD = ["git", "ls-files", "--others", "--exclude-standard"]
BRANCH_CMD = ["git", "symbolic-ref", "--short", "HEAD"]


def get_untracked_files() -> List[str]:
    output = subprocess.check_output(UNTRACKED_CMD)
    return output.decode().split("\n")


def get_current_branch() -> str:
    result = subprocess.run(BRANCH_CMD, stdout=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode().rstrip()
    return None
