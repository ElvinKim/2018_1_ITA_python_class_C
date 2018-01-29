"""
클래스
"""

"""
학생
"""
class Student:
    def __init__(self, name, student_id, grade, age):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.age = age

    def study(self):
        print("나는 공부가 좋아~~~~")

    def drink(self, alcohol):
        print(alcohol + "을(를) 마시자~~~")

    def play_game(self, game_name):
        print(game_name + "을 하자~~~")

    def get_name(self):
        return self.name

    def set_age(self, age):
        if age < 0:
            self.age = 1
        else:
            self.age = age


"""
연애
"""
class Love:
    definition = "남녀가 서로 그리워하고 사랑함."

    def __init__(self, man, woman, duration_month, age_gap):
        self.man = man
        self.woman = woman
        self.duration_month = duration_month
        self.age_gap = age_gap

    def skinship(self):
        print(self.man, self.woman, "good")


class Restaurant:
    name = "유식당"
    menu = {"aa": 100, "bb": 200}
    location = "어은동"
    staffs = ["유재석", "강호동", "하하"]

    def cook(self, menu_name):
        print(menu_name + "을 만들자~~~")

    def promotion(self):
        print("어서옵쇼~~~")

    def delivery(self, menu_name):
        print(menu_name + "을 배달하자")


print("{:-^20}".format(" Knight class "))
class Knight:
    level = 20
    name = "만년동꿀주먹"
    hp = 200

    def move(self, direction):
        print(direction + "방향으로 이동합니다.")

    def attack(self):
        print(self)
        print(self.name + "이(가) 공격합니다.")


knight1 = Knight()
print(knight1)
knight1.attack()
print(knight1.name)
knight1.move("앞")

print("{:-^20}".format(" 멤버 변수 수정 "))
knight1.name = "어은동핵폭탄"
knight1.level = 200
print(knight1.name)
print(knight1.level)


print("{:=^20}".format(" 네임스페이스 "))
print(Knight.__dict__)
knight2 = Knight()
print(knight2.__dict__)
print(knight2.name)
knight2.name = "몰라몰라"
knight2.level = 30
knight2.hp = 300
print(knight2.__dict__)
print(knight2.name)


class Wizard:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def move(self, direction):
        print(direction + "방향으로 이동합니다.")

    def attack(self):
        print(self)
        print(self.name + "이(가) 공격합니다.")

    def magic(self):
        print(self.name + "이(가) 마법을 씁니다.")

wizard = Wizard("마법사", 30, 1000)

print("{:-^20}".format(" 객체 변수 설정 "))
sangmook = Student("SangMook", "20171111", 3.7, 30)

print(sangmook.get_name())
sangmook.set_age(31)
sangmook.age = -1
print(sangmook.age)
print(Love.definition)

print("{:=^20}".format(" 상속 "))