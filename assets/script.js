const toggle = document.querySelector('.menu-toggle');
const navigation = document.getElementById('navigation');
function closeMenu() { navigation?.classList.remove('open'); toggle?.setAttribute('aria-expanded', 'false'); }
toggle?.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); navigation.classList.toggle('open', open); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
navigation?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
matchMedia('(min-width: 961px)').addEventListener('change', closeMenu);
document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
const interest = new URLSearchParams(location.search).get('interest');
const select = document.querySelector('select[name="interest"]');
if (select && [...select.options].some(option => option.value === interest)) select.value = interest;
// Preserve Netlify Forms on the existing host; private/local previews have no form backend.
const preview = /(^localhost$|^127\.0\.0\.1$|\.chatgpt\.site$)/.test(location.hostname);
document.querySelectorAll('form[data-netlify]').forEach(form => {
 if (preview) form.querySelector('.form-status').textContent = 'This preview does not send submissions. The contact service must be connected before enquiries can be received.';
 form.addEventListener('submit', event => {
  if (preview) { event.preventDefault(); form.querySelector('.form-status').textContent = 'Your message has not been sent. Submissions are unavailable in this preview.'; }
 });
});
