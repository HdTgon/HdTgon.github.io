from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.refs=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for k in ('href','src'):
            if k in a:self.refs.append(a[k])
root=Path('_site');p=Page();html=(root/'index.html').read_text();p.feed(html)
assert {'about-me','research','news','publications','education','awards'} <= set(p.ids)
assert len(p.ids)==len(set(p.ids))
assert 'Lorem ipsum' not in html and '260000+' not in html
for ref in p.refs:
    u=urlsplit(ref)
    if u.scheme or u.netloc:continue
    if u.path:
        target=root/unquote(u.path.lstrip('/'))
        assert target.exists(), f'Missing asset: {ref}'
    elif u.fragment:assert u.fragment in p.ids, f'Missing anchor: {ref}'
print('PASS: six sections, navigation, assets, and no template demo claims')
