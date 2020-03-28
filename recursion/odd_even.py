def push_odd_to_end(s):
    def inner(s, start, end):
        if start < end:
            if s[start] % 2 == 1 and s[end] % 2 == 0:
                temp     = s[start]
                s[start] = s[end]
                s[end]   = temp
                inner(s, start + 1, end -1)
            elif s[start] % 2 == 1 and s[end] % 2 == 1:
                inner(s, start, end - 1)
            else:
                inner(s, start + 1, end)

    inner(s, 0, len(s) - 1)
    return s

if __name__ == "__main__":
    input1    = [3, 5, 7, 2, 4, 6]
    expected1 = [6, 4, 2, 7, 5, 3]
    actual1   = push_odd_to_end(input1)
    assert expected1 == actual1, f"Test failed for input {input1}"

    input2    = [1, 2, 3, 4, 5, 6, 7, 8]
    expected2 = []
    actual2   = push_odd_to_end(input2)
    assert expected2 == actual2, f"Test failed for input {input2}"
    print("Test passed")
