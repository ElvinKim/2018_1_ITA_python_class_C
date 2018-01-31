"""
로또 구현하기
"""
print("{:-^20}".format(" problem1-1 "))
import random

lotto_lst = []

while len(lotto_lst) < 6:
    random_num = random.randint(1, 45)

    if random_num in lotto_lst:
        continue
    lotto_lst.append(random_num)

print(lotto_lst)


print("{:-^20}".format(" problem1-2 "))
lotto_lst = random.sample(range(1, 46), 6)
print(lotto_lst)


print("{:-^20}".format(" problem1-3 "))
num_range_lst = [i for i in range(1, 46)]
lotto_lst = []

for i in range(6):
    random_index = random.randint(0, 45 - (i + 1))
    lotto_lst.append(num_range_lst.pop(random_index))

print(lotto_lst)

"""
urllib module을 이용하여
https://www.kaist.ac.kr/_prog/fodlst/?site_dvs_cd=kr&menu_dvs_cd=050303
의 html 코드를 출력하기
"""

import urllib.request
url = "https://www.kaist.ac.kr/_prog/fodlst/?site_dvs_cd=kr&menu_dvs_cd=050303"

kaist_html = urllib.request.urlopen(url).read().decode("utf-8")
print(kaist_html)


