print("{:-^20}".format(" practice 1 "))
a = 20180108

str_a = str(a)
y = str_a[:4]
m = str_a[4:6]
d = str_a[6:]

print(y + "년 " + m + " 월" + d + "일")

print("{:-^20}".format(" practice 2 "))
b = "hi SangMook"
print("hello" + b[2:])
print(b.replace("hi", "hello"))

print("{:-^20}".format(" practice 3 "))
word = input("Please input your string: ")
print(word[0].upper() + word[1:-1].lower() + word[-1].upper())


