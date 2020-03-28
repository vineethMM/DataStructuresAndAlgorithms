def has_more_vowels(in_str):
    length     = len(in_str)
    vowels     = ['a', 'e', 'i', 'o', 'u']
    consonants = [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
        'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    ]

    def inner(in_str, index, v, c):
        if index < length:
            if in_str[index] in vowels:
                v = v + 1
            if in_str[index] in consonants:
                c = c + 1

            return inner(in_str, index + 1, v, c)
        else:
            return (v, c)

    (v, c) = inner(in_str, 0, 0, 0)
    return v > c


if __name__ == "__main__":
    input1 = "aeioudfghjklmn"
    input2 = "aeiou"
    assert not has_more_vowels(input1), f"Test failed for input {input1}"
    assert has_more_vowels(input2), f"Test failed for input {input2}"
    print("Test passed")
