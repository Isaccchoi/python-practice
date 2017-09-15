# 1,2번
def fruits(color):
    'input color, return fruits'
    color_fruit = {
        "red": "apple",
        "yellow": "banana",
        "green": "menon",
    }
    if color in color_fruit:
        return color_fruit[color]
    else:
        return "I don't know"

    # if color == "red":
    #     return "apple"
    # elif color == "yellow":
    #     return "banana"
    # elif color == "green":
    #     return "melon"
    # else:
    #     return "I don't know"


result1 = fruits("red")
result2 = fruits("yellow")
result3 = fruits("green")
result4 = fruits("blue")


print(result1)
print(result2)
print(result3)
print(result4)
help(fruits)


#3번
def calc(*args):
    if len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 1:
        return args[0] ** 2
    else:
        return None

print(calc(3))
print(calc(3, 5))
print(calc(3,5,7))

# 4번
def addsubtract(first, second):
    if first > second:
        return (first + second, first - second)
    else:
        return (first + second, second - first)

print(addsubtract(3,2))
print(addsubtract(2,5))
print(type(addsubtract(3,2)))

# 5번
def length_args(*args):
    print(len(args))
    return len(args)

length_args(3,4,5,6,7,8,9)
print(length_args(3,4,5,6,7,8,9,10))

# 6번
print([(lambda x, y : "%d x %d = %d" % (x, y, x * y))(x, y) for x in range(2, 10) for y in range(1, 10)])
