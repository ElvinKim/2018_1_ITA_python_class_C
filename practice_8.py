print("{:-^20}".format(" practice 1 "))
def average(a, b):
    return (a + b) / 2


print("{:-^20}".format(" practice 2-1 "))
def list_average_ver1(lst):
    total = 0
    cnt = 0

    for num in lst:
        total += num
        cnt += 1

    return total / cnt


def list_average_ver2(lst):
    return sum(lst) / len(lst)


print(average(10, 20))
print(list_average_ver1([1, 2, 3, 4, 5]))
