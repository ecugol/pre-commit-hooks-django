from hooks.check_untracked_migrations import main
from hooks.utils import get_current_branch


def test_no_untracked_migrations(temp_git_dir):
    with temp_git_dir.as_cwd():
        migrations_dir = temp_git_dir.mkdir('app')
        migrations_dir.join('main.py').write("print('hello world')")
        assert main() == 0


def test_untracked_migrations(temp_git_dir):
    with temp_git_dir.as_cwd():
        migrations_dir = temp_git_dir.mkdir('app').mkdir('migrations')
        migrations_dir.join('0001_initial.py').write("print('hello world')")
        assert main() == 1


def test_running_on_correct_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        current_branch = get_current_branch()
        assert main(["--branches", current_branch, "some_other_branch"]) == 0


def test_running_on_incorrect_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        assert main(["--branches", "branch_one", "branch_two"]) == 1

