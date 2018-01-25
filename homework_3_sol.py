print("{:-^20}".format(" problem 1-1 "))
for i in range(5):
    print("*" * (i + 1))

print("{:-^20}".format(" problem 1-2 "))
for i in range(5):
    for _ in range(i + 1):
        print("*", end="")
    print("")

print("{:-^20}".format(" problem 2-1 "))
n = 10
for i in range(n):
    form = "{:^" + str(2 * n - 1) + "}"
    print(form.format("*" * (2 * i + 1)))


print("{:-^20}".format(" problem 2-2 "))
for i in range(5):
    for _ in range(5 - (i + 1)):
        print(" ", end="")
    for _ in range(2 * i + 1):
        print("*", end="")
    print("")

print("{:-^20}".format(" problem 3-1 "))
sample_str = "BACAABBCCE"
c = "C"
index_lst = []
idx = 0

for s in sample_str:
    print(idx, s)
    if c == s:
        index_lst.append(idx)
    idx += 1
print(index_lst)


print("{:-^20}".format(" problem 3-2 "))
index_lst = []
for idx in range(len(sample_str)):
    if sample_str[idx] == c:
        index_lst.append(idx)
print(index_lst)

print("{:-^20}".format(" problem 3-3 "))
index_lst = []
for idx, s in enumerate(sample_str):
    if c == s:
        index_lst.append(idx)
print(index_lst)












