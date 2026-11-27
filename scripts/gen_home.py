"""One-off generator for the redesigned homepage (index.html)."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
s = (root / 'index.html').read_text(encoding='utf-8')
head = s[:s.index('<main id="main">')]
foot = s[s.index('</main>') + 7:]
head = head.replace('style.css?v=20261126', 'style.css?v=20261127').replace('content="/assets/logo.svg"', 'content="/assets/img/hike-coast.jpg"')


def ic(p):
    return ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round">' + p + '</svg>')


I = {
    'Physical': ic('<circle cx="14" cy="4.5" r="2"/><path d="M6 21l4-7 3 2 3-5-3-3-4 1-3 3M13 16l2 5"/>'),
    'Mental': ic('<path d="M12 21c-5-1-8-4-8-9a8 8 0 0116 0c0 5-3 8-8 9zM9 10c1-2 5-2 6 0M9 14c1 1 5 1 6 0"/>'),
    'Emotional': ic('<path d="M12 20s-8-5-8-11a4.5 4.5 0 018-2.5A4.5 4.5 0 0120 9c0 6-8 11-8 11z"/>'),
    'Social': ic('<circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20c0-4 3-6 6-6s6 2 6 6M15 14c3 0 6 1.5 7 5"/>'),
    'Spiritual': ic('<path d="M12 21c0-9 4-14 9-15 0 8-3 13-9 15zM12 21C12 13 8 9 3 9c0 7 3 10 9 12z"/>'),
    'Financial': ic('<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3 3 7 3s7-1.3 7-3v-6"/>'),
    'Digital': ic('<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 20h20"/>'),
    'Professional': ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 011-1h4a1 1 0 011 1v2M3 13h18"/>'),
}
dims = [
    ('Physical', 'Movement, nourishment, rest, sleep and preventive care.'),
    ('Mental', 'Focus, learning, resilience, clarity and asking for support.'),
    ('Emotional', 'Self-awareness, self-compassion and healthy expression.'),
    ('Social', 'Family, friendship, belonging and supportive communities.'),
    ('Spiritual', 'Meaning, values, reflection, connection and inner peace.'),
    ('Financial', 'Knowledge, planning, stability and confidence.'),
    ('Digital', 'Intentional technology use, boundaries and time offline.'),
    ('Professional', 'Purposeful work, healthy culture and work-life integration.'),
]
strip = ''.join(f'<a href="/wellbeing/"><span class="ico">{I[n]}</span>{n}</a>' for n, _ in dims)
cards = ''.join(f'<article><span class="ico">{I[n]}</span><h3>{n}</h3><p>{d}</p></article>' for n, d in dims)

main = f'''<main id="main">
<section class="hero hero-v2"><img class="hero-photo" src="/assets/img/hike-coast.jpg" alt="Friends walking together along a coastal path at sunrise"><div class="hero-shade"></div><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">PEOPLE · WORK · FAMILY · COMMUNITY · PLANET</p><h1>World Wellbeing Forum</h1><p class="hero-sub">Holistic wellbeing for individuals, families, workplaces and communities.</p><p class="hero-lead">Founded by Dr Sadhna Dixit to help people build health, happiness, balance and lasting wellbeing through yoga, meditation, mindfulness, naturopathy, mentoring and practical programmes.</p><div class="actions"><a class="button button-gold" href="/programs/">Our programmes →</a><a class="button button-ghost" href="/founder/">About Dr Sadhna Dixit</a></div></div><aside class="hero-card"><img src="/assets/img/sadhna-portrait.jpg" alt="Dr Sadhna Dixit" width="720" height="960"><div><h2>Dr Sadhna Dixit</h2><p>Author · Public speaker · Naturopath · Yoga teacher · Wellbeing mentor</p><blockquote>“If you can change your mind, you can change anything.”</blockquote></div></aside></div></section>
<nav class="dim-strip" aria-label="Dimensions of wellbeing"><div class="wrap">{strip}</div></nav>
<section class="section wrap what-is"><div class="what-copy"><p class="eyebrow">WHAT IS WELLBEING?</p><h2>A state of balance in body, mind and life.</h2><p class="lead">Wellbeing is a dynamic state of health, balance and contentment in your body, mind, relationships and environment — the ability to cope, grow, connect and thrive in daily life.</p><a class="text-link" href="/wellbeing/">Explore the dimensions of wellbeing →</a></div><div class="dimension-grid compact">{cards}</div></section>
<section class="feature-section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">HOW WE PROMOTE WELLBEING</p><h2>Learn · practise · grow</h2></div><p>Programmes for individuals, families, schools and organisations in New Zealand, India and Ireland.</p></div><div class="offer-grid"><article><img src="/assets/img/yoga-garden.jpg" alt="Yoga and meditation in a sunlit garden" loading="lazy"><div><h3>Yoga &amp; meditation</h3><p>Daily practices that build focus, inner strength, energy and lasting calm — a strong, balanced and flexible mind.</p><a class="text-link" href="/programs/">Learn more →</a></div></article><article><img src="/assets/img/hike-sunset.jpg" alt="Friends walking together at sunset" loading="lazy"><div><h3>Work-life balance</h3><p>Time and energy management, mindful productivity, stress reduction and goal alignment.</p><a class="text-link" href="/wellbeing/#work-life">Learn more →</a></div></article><article><img src="/assets/img/community-garden.jpg" alt="Neighbours sharing fresh produce at a community garden" loading="lazy"><div><h3>Family, friends &amp; community</h3><p>Family workshops, couples and parenting programmes and community-building activities.</p><a class="text-link" href="/wellbeing/">Learn more →</a></div></article></div></div></section>
<section class="section wrap topics"><article><h3>Mental health &amp; inner peace</h3><p>Meditation, breathing practices, journaling and nature-based therapies to overcome anxiety and burnout, improve sleep, and build confidence, clarity and emotional intelligence.</p></article><article><h3>Wellbeing at work</h3><p>Employee wellness programmes, corporate retreats, leadership resilience training and burnout prevention for healthier organisations.</p></article><article><h3>Financial, physical &amp; digital</h3><p>Money mindset and planning; movement, posture, sleep and mindful eating; tech-free routines, focus training and healthy device use.</p></article><article><h3>1-on-1 mentoring</h3><p>Personal coaching to manage stress and anxiety, find purpose and stay focused — for long-term wellbeing, happiness and success.</p></article><p class="small-note topics-note">Wellbeing education and coaching are not a substitute for medical or mental-health care.</p></section>
<section class="founder-feature"><div class="wrap founder-layout"><img class="portrait" src="/assets/img/sadhna-portrait.jpg" alt="Dr Sadhna Dixit" loading="lazy" width="720" height="960"><div><p class="eyebrow">FOUNDER &amp; CEO</p><h2>About Dr Sadhna Dixit</h2><p class="lead">Passionate about helping people realise their full potential through work-life integration and wellbeing.</p><p>An author, public speaker, alternative medicine advocate and qualified naturopath and yoga teacher, Sadhna has practised yoga for 25 years, learning while living in India and returning regularly to the Himalayas. She is CEO of the World Wellbeing Forum (New Zealand) and Director of Spiritual Earth (Ireland) and Fernleaf Ltd (New Zealand), and has organised the Rejuvenate India events with 500+ participants.</p><div class="actions"><a class="button button-light" href="/founder/">Read full profile →</a><a class="hero-link" href="/books/">Her books ↗</a></div></div></div></section>
<section class="testimonial"><div class="wrap"><p class="eyebrow">KIND WORDS</p><blockquote>“Highly recommend… a game changer. Sadhna is a gifted mentor — if you are ready to get focused and clear about your goals, or to understand your strengths and learn tools to avoid your pitfalls, then this is for you. So insightful.”</blockquote></div></section>
<section class="closing-section"><div class="wrap"><p class="eyebrow">START WHERE YOU ARE</p><h2>Small, meaningful changes<br>can shape a healthier life.</h2><p>Explore programmes, events and mentoring, or get in touch about working together.</p><a class="button button-light" href="/contact/">Connect with the Forum →</a></div></section></main>'''
(root / 'index.html').write_text(head + main + foot, encoding='utf-8', newline='\n')
print('ok')
