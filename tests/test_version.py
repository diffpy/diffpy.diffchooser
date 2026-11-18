"""Unit tests for __version__.py."""

import diffpy.diffchooser  # noqa


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(diffpy.diffchooser, "__version__")
    assert diffpy.diffchooser.__version__ != "0.0.0"
