import pytest
from string_utils import palindrome

@pytest.mark.parametrize("s", ["stats", "deified"])
def test_palindrome_true(s):
    assert palindrome(s)

@pytest.mark.parametrize("s", ["hello", "world"])
def test_palindrome_false(s):
    assert not palindrome(s)
