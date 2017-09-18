while True:
    l = [1,2,3,4]
    index_num = int(input("숫자를 입력해주세요: "))
    # index_num = int(index_num)
    try:
        l[index_num]
    except:
        print('IndexError!!!')
        continue
    else:
        break
