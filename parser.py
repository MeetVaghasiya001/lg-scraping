from request_data import *
from lxml import html
import re



def get_all_catagory_links(url):
    response = request(url)

    if response:
        all_links = {}
        tree = html.fromstring(response)
        main_divs = tree.xpath("//div[contains(@class,'menu-link')]")

        for div in main_divs:
            text = div.xpath("string(.)").strip()
            links = div.xpath("following-sibling::ul[1]//a/@href")
            if text:
                all_links[text] = links

        return all_links
    


def get_target_json(url):
    res = request(url)
    if not res:
        return None

    tree = html.fromstring(res)
    scripts = tree.xpath("//script[contains(text(), '__next_f.push')]/text()")

    pattern = r'self\.__next_f\.push\(\[\d+,\s*"((?:\\.|[^"\\])*\{[^{}]*"lang":"en-IN"[^{}]*\}(?:\\.|[^"\\])*)"\]\)'

    for s in scripts:
        m = re.search(pattern, s, re.DOTALL)
        if m:
            # unescape string
            s2 = bytes(m.group(1), "utf-8").decode("unicode_escape")

            # extract JSON object
            j = re.search(r'\{[^{}]*"lang":"en-IN"[^{}]*\}', s2)
            if j:
                return json.loads(j.group())

    return None


data = get_target_json('https://www.lg.com/in/tv-soundbars/oled-evo/')
with open('json pages/page.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,default=str)

# data = get_all_links('https://www.lg.com/in/')
# with open('json pages/links.json','w',encoding='utf-8') as f:
#     json.dump(data,f,indent=4,default=str)