def binary_op(numbers, comparator):
    def inner(numbers, begin, end):
        if begin == end:
            return numbers[begin]
        else:
            mid = (begin + end) // 2

            return comparator(
                inner(numbers, begin, mid),
                inner(numbers, mid + 1, end)
            )

    return inner(numbers, 0, len(numbers) - 1)


if __name__ == "__main__":
    print("Test 1")
    input1 = [1,2,3,4,5,6,7,8,9]
    max1 = binary_op(input1, max)
    min1 = binary_op(input1, min)
    print(f"Max of {input1} is : {max1}")
    print(f"Min of {input1} is : {min1}")


    print("Test 2")
    input2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    max2 = binary_op(input2, max)
    min2 = binary_op(input2, min)
    print(f"Max of {input2} is : {max2}")
    print(f"Min of {input2} is : {min2}")    
