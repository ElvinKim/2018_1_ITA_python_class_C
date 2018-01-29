class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def use(self, device):
        print(device.name + "(를)을 쓴다.")


class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grage = grade


class Device:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Smartphone(Device):
    def __init__(self, name, brand, phone_number):
        Device.__init__(self, name, brand)
        self.phone_number = phone_number

smartphone = Smartphone("갤럭시 6 엣지", "삼성", "01012345678")
sangmook = Student("상묵", 30, 3.7)

sangmook.use(smartphone)