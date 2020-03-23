def is_palindrome(s):
    def inner(s, start, end):
        if(start <= end):
            return (s[start] == s[end]) and inner(s, start + 1, end - 1)
        else:
            return True

    return inner(s, 0, len(s) - 1)


if __name__ == "__main__":
    assert is_palindrome("aba")
    assert is_palindrome("malayalam")
    assert not is_palindrome("abcs")
    print("Test passsed")
