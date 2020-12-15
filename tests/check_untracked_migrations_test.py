from pre_commit_hooks.check_untracked_migrations import main


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
