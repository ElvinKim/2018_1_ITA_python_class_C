"""
함수
"""
print("{:=^20}".format(" function sample "))

def add(a, b):
    return a + b


def odd_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

print(add(10, 20))
print(add("A", "B"))
print(odd_even(100))

print("{:=^20}".format(" 함수의 형태 "))
def return_my_name():
    return "영희"


def print_my_name(name):
    print("my name is " + name)


def say_hi():
    print("hi!!!!!")

print(return_my_name())
print(print_my_name("영희"))
say_hi()


print("{:=^20}".format(" 함수의 매개변수 "))

def multi_param_sample(*args):
    print(args)

multi_param_sample(1, 2, 3, 4, 5, 6)


def my_sum_ver1(*args):
    total = 0
    for num in args:
        total += num
    return total

def my_sum_ver2(*args):
    return sum(args)

def multi_param_sample_2(a, b, *args):
    print(a)
    print(b)
    print(args)

multi_param_sample_2(1, 2, 3, 4, 5, 6)










