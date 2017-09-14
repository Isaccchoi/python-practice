champion = "Lux"

def local1():
    champion ="Ahri"
    print('local1 :', champion)

    def local2():
        # nonlocal은 바깥 영역의 로컬스코프의 값을 참조할 수 있음
        nonlocal champion
        champion = "Ezreal"
        print('local2: ', champion)
    local2()
    print("local1: ", champion)


print('global: ', champion)
local1()
