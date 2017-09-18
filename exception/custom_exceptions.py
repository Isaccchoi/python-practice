import re

# custom Exception클래스 정의
class NotMatchedException(Exception):
    # 출력될 내용 안에 pattern과 Source를 담아야 하기때문에 raise시 함께 받음
    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source

    # Exception 발생시에 출려될 내용
    def __str__(self):
        return f"Pattern {self.pattern}is not exist in {self.source}"

def search_from_source(p, s):
    m = re.search(p, s)
    # search가 실패할 경우 None이 반환됨
    if not m:
        # 에러 강제로 발생
        raise NotMatchedException(p, s)

s = 'lux, the Lady of Luminosity'
p = r'L\w{5}\b'

# Error가 발생하는 것을 TryExcept로 감쌈
try:
    result = search_from_source(p, s)
    print(result)
# custom Exception인 NotMatchedException에서만 print해서 처리
except NotMatchedException:
    print('에러남')
