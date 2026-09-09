"""Exercise both hosting layouts and verify emitted links, CSS assets and metadata."""
import os
import re
import subprocess
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):
  super().__init__(); self.links = []
 def handle_starttag(self, tag, attrs):
  self.links.extend(value for key, value in attrs if key in {'href', 'src', 'action'} and value)

for base in ['', '/website']:
 origin = 'https://world-wellbeing-forum.github.io' + base
 subprocess.run([sys.executable, 'scripts/build.py'], cwd=root, env={**os.environ, 'BASE_PATH': base, 'SITE_URL': origin}, check=True)
 dist = root / 'dist'
 for file in dist.rglob('*'):
  if file.suffix == '.html':
   parser = Links(); parser.feed(file.read_text()); links = parser.links
  elif file.suffix == '.css':
   links = re.findall(r'url\([\"\']?([^\)\"\']+)', file.read_text())
  else: continue
  for link in links:
   url = urlsplit(link)
   if url.scheme or url.netloc or not url.path: continue
   if url.path.startswith('/'):
    assert url.path.startswith(base + '/'), (file, link, base)
    target = dist / url.path[len(base):].lstrip('/')
   else: target = file.parent / url.path
   if target.is_dir(): target = target / 'index.html'
   assert target.is_file(), (file, link, target)
 for loc in ET.parse(dist / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
  assert loc.text.startswith(origin + '/')
 assert (dist / '.nojekyll').exists()
 assert not (dist / '.openai').exists()
print('Both hosting layouts passed: emitted navigation, assets, form actions and sitemap.')
