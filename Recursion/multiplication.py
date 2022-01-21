def multiplication(a,b):

    if b == 0:
        return 0

    smalleroutput = multiplication(a,b-1)
    return smalleroutput + b

print(multiplication(3,5))
