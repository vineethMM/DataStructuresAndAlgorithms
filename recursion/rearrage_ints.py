def rearrage_wrt_k(s, k):
    def swap(start, end):
        temp     = s[start]
        s[start] = s[end]
        s[end]   = temp

    def inner(start, end):
        if start < end:
            if s[start] == k == s[end]:
                inner(start, end - 1)
                return inner(start + 1, end)
            if s[start] > k:
                swap(start, end)
                return inner(start, end - 1)
            elif s[end] == k:
                return inner(start + 1, end)
            elif s[end] < k:
                swap(start, end)
                return inner(start + 1, end)
            else:
                return inner(start, end - 1)

        return (start, end)

    print(inner(0, len(s) - 1))
    return s


if __name__ == "__main__":
    input1    = [1, 2, 7, 8, 9, 5, 3]
    expected1 = [3, 1, 2, 5, 9, 8, 7]
    actual1   = rearrage_wrt_k(input1, 5)
    assert expected1 == actual1, f"Test failed for {input1}"

    input2    = [1, 2, 7, 8, 9, 5, 5, 3, 3]
    expected2 = [3, 1, 3, 2, 5, 5, 9, 8, 7]
    actual2   = rearrage_wrt_k(input2, 5)
    assert expected2 == actual2, f"Test failed for {input2}"

    input3    = [5, 2, 7, 8, 9, 5, 5, 3, 5]
    expected3 = [3, 2, 5, 5, 5, 5, 9, 7, 8]
    actual3   = rearrage_wrt_k(input3, 5)
    assert expected3 == actual3, f"Test failed for {input3}"

    input4    = [6, 2, 7, 8, 9, 5, 10]
    expected4 = [2, 5, 7, 8, 9, 10, 6]
    actual4   = rearrage_wrt_k(input4, 5)
    assert expected4 == actual4, f"Test failed for {input4}"
    print("Tests passed")
