import sys

sys.path.append("./")  # noqa: E402
from modules.dummy import dummy  # isort:skip  # noqa: E402


def test_dummy():
    assert dummy()
