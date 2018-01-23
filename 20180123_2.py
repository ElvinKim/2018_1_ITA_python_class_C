print("{:=^20}".format(" List "))
print([])
print([1, 2, 3, 4, 5])
print(["python", "is", "good"])
print([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("{:-^20}".format(" list sample "))
a = ["python", 1, 2, 3, 4, 5, 6]
print(a[0])
print(a[0][0])
print(a[3:])
print(a[-2])

print("{:-^20}".format(" list 연산자 "))
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

print("{:-^20}".format(" list 수정 "))
a = [1, 2, 3, 4, 5]
a[0] = 100
a[4] = 500
a[1] = [200, 300, 400]
a[1:2] = [200, 300, 400]
a[1:4] = [200, 300, 400]
print(a)

print("{:-^20}".format(" list 삭제 "))
a = [1, 2, 3, 4, 5]
del a[1]
del a[1:]
print(a)


print("{:-^20}".format(" copy module "))
import copy
a = [1, 2, 3, 4, 5, 6]
b = copy.copy(a)
b[0] = 100
print(b)
print(a)

print("{:-^20}".format(" function of list "))
a = [1, 2, 3, 4]
a.append(5)
print(a)

# sort
b = [3, 2, 6, 3, 1, 4]
b.sort()
print(b)

# reverse
b.reverse()
print(b)

# index
b = [3, 2, 6, 3, 1, 4]
print(b.index(3))


# insert
b = [3, 2, 6, 3, 1, 4]
b.insert(0, "python")
print(b)

# remove
b = [3, 2, 6, 3, 1, 4]
b.remove(3)
print(b)

# count
b = [3, 2, 6, 3, 1, 4]
print(b.count(3))

# pop
b = [3, 2, 6, 3, 1, 4]
print(b.pop())
print(b)
print(b.pop())
print(b)
print(b.pop(0))
print(b)

# extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
# a += b
# a = a + b
print(a)


print("{:=^20}".format(" Tuple "))
a = (1, 2, 3, 4, 5)
# a[0] = 10
# del a[0]

print("{:=^20}".format(" Dictionary "))
lst = ['a', 'b', 'c']
print(lst[0])
lst_dict = {0: "a", 1: "b", 2: "c", 10: "d"}
print(lst_dict[0])

# dictionary
me = {"name": "SangMook", "age": 20}
print(me)

# 추가
me['id'] = 100
print(me)

# 삭제
del me["age"]
print(me)


print("{:=^20}".format(" Set "))
lst = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]
print(list(set(lst)))
t = (1, 2, 3, 4, 5, 6, 7)
t_lst = list(t)
t_lst[0] = 10
print(t_lst)
lst = [100, 200]
l_tuple = tuple(lst)
print(l_tuple)
