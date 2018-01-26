print("{:=^20}".format(" problem 1 "))

f = open('multiplication_table.txt', "w", encoding="utf-8")
for i in range(2, 10):
    for j in range(1, 10):
        f.write("{} * {} = {}\n".format(i, j, i * j))
    f.write("-" * 10 + "\n")
f.close()

print("{:=^20}".format(" problem 2 "))
f = open('multiplication_table.txt', "r", encoding="utf-8")

for line in f.readlines():
    # print(line, end="")
    # print(line.strip())
    print(line.replace("\n", ""))
f.close()

print("{:=^20}".format(" problem 3 "))
with open('multiplication_table.txt', "a", encoding="utf-8") as f:
    for i in range(10, 20):
        for j in range(1, 10):
            f.write("{} * {} = {}\n".format(i, j, i * j))
        f.write("-" * 10 + "\n")

