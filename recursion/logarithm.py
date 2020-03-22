def integer_logarithm(n):
    '''Returns the integer part of logarithm of `n` to the base 2'''
    if n < 2:
        return 0
    else:
        return 1 + integer_logarithm(n // 2)

if __name__ == "__main__":
    print("Test 1")
    print(f"Log of 10 to the base 2 is: {integer_logarithm(10)}")    
