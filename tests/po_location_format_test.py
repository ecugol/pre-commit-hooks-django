import pytest

from hooks.po_location_format import main
from hooks.utils import get_current_branch


INPUT_PO_DATA = """
#: foo/bar.py:123 foo/bar.py:200
#: foo/foo.py:123
msgid "Foo"
msgstr "Bar"

#: foo/bar.py:123 foo/bar.py:200
#: foo/foo.py:123
msgid "Bar"
msgstr "Foo"
"""

FILE_PO_DATA = """
#: foo/bar.py
#: foo/foo.py
msgid "Foo"
msgstr "Bar"

#: foo/bar.py
#: foo/foo.py
msgid "Bar"
msgstr "Foo"
"""

NEVER_PO_DATA = """
msgid "Foo"
msgstr "Bar"

msgid "Bar"
msgstr "Foo"
"""


@pytest.mark.parametrize(
    "input_data,output_data,add_location",
    [(INPUT_PO_DATA, FILE_PO_DATA, "file"), (INPUT_PO_DATA, NEVER_PO_DATA, "never")],
)
def test_output_is_correct(input_data, output_data, add_location, tmpdir):
    with tmpdir.as_cwd():
        in_file = tmpdir.join(f"in_{add_location}.po")
        in_file.write_text(INPUT_PO_DATA, encoding="utf-8")
        assert main([str(in_file), "--add-location", add_location]) == 1
        with in_file.open() as f:
            assert output_data == f.read()
