def towers_of_hanoi(source, temp, target, n):
    if n == 1:
        # when the number of disks is 1, move it to target
        target.append(source.pop())
    else:
        # move n-1 disks from `source` to `temp` so that we can expose
        # n'th disk, for this process use `target`as `temporary storage`
        towers_of_hanoi(source, target, temp, n - 1)

        # n'th disk is exposed, move it to target
        target.append(source.pop())

        # Now move n-1 disks from `temp` to `target`,
        # use `source` as temporary storage
        towers_of_hanoi(temp, source, target, n - 1)

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    b = []
    c = []
    towers_of_hanoi(a, b, c, 5)

    assert a == [] and b == [] and c == [5, 4, 3, 2, 1]
