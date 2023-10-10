import requests
from lxml import etree


url = "https://nba.hupu.com/stats/players"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"
}
req = requests.get(url, headers=headers)

e = etree.HTML(req.text)
a = e.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr/td[2]/a/text()")
b = e.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr/td[3]/a/text()")
c = e.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr/td[4]/text()")
d = e.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr/td[5]/text()")
with open("nba.txt", "w", encoding="utf-8") as f:
    for a, b, c, d in zip(a, b, c, d):
        f.write(f"姓名:{a} 球队:{b} 得分：{c} 命中-出手:{d}\n")
