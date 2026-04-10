def count_vowels(text: str) -> int:
    """Returns the count of vowel characters (a, e, i, o, u - case-insensitive)."""
    if text is None:
        raise TypeError("Input cannot be None")
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def reverse_string(text: str) -> str:
    """Returns the string with all characters in reversed order."""
    if text is None:
        raise TypeError("Input cannot be None")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Returns True if text reads the same forwards and backwards (case-insensitive, ignoring spaces)."""
    if text is None:
        raise TypeError("Input cannot be None")
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    """Returns the number of words in text. Words are separated by whitespace."""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text.strip():
        return 0
    return len(text.split())


def capitalise_words(text: str) -> str:
    """Returns text with the first letter of each word capitalised and the rest lowercase."""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text.strip():
        return ""
    return ' '.join(word.capitalize() for word in text.split())


def remove_duplicates(text: str) -> str:
    """Returns text with consecutive duplicate characters removed (preserves first occurrence)."""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text:
        return ""
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)
