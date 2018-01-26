"""
파일
"""
# print("{:-^20}".format(" write "))
# f = open("sample.txt", "w", encoding="utf-8")
# f.write("1\n")
# f.write("2\n")
# f.write("3\n")
# f.close()
#
# print("{:-^20}".format(" read "))
# f = open("sample.txt", "r", encoding="utf-8")
#
# print(f.read())
# print(f.readline())
# print("-" * 10)
#
# for line in f.readlines():
#     print(line)
#
# for _ in range(5):
#     print(f.readline())
# f.close()
#
# print("{:-^20}".format(" 추가 "))
# f = open("sample_2.txt", "a", encoding="utf-8")
# f.write("11\n")
# f.write("12\n")
# f.close()

print("{:-^20}".format(" with "))
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.readline())






