"""
예외처리
"""
import random as rd

# print("{:-^20}".format(" Sample "))
# while True:
#     try:
#         a = int(input("a = "))
#         b = int(input("b = "))
#         print("{} / {} = {}".format(a, b, a / b))
#     except ZeroDivisionError as e:
#         print(e)
#         print("0으로 나눌 수 없어!!!")
#     except ValueError as e:
#         print(e)
#         print("입력 값에 문제가 있네....!")
#     except Exception as e:
#         print(e)

print("{:-^20}".format(" 오류 발생 시키기 "))

class Person:
    def introduce(self):
        raise NotImplemented


class Police(Person):
    def introduce(self):
        print("나는 경찰관이야!!!")


class Student(Person):
    def introduce(self):
        print("나는 학생이야~~~")

kim = Police()
kim.introduce()
park = Student()
park.introduce()


print("{:-^20}".format(" 에러만들기 "))
class Molla(Exception):
    def __str__(self):
        return "몰라 에러 발생이야."

class ScoreError(Exception):
    def __str__(self):
        return "범위가 아닌 값을 입력하였습니다."


def input_score(score):
    if score < 0 or score > 100:
        raise ScoreError()

try:
    input_score(200)
except ScoreError as e:
    print(e)
