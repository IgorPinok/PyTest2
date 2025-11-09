from string_utils import palindrome

def test_palindrome():
    assert palindrome("stats")
    assert palindrome("deified")
    assert not palindrome("hello")
    assert not palindrome("world")