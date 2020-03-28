def merge_sort(s):
    def merge(s1, s2, s):
        j = k = 0
        while j + k < len(s):
            jk_inrange = j < len(s1) and k < len(s2)

            if (jk_inrange and s1[j] < s2[k]) or (not jk_inrange and j < len(s1)):
                s[j + k] = s1[j]
                j += 1
            else:
                s[j + k] = s2[k]
                k += 1

        return s

    def sort(s):
        if(len(s)) > 1:
            n = len(s) // 2
            return merge(sort(s[0:n]), sort(s[n:]), [None] * len(s))
        else:
            return s

    return sort(s)


if __name__ == "__main__":
    input1   = [5, 4, 4, 3, 1, 2]
    expected = [1, 2, 3, 4, 4, 5]
    actual   = merge_sort(input1)
    assert expected == actual, f"Test failed for input {input1}"
    print("Test passed")
