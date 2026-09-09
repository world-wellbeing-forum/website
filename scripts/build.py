"""Validate local links and stage the static website for deployment."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import shutil
import os
import re
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]
routes=['about','our-work','health','environment','humanitarian','education-technology','global','founder','get-involved','contact']
# Flat HTML files are the editable source. Directory routes are generated.
for route in routes:
 folder=root/route
 folder.mkdir(exist_ok=True)
 shutil.copy2(root/(route+'.html'),folder/'index.html')
class Document(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.add(attrs['id'])
  for attr in ['href','src','action']:
   if attr in attrs:self.links.append(attrs[attr])
files=list(root.glob('*.html'))+[root/r/'index.html' for r in routes]
docs={}
for file in files:
 doc=Document();doc.feed(file.read_text());docs[file.resolve()]=doc
errors=[]
for file,doc in docs.items():
 for link in doc.links:
  url=urlsplit(link)
  if url.scheme or url.netloc:continue
  target=root/unquote(url.path).lstrip('/') if url.path.startswith('/') else file.parent/unquote(url.path) if url.path else file
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{file.name}: missing {link}')
  elif url.fragment and target.resolve() in docs and url.fragment not in docs[target.resolve()].ids:errors.append(f'{file.name}: missing anchor {link}')
if errors:raise SystemExit('\n'.join(errors))
dist=root/'dist'
if dist.exists():shutil.rmtree(dist)
dist.mkdir()
for file in root.glob('*.html'):shutil.copy2(file,dist/file.name)
for route in routes:shutil.copytree(root/route,dist/route)
shutil.copytree(root/'assets',dist/'assets')
for name in ['robots.txt','sitemap.xml']:shutil.copy2(root/name,dist/name)
print(f'Built {len(files)} pages. All local links, form actions and anchors resolve.')

# GitHub project sites live below /repository; other static hosts can use /.
base_path = os.environ.get('BASE_PATH', '').strip('/')
base_path = '/' + base_path if base_path else ''
site_url = os.environ.get('SITE_URL', 'https://world-wellbeing-forum.github.io/website').rstrip('/')
if not site_url.startswith(('https://', 'http://')):
 raise SystemExit('SITE_URL must be an absolute HTTP(S) URL')
for file in dist.rglob('*'):
 if file.suffix not in {'.html', '.css'}: continue
 text = file.read_text()
 if base_path:
  text = re.sub(r'((?:href|src|action)=[\"\'])/(?!/)', lambda m: m[1] + base_path + '/', text)
  text = re.sub(r'(url\([\"\']?)/(?!/)', lambda m: m[1] + base_path + '/', text)
  text = text.replace('content="/assets/', 'content="' + base_path + '/assets/')
 file.write_text(text)
(dist / '.nojekyll').touch()
(dist / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('<url><loc>' + escape(site_url + '/' + route) + '</loc></url>\n' for route in [''] + [r + '/' for r in routes]) + '</urlset>\n')
(dist / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + site_url + '/sitemap.xml\n')
print(f'Static output uses base path {base_path or "/"} and origin {site_url}')
