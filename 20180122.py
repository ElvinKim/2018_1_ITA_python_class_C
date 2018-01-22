"""
변수
"""

a = 10
b = "ABCD"

print(a)
print(b)

_name = "SangMook"
var_1 = 10

# error
# 10a = 10
# True = 10

a = 10
A = 20
print(a)
print(A)

print("=" * 30)

"""
문자열
"""
print(int("12345"))
print(str(12345))

print("I'm a python programmer")
print('I\'m a python programmer')

print("Life is too short\nYou need Python")

s = """python
is 
very 
good
"""
print(s)

# 문자열 연산자
print("-" * 30)
print("ABC" + "DEF")
print("ABC" * 3)

score = 90
print(str(score) + "점")

# 인덱싱 & 슬라이싱
print("-" * 30)
b = "gfedcba"
print(b[0])
print(b[2])
print(b[-1])
print(b[-2])

print(b[0:3])
print(b[3:-1])


# 포맷팅
print("-" * 30)
name_format = "나의 이름은 %s 입니다."
age_format = "나의 나이는 %d살 입니다."
name_age_format = "나의 나이는 %d살 이고 이름은 %s입니다."

print(name_format % "김상묵")
print(age_format % 20)
print(name_age_format % (20, "김상묵"))

name_age_format_ver2 = "나의 나이는 %s살 이고 이름은 %s입니다."

print(name_age_format_ver2 % (str(20), "김상묵"))


# format function
print("-" * 30)
name_format = "나의 이름은 {} 입니다."
age_format = "나의 나이는 {}살 입니다."
name_age_format = "나의 나이는 {}살 이고 이름은 {}입니다."

print(name_format.format("김상묵"))
print(age_format.format(20))
print(name_age_format.format(20, "김상묵"))
print("나의 나이는 {1}살 이고 이름은 {0}입니다.".format("김상묵", 20))
print("나의 나이는 {age}살 이고 이름은 {name}입니다.".format(name="김상묵", age=20))

















