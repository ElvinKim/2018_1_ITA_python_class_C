"""
정규 표현식
"""
import re

print("{:-^20}".format(" match "))

pattern = re.compile("[a-z]+")
sample_str = "Pabc aaaa bbb Aabbb"

m = pattern.match(sample_str)
print(m)

print("{:-^20}".format(" search "))
pattern = re.compile("[a-z]+")
sample_str = "Pabc aaaa bbb Aabbb"

m = pattern.search(sample_str)
print(m)

print("{:-^20}".format(" find all "))
pattern = re.compile("[a-z]+")
sample_str = "Pabc aaaa bbb Aabbb"

match_results_lst = pattern.findall(sample_str)
print(match_results_lst)


print("{:-^20}".format(" find iter "))
pattern = re.compile("[a-z]+")
sample_str = "Pabc aaaa bbb Aabbb"

match_results_iter = pattern.finditer(sample_str)

for m in match_results_iter:
    print(m.span())


print("{:-^20}".format(" match obj "))
pattern = re.compile("[a-z]+")
sample_str = "Pabc aaaa bbb Aabbb"

m = pattern.search(sample_str)
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())


print("{:-^20}".format(" compile option "))
pattern = re.compile("abc.abc")
m = pattern.match("abc\nabc")
print(m)

pattern = re.compile("abc.abc", re.DOTALL)
m = pattern.match("abc\nabc")
print(m)

print("{:-^20}".format(" greedy vs non-greedy "))

html = """
<div>
<span>aaa</span>
<div>TEST</div>
</div>
"""

pattern = re.compile("<.*?>", re.DOTALL)
print(pattern.findall(html))