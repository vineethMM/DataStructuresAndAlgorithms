from math import pow

digit = {
   '0' : 0,
   '1' : 1,
   '2' : 2,
   '3' : 3,
   '4' : 4,
   '5' : 5,
   '6' : 6,
   '7' : 7,
   '8' : 8,
   '9' : 9
}

def string_to_int(num_as_str):
    l = len(num_as_str)
    if l == 1:
        return digit[num_as_str]
    else:
        return pow(10, l - 1) * digit[num_as_str[0]] + string_to_int(num_as_str[1:])

if __name__ == "__main__":
    print("Test 1")
    res = string_to_int('123')
    print(f"Interger represenstation of 123 is {res} ")
