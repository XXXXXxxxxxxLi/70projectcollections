import requests
from lxml import etree
import os

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"
}

hero_info_url = "https://pvp.qq.com/web201605/js/herolist.json"
req1 = requests.get(hero_info_url, headers=headers)
hero_data = req1.json()

for h in hero_data:
    ename = h.get("ename")
    cname = h.get("cname")

    # 创建英雄文件夹
    if not os.path.exists(cname):
        os.makedirs(cname)

    hero_info_url = f"https://pvp.qq.com/web201605/herodetail/{ename}.shtml"
    hero_info_req = requests.get(hero_info_url, headers=headers)
    hero_info_req.encoding = "gbk"
    e = etree.HTML(hero_info_req.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]

    # 处理名称，去除后面的&和数字
    names = [name.split("&")[0] for name in names.split("|")]

    for i, n in enumerate(names):
        j = i + 1
        req = requests.get(
            f"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{j}.jpg",
            headers=headers,
        )

        # 构建完整的文件路径
        file_path = os.path.join(cname, f"{n}.jpg")

        with open(file_path, "wb") as f:
            f.write(req.content)

        print(f"已下载：{n}的皮肤，保存在 {file_path}")
