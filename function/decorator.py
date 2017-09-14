def print_arg_type(f):
    def ret_function(*args):
        for arg in args:
            print('%s type: %s'%(arg, type(arg)))
        return f(*args)
    return ret_function

@print_arg_type
def print_string(str):
    print('arg type:', type(str))
    print(str)

@print_arg_type
def print_int(i):
    print('arg type:', type(i))
    print(i)

print_string('abc')
# print_arg_type(print_string)('abc')
