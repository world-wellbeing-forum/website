"""Validate local links and stage the static website for deployment."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import shutil
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
