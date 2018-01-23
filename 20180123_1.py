a = "ABCABCABCCCC"

# count
print("{:-^20}".format(" count "))
print(a.count("AB"))

# index & find
print("{:-^20}".format(" index & find "))
print(a.index("B"))
print(a.find("B"))

# print(a.index("E"))
# print(a.find("E"))

# join
print("{:-^20}".format(" join "))
print(",".join(a))
print("-".join(a))

# upper & lower
print("{:-^20}".format(" upper & lower "))
b = "abcDEFg"
print(b.upper())
print(b.lower())

# strip
print("{:-^20}".format(" strip "))
print("         abc         ".lstrip())
print("         abc         ".rstrip())
print("         abc         ".strip())

# replace
print("{:-^20}".format(" replace "))
print("python is bad".replace("bad", "good"))
print("python is bad bad bad".replace("bad", "good", 2))


# split
print("{:-^20}".format(" split "))
print("python is bad bad bad".split())
print("python,is,bad,bad,bad".split(","))

# format
print("{:-^20}".format(" format "))
print("{:<20}".format("hi"))
print("{:>20}".format("hi"))
print("{:^20}".format("hi"))






