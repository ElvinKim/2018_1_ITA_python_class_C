from bs4 import BeautifulSoup
import urllib.request


url = "https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=emp&stt_dt=2018-02-01&site_dvs="
req = urllib.request.Request(url)
kaist_menu_html = urllib.request.urlopen(req).read().decode("utf-8")

soup = BeautifulSoup(kaist_menu_html, "html.parser")

menu_list = soup.find("table", {"class": "menuTb"}).find_all("td")

for menu in menu_list:
    print(menu.text)
    print("-" * 30)
