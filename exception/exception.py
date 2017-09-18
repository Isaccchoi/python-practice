l = list('abcd')
d = dict(name='Lux', champion_type="Magician")

print('program start')
try:
    # index에러를 일으키기 전 코드
    print('before l[5]')
    print('check dict key')
    d['Sona']
    print('check list index')
    l[5]
    # index에러를 일으킨 이후 코드
    print('after l[5]')
except IndexError as e:
    # index에러가 발생할 경우의 코드
    print(e)
    print('l[5] exception')
except KeyError as e:
    print(e)
    print("d['sona'] exception")


print('program terminated')
