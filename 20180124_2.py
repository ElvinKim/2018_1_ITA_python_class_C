"""
제어문
"""
print("{:=^20}".format(" Sample "))
print(1 > 0)
print(1 < 0)

if True:
    print("True condition")

if False:
    print("False condition")

if 1 > 0:
    print("True condition")
    print("aaa")

if 1 < 0:
    print("False condition")

if True:
    if True:
        print("True & True condition")
    if False:
        print("True & False condition")


print("{:-^20}".format(" if-else "))
input_num = int(input("input number:"))
if input_num % 2 == 1:
    print("홀수")
else:
    print("짝수")

print("{:-^20}".format(" if-elif-else "))
input_num = int(input("input number:"))

if input_num > 0:
    print("양수")
elif input_num < 0:
    print("음수")
else:
    print("zero")

input_num = int(input("input number:"))

if input_num % 3 == 0:
    print("3의 배수")
elif input_num % 4 == 0:
    print("4의 배수")

print("{:-^20}".format(" or-and-not "))
print(True and False)
print(True or False)
print(not True)

english_score = 90
math_score = 70

if english_score > 80 and math_score > 80:
    print("PASS")
else:
    print("FAIL")


print("{:-^20}".format(" in "))
if "A" in ["A", "B", "C"]:
    print("가즈아!")

if "A" in ("A", "B", "C"):
    print("가즈아!")

print("{:-^20}".format(" 자료형의 참과 거짓 "))
if "ABC":
    print("True")

if ["ABC"]:
    print("True")

if 10:
    print("True")

if None:
    print("False")

if 0:
    print("False")

if "":
    print("False")

if []:
    print("False")

if not None:
    print("not None")

print("{:-^20}".format(" while sample "))
x = 0
while x < 10:
    print(x)
    x += 1  # x = x + 1

print("{:-^20}".format(" while break "))
x = 0
while True:
    if x * 3 > 56:
        break
    x += 1
print(x)

x = 0
while x * 3 <= 56:
    x += 1
print(x)

print("{:-^20}".format(" while continue "))
a = 0
while a <= 20:
    a += 1
    if a % 2 == 1:
        continue
    print(a)

print("{:-^20}".format(" 무한루프 "))
x = 0
while x < 10:
    print(x)

print("{:=^20}".format(" For "))
print("{:-^20}".format(" sample "))

for x in ["python", 1, 2, 3, 4, 5]:
    print(x)

for x in "ABCD":
    print(x)

print("{:-^20}".format(" range "))
for n in range(10):
    print("*", end="")

for n in range(1, 11):
    print(n)

for n in range(1, 11, 2):
    print(n)

print("{:-^20}".format(" 구구단 "))

for i in range(2, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))
    print("-" * 10)


















