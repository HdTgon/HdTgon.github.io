"""Check generated local assets, navigation, publication fields and Pages contract."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])

page = Page()
page.feed((ROOT / 'dist/index.html').read_text())
assert len(page.ids) == len(set(page.ids)), 'Duplicate IDs'
assert {'about', 'research', 'news', 'publications', 'education', 'services'} <= set(page.ids)
for ref in page.refs:
    parsed = urlsplit(ref)
    if parsed.scheme:
        assert parsed.scheme in ('http', 'https', 'mailto'), ref
    elif parsed.path:
        asset = ROOT / 'dist' / unquote(parsed.path)
        assert asset.is_file(), f'Missing local asset: {ref}'
    elif parsed.fragment:
        assert parsed.fragment in page.ids, f'Missing anchor: {ref}'
profile = json.loads((ROOT / 'data/profile.json').read_text())
for p in profile['publications']:
    assert {'title','authors','venue','year','links'} <= p.keys()
    assert isinstance(p['authors'], list) and isinstance(p['links'], dict)
workflow = (ROOT / '.github/workflows/pages.yml').read_text()
for required in ('branches: [main]', 'workflow_dispatch:', 'pages: write', 'id-token: write', 'actions/upload-pages-artifact@v3', 'actions/deploy-pages@v4', 'path: dist', 'needs: build', 'name: github-pages'):
    assert required in workflow, f'Missing deployment setting: {required}'
assert (ROOT / 'dist/.nojekyll').exists()
print(f'PASS: six sections, {len(page.refs)} references, local assets, publication schema and Pages contract')
