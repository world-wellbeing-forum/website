"""One-off: fill Journal, Events and Contact pages."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
EMAIL = 'sadhna@sadhnadixit.com'


def swap_main(name, main, title=None, desc=None):
    p = root / name
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'<main id="main">.*?</main>', lambda m: main, s, count=1, flags=re.S)
    if title:
        s = re.sub(r'<title>.*?</title>', f'<title>{title} | World Wellbeing Forum</title>', s, count=1)
        s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title} | World Wellbeing Forum">', s, count=1)
    if desc:
        s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
        s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', s, count=1)
    p.write_text(s, encoding='utf-8', newline='\n')


journal = '''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">JOURNAL</p><h1>Highlights from Dr Sadhna Dixit</h1><p class="lead">Moments, ideas and milestones from Sadhna’s work in wellbeing, yoga, meditation and naturopathy.</p></div></section>
<section class="section wrap"><div class="journal-grid">
<article class="post"><img src="/assets/img/yoga-garden.jpg" alt="Yoga and meditation in a sunlit garden" loading="lazy"><div><p class="eyebrow">PRACTICE</p><h2>25 years of yoga</h2><p>Sadhna learned yoga while living in India and has practised for 25 years. She teaches yoga and meditation regularly and travels back to India to spend time in the Himalayas, deepening her own practice and renewing her teaching.</p></div></article>
<article class="post"><img src="/assets/img/hike-sunset.jpg" alt="Friends walking together at sunset" loading="lazy"><div><p class="eyebrow">PHILOSOPHY</p><h2>“If you can change your mind, you can change anything”</h2><p>Modern life is full of weapons of mass distraction. Sadhna’s approach is to build the skills to find the off-button, relax and focus, developing a strong, balanced and flexible mind.</p></div></article>
<article class="post"><img src="/assets/img/community-garden.jpg" alt="Neighbours sharing fresh produce at a community garden" loading="lazy"><div><p class="eyebrow">EVENTS</p><h2>Rejuvenate India</h2><p>A celebration and promotion of wellbeing with more than 500 participants, on the themes of Wellbeing at Work and Wellbeing for All.</p><a class="text-link" href="/events.html">See events →</a></div></article>
<article class="post"><img src="/assets/img/hike-coast.jpg" alt="Friends walking along a coastal path" loading="lazy"><div><p class="eyebrow">BACKGROUND</p><h2>From emergency response to wellbeing</h2><p>Before focusing on wellbeing, Sadhna worked in international emergency response and development programming, responding to man-made and natural disasters in New Zealand and Asia.</p><a class="text-link" href="/founder/">Read her story →</a></div></article>
<article class="post"><div class="post-text"><p class="eyebrow">AUTHOR</p><h2>Five books on wellbeing and naturopathy</h2><p>Sadhna is the author of five books, including <em>A Cure to Cancer by Naturopathy</em>. She has become a well-known voice in alternative medicine through her books and videos.</p><a class="text-link" href="/books/">About the books →</a></div></article>
<article class="post"><div class="post-text"><p class="eyebrow">WORKING TOGETHER</p><h2>Programmes for people and organisations</h2><p>Sadhna delivers wellbeing programmes for businesses, Chambers of Commerce, entrepreneurs, schools and individuals, and offers mentoring, life coaching and one-to-one stress support.</p><a class="text-link" href="/programs/">View programmes →</a></div></article>
</div><p class="small-note">Stories and updates will be added here as they are shared.</p></section></main>'''

events = '''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">EVENTS</p><h1>Events &amp; opportunities</h1><p class="lead">Forums, workshops, retreats and rejuvenation programmes across New Zealand, India and Ireland — for individuals, families, workplaces and communities.</p></div></section>
<section class="section wrap"><div class="section-heading"><div><p class="eyebrow">HIGHLIGHT</p><h2>Rejuvenate India</h2></div></div><div class="founder-bio"><img class="wide-photo flat" src="/assets/img/community-garden.jpg" alt="Community gathering around fresh produce" loading="lazy"><div><p class="lead">A celebration and promotion of wellbeing with more than 500 participants.</p><p>Organised by Dr Sadhna Dixit, the Rejuvenate India events centred on two themes: <strong>Wellbeing at Work</strong> and <strong>Wellbeing for All</strong>, bringing people together around yoga, meditation and practical ideas for healthier lives.</p></div></div></section>
<section class="feature-section"><div class="wrap"><p class="eyebrow">WHAT WE RUN</p><h2>Ways to take part</h2><div class="columns story"><article><h3>Workshops &amp; talks</h3><p>Stress management, mindful productivity and emotional intelligence for teams, schools and community groups.</p></article><article><h3>Yoga &amp; meditation sessions</h3><p>Group practices to build focus, calm and inner strength, led by a teacher with 25 years of practice.</p></article><article><h3>Retreats &amp; summits</h3><p>Rejuvenation camps and forums in New Zealand, India and Ireland.</p></article><article><h3>Corporate &amp; school programmes</h3><p>Tailored wellbeing programmes for businesses, Chambers of Commerce, entrepreneurs and schools.</p></article></div></div></section>
<section class="section wrap"><h2>Upcoming events</h2><p class="lead">No dates are published here yet. To hear about upcoming events, or to host a talk, workshop or programme for your organisation, get in touch.</p><p><a class="button" href="/contact/">Enquire about events →</a> &nbsp; <a class="text-link" href="mailto:%s">%s</a></p></section></main>''' % (EMAIL, EMAIL)

contact = '''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">GET IN TOUCH</p><h1>Let’s start a conversation.</h1><p class="lead">For enquiries about wellbeing programmes, yoga and meditation, workplace workshops, mentoring, speaking, events or partnerships, email Dr Sadhna Dixit directly or use the form.</p></div></section>
<section class="section wrap contact-panel"><div><h2>Work with us</h2><p>We welcome enquiries from individuals, businesses, schools, Chambers of Commerce, community groups and organisations interested in wellbeing.</p><p><strong>Email</strong><br><a class="text-link" href="mailto:%(e)s">%(e)s</a></p><p><strong>Based in</strong><br>New Zealand, working with people and organisations in New Zealand, India and Ireland.</p><div class="contact-note"><h3>Enquiry areas</h3><ul><li>Wellbeing at work</li><li>Yoga &amp; meditation</li><li>Mentoring &amp; personal development</li><li>Speaking &amp; events</li><li>Partnerships &amp; collaborations</li></ul></div></div>
<form id="enquiry" class="contact-form" action="mailto:%(e)s" method="post" enctype="text/plain"><h2>Send an enquiry</h2><label>Your name<input name="name" required autocomplete="name"></label><label>Your email<input type="email" name="email" required autocomplete="email"></label><label>I’m interested in<select name="topic"><option>Wellbeing at work</option><option>Yoga &amp; meditation</option><option>Mentoring &amp; personal development</option><option>Speaking &amp; events</option><option>Partnerships &amp; collaborations</option><option>Something else</option></select></label><label>Message<textarea name="message" rows="5" required></textarea></label><button class="button" type="submit">Send enquiry</button><p class="small-note">This opens your email app with the message ready to send to %(e)s. Wellbeing programmes are not a substitute for medical or mental-health care.</p></form></section></main>''' % {'e': EMAIL}

swap_main('blog.html', journal, 'Journal', 'Highlights from Dr Sadhna Dixit: yoga, wellbeing, Rejuvenate India, her books and her work.')
swap_main('events.html', events, 'Events', 'Wellbeing events, workshops and retreats from the World Wellbeing Forum, including Rejuvenate India.')
swap_main('contact.html', contact, 'Contact', 'Contact Dr Sadhna Dixit and the World Wellbeing Forum about programmes, workshops, mentoring, speaking and events.')

(root / 'assets' / 'script.js').write_text(
    (root / 'assets' / 'script.js').read_text(encoding='utf-8').rstrip('\n') +
    "\ndocument.getElementById('enquiry')?.addEventListener('submit',e=>{e.preventDefault();const f=e.target,d=new FormData(f);const body=`Name: ${d.get('name')}\\nEmail: ${d.get('email')}\\nInterested in: ${d.get('topic')}\\n\\n${d.get('message')}`;location.href=`mailto:"
    + EMAIL + "?subject=${encodeURIComponent('Website enquiry: '+d.get('topic'))}&body=${encodeURIComponent(body)}`});\n",
    encoding='utf-8', newline='\n')

css = '''
.journal-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:28px;margin-bottom:28px}.post{background:#fff;border:1px solid var(--line);display:flex;flex-direction:column}.post img{width:100%;height:230px;object-fit:cover;display:block}.post>div{padding:24px}.post h2{font-size:1.6rem;margin-bottom:.6rem}.post p{color:var(--muted)}.post .text-link{display:inline-block;margin-top:6px}.post-text{background:var(--cream)}.post-text,.post:has(.post-text){background:var(--cream)}.wide-photo.flat{margin-top:0;max-height:none;height:100%;min-height:260px}
.contact-form{display:grid;gap:16px;align-content:start;background:var(--cream);padding:34px}.contact-form h2{margin-bottom:.4rem}.contact-form label{display:grid;gap:6px;font-weight:700;font-size:.9rem}.contact-form input,.contact-form select,.contact-form textarea{font:inherit;font-weight:400;padding:12px;border:1px solid var(--line);border-radius:2px;background:#fff;color:var(--ink)}.contact-form input:focus,.contact-form select:focus,.contact-form textarea:focus{outline:2px solid var(--green);outline-offset:1px}.contact-form .button{justify-self:start;cursor:pointer}.contact-panel .contact-note{margin-top:24px}
@media(max-width:760px){.journal-grid{grid-template-columns:1fr}}
'''
with open(root / 'assets' / 'style.css', 'a', encoding='utf-8', newline='\n') as f:
    f.write(css)
print('ok')
