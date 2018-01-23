print("{:-^20}".format(" practice 1 "))
lst= []
lst.append(21)
lst.extend([42, 23, 14, 5, 66])

print("{:-^20}".format(" practice 2 "))
lst.sort()
print(lst)

print("{:-^20}".format(" practice 3 "))
max_num = max(lst)
min_num = min(lst)
print("max:", max_num)
print("min:", min_num)

print("{:-^20}".format(" practice 4 "))
lst.remove(max_num)
lst.remove(min_num)
print(lst)


