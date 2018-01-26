f = open("sample.txt", 'r', encoding="utf-8")
#print(f.read())
#print(f.readlines())
#print(f.read())

# for line in f.readlines()[:5]:
#     print(line)

for _ in range(5):
    print(f.readline())
