def multiply(m, n):
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)

if __name__ == "__main__":
    assert multiply(10, 2) == 20, "Test failed for 10 * 2"
