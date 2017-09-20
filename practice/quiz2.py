@mydecorator
def mymax(*args):
    result = args[0]
    try:
        for i in args:
            if result < i:
                result = i
        return result
    except:
        print("Invalid arguments")


def mydecorator(func):
    def let_func(*args):
            print(len(args),"개")
        return func(*args):
    return ret_func
