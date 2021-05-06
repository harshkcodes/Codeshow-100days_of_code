bases = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hex": 16,
    "hexadecimal": 16
}

default = 10


def verify_base(x):
   
    try:
        return int(x)
    except:
        if x in bases:
            return bases[x]
        else:
            return default


def decimal_value(x):
    if(x >= '0' and x <= '9'):
        return int(x)
    elif(x >= 'a' and x <= 'z'):
        return int(ord(x) - ord('a') + 10)
    elif(x >= 'A' and x <= 'Z'):
        return int(ord(x) - ord('A') + 10)
    else:
        # Error
        raise Exception('Number not valid for: ', x)


def to_special_caracter(x):
    if(x >= 0 and x <= 9):
        return str(x)
    elif(x > 9):
        return chr(ord('a') + x - 10)
    else:
        raise Exception('Not valid negative number in converter: ', x)


def convert(n, from_base, to_base):
 
    n = str(n)
    from_base = verify_base(from_base)
    to_base = verify_base(to_base)

    if(n == "0"):
        return n

    if(n[0] == '-'):
        n = n[1:]
        negative = True
    else:
        negative = False

    multi = 1
    decimal_number = 0
    if(from_base == 10):
        decimal_number = int(n)
    else:
        for i in range(len(n) - 1, -1, -1):
            decimal_number += (multi * decimal_value(n[i]))
            multi *= from_base

    if(to_base == 10):
        decimal_number = str(decimal_number)
        if(negative):
            decimal_number = '-' + decimal_number

        return decimal_number

    result = ""

    while(decimal_number > 0):
        value = decimal_number % to_base
        result = to_special_caracter(value) + result
        decimal_number = int((decimal_number - value)/to_base)

    if(negative):
            result = '-' + result

    return result


def test_convert():
    print(convert("1111000111", 2, 8) == "1707")
    print(convert("1111000111", 2, 10) == "967")
    print(convert("1111000111", 2, 16) == "3c7")
    print(convert("1234567", 8, 2) == "1010011100101110111")
    print(convert("1234567", 8, 10) == "342391")
    print(convert("1234567", 8, 16) == "53977")
    print(convert("987123", 10, 2) == "11110000111111110011")
    print(convert("987123", 10, 8) == "3607763")
    print(convert("987123", 10, 16) == "f0ff3")
    print(convert("abcdef", 16, 2) == "101010111100110111101111")
    print(convert("abcdef", 16, 8) == "52746757")
    print(convert("abcdef", 16, 10) == "11259375")

    print(convert("179", 10, 16) == "b3")
    print(convert("b3", 16, 10) == "179")

    print("Negative Tests")
    print(convert("-179", 10, 16) == "-b3")
    print(convert("-b3", 16, 10) == "-179")
    print(convert("-1111000111", 2, 10) == "-967")

test_convert()
