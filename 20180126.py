"""
함수 - 2
"""

print("{:=^20}".format(" function return "))
def calculation(a, b):
    return a + b, a - b, a * b, a / b

print(calculation(1, 2))

def sum_sub(a, b):
    return a + b
    return a - b

print(sum_sub(1, 2))

print("{:=^30}".format(" function param init "))
def login(email, password, remember_me=False):
    print("email :", email)
    print("password :", password)

    if remember_me:
        print("나를 기억해!")

login("sangmook.kim@kaist.ac.kr", 123)
login("sangmook.kim@kaist.ac.kr", 123, True)



print("{:=^30}".format(" global "))
n = 1

def make_10():
    global n
    n = 10

make_10()
print(n)










