import pytest


def test_fail_at_import():
    from maybeissue.poc import poc
    poc()