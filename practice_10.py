print("{:-^20}".format(" practice 1-1 "))

def my_average(*args):
    return sum(args) / len(args)


print("{:-^20}".format(" practice 1-2 "))
def my_average(*args):
    total = 0
    cnt = 0

    for num in args:
        total += num
        cnt += 1

    return total / cnt

print("{:-^20}".format(" practice 2 "))
def my_concat(c, *args):
    return c.join(args)


print(my_concat("-", "a", 'b', 'c'))




