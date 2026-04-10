import pytest
from string_utils import (
    count_vowels, reverse_string, is_palindrome,
    word_count, capitalise_words, remove_duplicates
)

# ==================== Tests for count_vowels ====================

def test_count_vowels_basic():
    """Test count_vowels with normal input."""
    assert count_vowels("Hello") == 2


def test_count_vowels_all_vowels():
    """Test count_vowels with all vowels."""
    assert count_vowels("AEIOUaeiou") == 10


def test_count_vowels_no_vowels():
    """Test count_vowels with string containing no vowels."""
    assert count_vowels("bcdfg") == 0


def test_count_vowels_empty_string():
    """Edge case: empty string."""
    assert count_vowels("") == 0


def test_count_vowels_case_insensitive():
    """Edge case: case sensitivity check."""
    assert count_vowels("AbCdEfG") == 2  # A and E


def test_count_vowels_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        count_vowels(None)


# ==================== Tests for reverse_string ====================

def test_reverse_string_basic():
    """Test reverse_string with normal input."""
    assert reverse_string("abc") == "cba"


def test_reverse_string_single_character():
    """Edge case: single character."""
    assert reverse_string("a") == "a"


def test_reverse_string_empty_string():
    """Edge case: empty string."""
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    """Test reverse_string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_string_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        reverse_string(None)


# ==================== Tests for is_palindrome ====================

def test_is_palindrome_basic_true():
    """Test is_palindrome with a valid palindrome."""
    assert is_palindrome("racecar") is True


def test_is_palindrome_basic_false():
    """Test is_palindrome with a non-palindrome."""
    assert is_palindrome("hello") is False


def test_is_palindrome_with_spaces():
    """Test is_palindrome with spaces (ignores spaces)."""
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_case_insensitive():
    """Edge case: case sensitivity check."""
    assert is_palindrome("RaceCar") is True


def test_is_palindrome_single_character():
    """Edge case: single character is always a palindrome."""
    assert is_palindrome("a") is True


def test_is_palindrome_empty_string():
    """Edge case: empty string is a palindrome."""
    assert is_palindrome("") is True


def test_is_palindrome_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        is_palindrome(None)


# ==================== Tests for word_count ====================

def test_word_count_basic():
    """Test word_count with normal input."""
    assert word_count("Hello World") == 2


def test_word_count_single_word():
    """Test word_count with single word."""
    assert word_count("Hello") == 1


def test_word_count_multiple_spaces():
    """Edge case: multiple spaces between words."""
    assert word_count("  Hello    World  ") == 2


def test_word_count_empty_string():
    """Edge case: empty string."""
    assert word_count("") == 0


def test_word_count_only_spaces():
    """Edge case: string with only spaces."""
    assert word_count("     ") == 0


def test_word_count_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        word_count(None)


# ==================== Tests for capitalise_words ====================

def test_capitalise_words_basic():
    """Test capitalise_words with normal input."""
    assert capitalise_words("hello world") == "Hello World"


def test_capitalise_words_already_capitalised():
    """Test capitalise_words with already capitalised words."""
    assert capitalise_words("Hello World") == "Hello World"


def test_capitalise_words_mixed_case():
    """Test capitalise_words with mixed case input."""
    assert capitalise_words("hELLO wORLD") == "Hello World"


def test_capitalise_words_single_word():
    """Edge case: single word."""
    assert capitalise_words("hello") == "Hello"


def test_capitalise_words_empty_string():
    """Edge case: empty string."""
    assert capitalise_words("") == ""


def test_capitalise_words_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        capitalise_words(None)


# ==================== Tests for remove_duplicates ====================

def test_remove_duplicates_basic():
    """Test remove_duplicates with normal input."""
    assert remove_duplicates("aaabbbcc") == "abc"


def test_remove_duplicates_long_duplicates():
    """Edge case: consecutive duplicates of length > 3."""
    assert remove_duplicates("aaaabbbbcccc") == "abc"


def test_remove_duplicates_no_duplicates():
    """Test remove_duplicates with no consecutive duplicates."""
    assert remove_duplicates("abc") == "abc"


def test_remove_duplicates_single_character():
    """Edge case: single character repeated."""
    assert remove_duplicates("aaaaa") == "a"


def test_remove_duplicates_empty_string():
    """Edge case: empty string."""
    assert remove_duplicates("") == ""


def test_remove_duplicates_none_input():
    """Exception test: None input should raise TypeError."""
    with pytest.raises(TypeError, match="Input cannot be None"):
        remove_duplicates(None)

