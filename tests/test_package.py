import pytest

from ya_dancer import __version__


@pytest.mark.package
def test_package_version():
    assert isinstance(__version__, str)
