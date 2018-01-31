import urllib.request
import re


url = "https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=fclt&dvs_cd=fclt&stt_dt=2018-01-31&site_dvs="

kaist_html = urllib.request.urlopen(url).read().decode("utf-8")

menu_pattern = re.compile('''<table class="menuTb".*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>''', re.DOTALL)

for menu in menu_pattern.findall(kaist_html)[0]:
    menu = menu.replace("<br />", "").replace("&amp;", "")
    re.sub()
    print("-" * 30)
