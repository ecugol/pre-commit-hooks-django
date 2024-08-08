import subprocess

import pytest


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join("gits")
    subprocess.call(["git", "init", "--", str(git_dir)])
    yield git_dir
