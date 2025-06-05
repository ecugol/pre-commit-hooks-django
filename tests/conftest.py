import subprocess

import pytest


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join("gits")
    subprocess.call(["git", "init", "--", str(git_dir)])
    yield git_dir


@pytest.fixture
def temp_git_detached_dir(tmpdir):
    git_dir = tmpdir.join("gits")
    subprocess.call(["git", "init", "--", str(git_dir)])
    subprocess.call(
        ["git", "commit", "--allow-empty", "-m", "initial commit"], cwd=git_dir
    )
    subprocess.call(["git", "checkout", "--detach"], cwd=git_dir)
    yield git_dir
