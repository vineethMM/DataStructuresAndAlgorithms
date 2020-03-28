def quick_sort(s):
    def swap(i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

    def arrange_pivot(start, end, pivot):
        # Re-arrage the elements in `s` so that  elements less or equal to
        # `pivot` will come before pivot and elements greater of equal to `pivot`
        # comes after pivot.(If the pivot element is present more than ones,
        # we only care about one occurance of it, other occurance can be before
        # or after it).
        # s1 <= pivot <= s2
        # both s1 and s2 can have elements equal to `pivot`
        if start < end:
            if s[start] > pivot:
                swap(start, end)
                return arrange_pivot(start, end - 1, pivot)
            elif s[end] < pivot:
                swap(start, end)
                return arrange_pivot(start + 1, end, pivot)
            elif s[start] == pivot:
                return arrange_pivot(start, end - 1, pivot)
            else:
                return arrange_pivot(start + 1, end, pivot)

        return start

    def inner(start, end):
        if start < end:
            # choosing the last element as pivot, find its position
            pivot_index = arrange_pivot(start, end, s[end])
            # recursively sort 
            inner(start, pivot_index - 1)
            inner(pivot_index + 1, end)

    inner(0, len(s) - 1)
    return s

if __name__ == "__main__":
    in1 = [1, 2, 3, 4, 5, 6]
    assert quick_sort(in1) == [1, 2, 3, 4, 5, 6], f"Test failed for {in1}"
    in2 = [6, 5, 4, 3, 2, 1]
    assert quick_sort(in2) == [1, 2, 3, 4, 5, 6], f"Test failed for {in2}"
    in3 = [3, 42, 8, 1,9, 19, 3, 3]
    assert quick_sort(in3) == [1, 3, 3, 3, 8, 9, 19, 42], f"Test failed for input {in3}"
    print("Tests passed")
