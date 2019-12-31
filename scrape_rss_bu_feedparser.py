import feedparser

d = feedparser.parse('https://b.hatena.ne.jp/hotentry/it.rss')
for entry in d.entries:
    print(entry.link, entry.title)