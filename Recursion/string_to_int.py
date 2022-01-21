def str_to_int(str):
    if (len(str) == 1):
        return ord(str[0]) - ord('0')

    y = str_to_int(str[1:])
    x = ord(str[0]) - ord('0')
    x = x * (10**(len(str) - 1)) + y;
    return int(x)

a = '1245'
print(str_to_int(a))
