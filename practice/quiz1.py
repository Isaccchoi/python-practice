# 1부터 20까지의 정수를 갖는 result 리스트를 만들고
# 슬라이스 연산으로 해당 리스트를 '홀수'만 가지며, '역순'이 되도록 하시오.

result = list(range(1,21))
result = [x for x in range(1,21)]


# split및 join을 사용하여 우울한 하루를 활기찬 하루로 바꾸시오
today = '우울한 하루'
today = today.split()
today[0] = '활기찬'
" ".join(today)


# 숫자를 받아 곱을 계산하여 반환하는 myfunc를 할당하여 만드시오
# 1자가 1개면 제곱, 2개면 두 수의 곱 그외에는 'Invalid arguments'를 출력
def myfunc(*args):
    length = len(args)
    if length == 1:
        return args[0] **2
    elif length ==2:
        return args[0] * args[1]
    else:
        return 'Invalid arguments'
