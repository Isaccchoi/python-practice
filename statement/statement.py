is_holiday = True


# if문
if is_holiday:
    print("Good")
else:
    print("bad")


# 조건 표현식
print("Good") if is_holiday else print("Bad")



vacation = 5
# 중첩  if문
if vacation > 7:
    print("Good")
elif vacation > 5:
    print("Normal")
else:
    print("Bad")

# 중첩 조건 표현식
print("Good") if vacation >= 7 else print("normal") if vacation >=5 else print("Bad")


# zip을 사용하지 않고 여러 시퀀스 동시순회
fruits = ['apple', 'banana', 'melon']
colors = ['red', 'yellow', 'green', 'purple']

for fruit in fruits:
    print("fruit: " + fruit + " color: " + colors[fruits.index(fruit)])

# zip으로 묶을 경우 여러 시퀀스를 동시순회가 가능하며 여러 시퀀스중 가장 짧은 시퀀스가 끝나면 순회가 멈춘다

fruits = ['apple', 'banana', 'melon']
colors = ['red', 'yellow', 'green', 'purple']

for fruit, color in zip(fruits, colors):
    print('fruit:', fruit, ' color:', color)


# While 문 - 참일동안 계속 반복(무한루프가 될 수도 있음)


# 컴프리헨션 - 함축 내포
# 컴프리헨션 안에 조건문을 넣을 수 있다

l = [item for item in range(1,6)]
l2 = [item for item in range(1,6) if item%2 ==0]



for first_number in range(0,7):
    for second_number in range(1,4):
        print(first_number + ", " + second_number)


l = [(first_number, second_number) for first_number in range(0,7)  for second_number in range(1,4)]



for first_number in range(0,7):
    if first_number % 2 == 0:
        for second_number in range(1,4):
            print(first_number, second_number)
    else:
        continue

l = [(first_number, second_number) for first_number in range(0,7)  for second_number in range(1,4) if second_number % 2 == 0]

result=0
for number in range(1000, 20001):
    if number % 2 ==1:
        result += number

# 컴프리헨션 리스트
result = sum([x for x in range(1001, 2000) if x % 2 ==0])


# step 사용
result = sum([x for x in range(1001, 2000, 2)])


# 구구단 컴프리헨션 리스트 사용
l = ['%d x %d = %d' % (x,y, x * y) for x in range(2,10) for y in range(1,10)]


# 현재 출력하는 결과가 몇단인지 표현
gugu_index = 2
# 전체 구구단 결과리스트중 몇번째를 순회하는지
list_index = 0

for item in l:
    if list_index % 9 == 0:
        print("==%s단==" % gugu_index)
        gugu_index += 1
    list_index += 1
    print(item)



number_list = []
for number in range(1,100):
    if number % 7 == 0:
        number_list.append(number)
    elif number % 9 == 0:
        number_list.append(number)


# 구구단 중첩 리스트 컴프리헨션
gugu_list = []
gugu_list = [{
            "title": "%d단" % x,
            "items": ["%d x %d =%d"% (x,y,x*y) for y in range(1, 10)]
        }
        for x in range(2,10)
]

print(gugu_list)
