def nth_harmonic(n):
    ''' Find the nth harmonic number'''
    if n == 1:
        return 1
    else:
        return (1 / n) + nth_harmonic(n - 1)


if __name__ == "__main__":
    print("Test 1")
    print(f"3rd harmonic number is {nth_harmonic(3)}")
    print("\nTest 2")
    print(f"9th harmonic number is {nth_harmonic(9)}")
