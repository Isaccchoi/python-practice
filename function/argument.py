def multiplication(*args):
    multiple = 1
    if len(args) >=2:
        for arg in args:
            multiple *= arg
    else:
        multiple = args[0]**2

    print( multiple)


multiplication(3)
multiplication(3,5)
