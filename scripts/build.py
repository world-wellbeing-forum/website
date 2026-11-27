"""Build and validate the static World Well-Being Forum website."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import shutil, os, re
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]
nl=chr(10)
routes=['about','our-work','health','environment','humanitarian','education-technology','global','founder','get-involved','contact','programs']
for route in routes:
    source=root/(route+'.html')
    if not source.is_file(): raise SystemExit(f'Missing page source: {source}')
    folder=root/route
    folder.mkdir(exist_ok=True)
    shutil.copy2(source,folder/'index.html')
class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.ids=set()
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for attr in ('href','src','action'):
            if attrs.get(attr): self.links.append(attrs[attr])
files=list(root.glob('*.html'))+[root/r/'index.html' for r in routes]
docs={}
for file in files:
    source=file.read_text(encoding='utf-8')
    if not source.lstrip().lower().startswith('<!doctype html>'):
        raise SystemExit(f'{file}: missing HTML5 doctype')
    if '<html' not in source.lower() or '<head' not in source.lower() or '<body' not in source.lower():
        raise SystemExit(f'{file}: incomplete HTML document')
    doc=Document()
    doc.feed(source)
    docs[file.resolve()]=doc
errors=[]
for file,doc in docs.items():
    for link in doc.links:
        url=urlsplit(link)
        if url.scheme or url.netloc or not url.path: continue
        target=root/unquote(url.path).lstrip('/') if url.path.startswith('/') else file.parent/unquote(url.path)
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{file.name}: missing {link}')
        elif url.fragment and target.resolve() in docs and url.fragment not in docs[target.resolve()].ids:
            errors.append(f'{file.name}: missing anchor {link}')
if errors: raise SystemExit(nl.join(errors))
dist=root/'dist'
if dist.exists(): shutil.rmtree(dist)
dist.mkdir()
for file in root.glob('*.html'): shutil.copy2(file,dist/file.name)
for route in routes: shutil.copytree(root/route,dist/route)
shutil.copytree(root/'assets',dist/'assets')
if not (dist/'index.html').is_file() or not (dist/'assets/style.css').is_file() or not (dist/'assets/logo.svg').is_file():
    raise SystemExit('Deployment artifact is missing its homepage or core assets')
base_path=os.environ.get('BASE_PATH','').strip('/')
base_path='/'+base_path if base_path else ''
site_url=os.environ.get('SITE_URL','https://world-wellbeing-forum.github.io/website').rstrip('/')
if not site_url.startswith(('https://','http://')): raise SystemExit('SITE_URL must be an absolute HTTP(S) URL')
for file in dist.rglob('*'):
    if file.suffix not in {'.html','.css'}: continue
    source=file.read_text(encoding='utf-8')
    if base_path:
        source=re.sub(r"""((?:href|src|action)=["'])/(?!/)""",lambda m:m[1]+base_path+'/',source)
        source=re.sub(r"""(url\(["']?)/(?!/)""",lambda m:m[1]+base_path+'/',source)
        source=source.replace('content="/assets/','content="'+base_path+'/assets/')
    file.write_text(source,encoding='utf-8')
(dist/'.nojekyll').touch()
urls=['']+[r+'/' for r in routes]
sitemap='<?xml version="1.0" encoding="UTF-8"?>'+nl+'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+nl+''.join('<url><loc>'+escape(site_url+'/'+r)+'</loc></url>'+nl for r in urls)+'</urlset>'+nl
(dist/'sitemap.xml').write_text(sitemap,encoding='utf-8')
(dist/'robots.txt').write_text('User-agent: *'+nl+'Allow: /'+nl+'Sitemap: '+site_url+'/sitemap.xml'+nl,encoding='utf-8')
print(f'Built {len(files)} HTML documents. Homepage, assets and local links validated. Base path: {base_path or "/"}')
