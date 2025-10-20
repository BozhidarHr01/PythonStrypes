def is_palindrome(chars):
    if len(chars) <= 1:
        return True

    if chars[0] == chars[-1]:
        return is_palindrome(chars[1:-1])
    return False

print(is_palindrome("abba"))