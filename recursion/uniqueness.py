def is_uniquet_set(numbers):
    def not_in(n, seq, start, end):
        for i in range(start, end):
            if n == seq[i]:
                return False
        # if not match found abovem return True
        return True

    def inner(nums, start, end):
        if start >= end:
            return True
        else:
            # Check if the first element is unique
            first_is_unique = not_in(nums[start], nums, start + 1, end)
            # if the first element is unique, check for rest of the elements
            return  first_is_unique and inner(nums, start + 1, end)

    return inner(numbers, 0, len(numbers))

if __name__ == "__main__":
    assert is_uniquet_set([1, 2, 3]), "Test failedn for [1, 2, 3]"
    assert not is_uniquet_set([1, 2, 3, 3]), "Test failedn for [1, 2, 3, 3]"
