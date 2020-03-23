def reverse_str(in_str):
    in_list = list(in_str)

    def inner(list, start, end):
        if start < end:
            temp        = list[start]
            list[start] = list[end]
            list[end]   = temp
            return inner(in_list, start + 1, end - 1)
        else:
            return list


    return "".join(inner(in_list, 0, len(in_list) - 1))


if __name__ == "__main__":
    input    = "abcde"
    expected = "edcba"
    actual   = reverse_str(input)

    assert expected == actual, f"Test failed for input {input}"
    print("Test passed")
