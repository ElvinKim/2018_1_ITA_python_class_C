if "abc" in "abc aaa bb dd":
    print("abc")

lst = list("ABCDEFGABCDEFG")

idx = 0
for x in lst:
    print(idx, x)
    idx += 1

print("{:-^20}".format(" enumerate "))
for i, x in enumerate(lst):
    print(i, x)

x, y, z = (1, 2, 3)

print(x)
print(y)

print("{:-^20}".format(" list compression "))
square_lst = []
for num in range(1, 11):
    square_lst.append(num ** 2)
print(square_lst)

square_lst = [num ** 2 for num in range(1, 11)]
print(square_lst)


print("{:-^20}".format(" zip "))
lst1 = ["a", "b", "c", "d", "e", "f", "g"]
lst2 = ["A", "B", "C", "D"]

for i, j in zip(lst1, lst2):
    print(i, j)

print([x for x in zip(lst1, lst2)])



