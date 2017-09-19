def mydecorator(func):
    def len_args(*args):
        print(len(args))
        return func(*args)
    return len_args

@mydecorator
def selection_sort(*args):
    print("실제 함수")
    try:
        print("트라이문 안")
        if len(args) == 1:
            return args[0]
        length = len(args)
        result=list(args)
        for i in range(length-1):
            min_index = i
            for j in range(i+1, length):
                if result[min_index] < result[j]:
                    min_index = j
            result[i], result[min_index] = result[min_index], result[i]
        return result[0]
    except:
        print('Invalid arguments')


# def mydecorator(func):
#     print(len(args)


selection_sort(1,2,3,4,6,5,1,2,3,3,3,3,3,3,3)
