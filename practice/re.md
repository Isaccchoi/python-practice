# 정규표현식 (Regular Expressions)

특정한 패턴에 일치하는 복잡한 문자열 처리시 사용하는 기법

파이썬에서는 표준모듈 ```re```를 사용해서 정규표현식을 처리할 수 있다.


## match 
특정한 패턴을 첫번째 인자에 전달하여 찾는다 

```python
import re
result = re.match('Lux', 'Lux, the lady of Lmiosity')
```
```match```의 첫번 째 인자에는 패턴이 들어가며 두 번째 인자에는 문자열 소스가 들어간다. ```mactch()```는 패턴 일치 여부를 확인하고 일치할 경우 Match object를 반환한다.

조금 복잡하거나 자주 사용되는 패턴은 미리 컴파일 하여 속도를 향상 시킬 수 있음

```python
pattern1=re.compile('Lux')
```
## search
문자열 전체에서 첫 번째 일치하는 패턴을 찾는다

```python
>>> import re
>>> source = 'Lux, the Lady of Luminosity'
>>> m = re.search('Lady', source)
>>> if m:
...		print(m.group())
...		
Lady
```

## findall: 일치하는 모든 패턴 찾기

```python
>>> m = re.findall('y', source)
>>> m
>>> ['y','y']
>>> m = re.findall('y..', source)
>>> m
['y o']
```
```python
>>> m = re.findall('y.?.?',source)
>>> m
['y o','y']
```

## split: 패턴으로 나누기

문자열의 ```split()```메서드와 비슷하지만 패턴을 사용할 수 있다.

```python
>>> m = re.split('o', source)
>>> m
['Lux, the lady ', 'f Lumin', 'sity']
```

## sub: 패턴 대체 하기
문자열의 ```replace()```메서드와 비슷하지만 패턴을 사용할 수 있다.

```python
>>> m = re.sub('o', '!', source)
>>> m
'Lux, the Lady !f Lumin!sity'
```

## 정규표현식의 패턴 문자 

패턴 | 문자
---|---
\d|숫자
\D|비숫자
\w|문자
\W|비문자
\s|공백 문자
\S|비공백 문자
\b|단어 경계(\w \W의 경계)
\B|비단어 경계


## 정규표현식의 패턴 지정자(Pattern specifier)

패턴|의미
---|---
abc|리터럴```abc```
(expr)|expr
expr1\|exprt2|exprt1또는 expr2
```.```|```\n```을 제외한 모든 문자 
```^```|소스 문자열의 시작 
```$```|소스 문자열의 끝
expr```?```| 0또는 1회의  expr
expr```*```| 0회 이상의 최대 expr
expr```*?```|0회 이상의 최대 expr
expr```+```|1회 이상의 최대  expr
expr```+?```|1회 이상의 최소 expr
expr```{m}```|m회의 expr
expr```{m,n}```|m에서 n회의 최대 expr
expr```{m,n}?```|m에서 n회의 최소 expr
[abc]|a or b or c
[^abc]|not(a or b or c)
expr1(?=expr2)|뒤에 expr2가 오면 expr1에 해당하는 부분
expr1(?!expr2)|뒤에 expr2r가 오지 *않으면* expr1에 해당하는 부분
(?<=expr1)expr2|앞에 expr1이 오면 expr2에 해당하는 부분
(?<!expr1)expr2|앞에 expr1이 오지 *않으면* expr2에 해당 하는 부분


### r
정규 표현식 패턴에는 항상 앞에 r을 붙인다고 생각하는 것이 좋다.(만약 정규표현식 내부에서 ```\```를 쓰지 않을 경우, ```r```을 붙임과 붙이지 않음은 같은 결과를 가져 온다.

## 매칭 결과 그룹화
Match객체의```group()```함수는 매치된 *전체 문자열*을 리턴하며, ```groups()``` 함수는 지정된 *그룹 리스트*를 리턴해준다
```group(0)```은 ```group()```와 같은 동작을 하며 ```group(숫자)```는 매치된 ```숫자```번째의 그룹 요소를 리턴해준다.

```python
s = re.search(r'\w+\w(was)', story)
s.groups()
s.group(0)
s.group(1)
```
```(?P<name>expr)```패턴을 사용하면 매칭된 표현식 그룹에 이름을 붙여서 사용할 수 있다.

```python
m = re.search(r'(?P<before>\w+)\s+(?P<was>was)\s+(?P<after>\w+)', story)
m.groups()
m.group('before')
m.group('was')
m.group('after')
```

## 최소 일치와 최대 일치
```html
<html><body><h1>HTML</h1></body></html>
```
위 항목을 
```python
m = re.match(r'<.*>', html)
```
로 검색을 하면 ```.*```표현식이 첫 번째 ```>```에서 멈추는 것이 아니라 맨 마지막 ```>```까지 검색을 진행한다.
```*```이나 ```+```에 최소일치인 ```?```를 붙여주면, 표현식 다음부분에 해당하는 문자열이 처음 나왔을 때 그 부분까지만 일치시키고 검색을 마친다.

