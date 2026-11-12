"""Build a fully static academic homepage using only Python's standard library."""
import json
import shutil
from datetime import date
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

def text(value):
    return escape(str(value), quote=True)

def url(value):
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        raise ValueError(f"Invalid URL: {value!r}")
    parsed = urlsplit(value)
    if parsed.scheme not in ('', 'https', 'http', 'mailto') or value.startswith('//'):
        raise ValueError('Only relative, HTTP(S), and mailto links are supported')
    if not parsed.scheme and ('..' in Path(parsed.path).parts or parsed.path.startswith('/')):
        raise ValueError('Local URLs must be relative to the website root')
    if parsed.scheme in ('http', 'https') and not parsed.netloc:
        raise ValueError('HTTP(S) URLs require a host')
    return text(value)

def link(label, value):
    return f'<a href="{url(value)}">{text(label)} ↗</a>'

def build():
    p = json.loads((ROOT / 'data/profile.json').read_text())
    for key in ('name', 'about', 'interests', 'publications', 'news', 'education', 'services'):
        if key not in p:
            raise ValueError(f'Missing profile key: {key}')
    photo = ROOT / p['photo']
    if not photo.is_file() or not photo.resolve().is_relative_to((ROOT / 'assets').resolve()):
        raise ValueError('Profile photo must be an existing asset')
    publications = []
    for paper in sorted(p['publications'], key=lambda item: item['year'], reverse=True):
        if not isinstance(paper['year'], int) or not paper['title'] or not paper['venue']:
            raise ValueError('Every paper needs a title, venue, and integer year')
        authors = ', '.join(text(a) for a in paper['authors']) or 'Authors to be confirmed'
        links = ''.join(link(k, v) for k, v in paper['links'].items() if v)
        publications.append(f'<article class="publication"><div class="pub-year">{paper["year"]}</div><div><h3>{text(paper["title"])}</h3><p class="authors">{authors}</p><p class="venue">{text(paper["venue"])}</p><div class="paper-links">{links}</div></div></article>')
    def timeline(entries, empty):
        if not entries:
            return f'<p class="empty">{text(empty)}</p>'
        return '<ul class="timeline">' + ''.join(f'<li><time>{text(e["date"])}</time>{text(e["text"])}</li>' for e in entries) + '</ul>'
    values = {k: text(v) for k, v in p.items() if isinstance(v, str)}
    values.update(
        social_links=''.join(link(k, v) if v else f'<span class="unavailable">{text(k)} <small>To add</small></span>' for k, v in p['links'].items()),
        about=''.join(f'<p>{text(a)}</p>' for a in p['about']),
        interests=''.join(f'<span>{text(i)}</span>' for i in p['interests']),
        news=timeline(p['news'], 'Updates will appear here.'),
        publications=''.join(publications) or '<p class="empty">Publications will be added here.</p>',
        education=timeline(p['education'], 'Education details will be added soon.'),
        services=timeline(p['services'], 'Academic service details will be added soon.'),
        year=str(date.today().year),
    )
    html = Template((ROOT / 'templates/index.html').read_text()).substitute(values)
    dist = ROOT / 'dist'
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir()
    (dist / 'index.html').write_text(html, encoding='utf-8')
    shutil.copytree(ROOT / 'assets', dist / 'assets')
    (dist / '.nojekyll').touch()
    print(f'Built {len(publications)} publications → {dist}')

if __name__ == '__main__':
    build()
