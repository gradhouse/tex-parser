# File: test_version.py
# Description: Unit tests for the versioning of the tex_parser package.
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

def test_version():
    """Test that the package version is correctly set."""
    import tex_parser
    assert tex_parser.__version__ == "0.1.0"
