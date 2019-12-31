import lxml.html

tree = lxml.html.parse('dp.html')
html = tree.getroot()
html.make_links_absolute('https://gihyo.jp/')

for a in html.classselect('#listBook > li > a[itemprop="url"]'):
    url = a.get('href')
    p = a.classselect('p[itemprop="name"]')[0]
    title = p.text_content()

    print(url, title)