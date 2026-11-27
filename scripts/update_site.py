"""One-off: shared nav/footer updates, founder portrait, and the Books page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
NAV = ('<nav id="navigation" aria-label="Main navigation"><a href="/about/">About</a><a href="/wellbeing/">Wellbeing</a>'
       '<a href="/programs/">Programmes</a><a href="/events.html">Events</a><a href="/books/">Books</a>'
       '<a href="/founder/">Dr Sadhna Dixit</a><a href="/blog.html">Journal</a><a class="nav-cta" href="/contact/">Enquire</a></nav>')
PORTRAIT = '<img class="portrait" src="/assets/img/founder-portrait.jpg" alt="Dr Sadhna Dixit" width="520" height="626">'

for f in root.glob('*.html'):
    s = f.read_text(encoding='utf-8')
    s = re.sub(r'<nav id="navigation".*?</nav>', NAV, s, count=1, flags=re.S)
    s = s.replace('style.css?v=20261126', 'style.css?v=20261127')
    s = s.replace('<a href="/events.html">Events</a><a href="/contact/">Contact</a></div>',
                  '<a href="/events.html">Events</a><a href="/books/">Books</a><a href="/contact/">Contact</a></div>')
    s = re.sub(r'<div class="founder-portrait-placeholder".*?</div>', PORTRAIT, s, flags=re.S)
    f.write_text(s, encoding='utf-8', newline='\n')

c = (root / 'contact.html').read_text(encoding='utf-8')
books = re.sub(r'<title>.*?</title>', '<title>Books | World Wellbeing Forum</title>', c, count=1)
books = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="Books on wellbeing and naturopathy by Dr Sadhna Dixit, founder of the World Wellbeing Forum.">', books, count=1)
books = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Books | World Wellbeing Forum">', books, count=1)
books = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Books on wellbeing and naturopathy by Dr Sadhna Dixit.">', books, count=1)
main = '''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">BOOKS</p><h1>Books by Dr Sadhna Dixit</h1><p class="lead">Dr Sadhna Dixit has written five books on wellbeing and naturopathy, drawing on 25 years of yoga practice and her work as a qualified naturopath.</p></div></section>
<section class="section wrap founder-bio"><img class="portrait" src="/assets/img/founder-portrait.jpg" alt="Dr Sadhna Dixit" width="520" height="626" loading="lazy"><div><p class="eyebrow">FEATURED</p><h2>A Cure to Cancer by Naturopathy</h2><p>One of five books by Sadhna on wellbeing and naturopathy, written as part of her work in alternative medicine and holistic health.</p><p>The remaining titles will be listed here as they are confirmed. Please <a class="text-link" href="/contact/">get in touch</a> to ask about the books or to arrange a talk.</p><p class="small-note">Books describe the author’s perspective on naturopathy and wellbeing. They are not a substitute for professional medical advice, diagnosis or treatment.</p></div></section></main>'''
books = re.sub(r'<main id="main">.*?</main>', lambda m: main, books, count=1, flags=re.S)
(root / 'books.html').write_text(books, encoding='utf-8', newline='\n')

b = root / 'scripts' / 'build.py'
t = b.read_text(encoding='utf-8')
if "'books'" not in t:
    t = t.replace("'contact','programs']", "'contact','programs','books']")
    b.write_text(t, encoding='utf-8', newline='\n')
print('done')
