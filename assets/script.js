
function subscribe(e){ e.preventDefault(); alert('Thanks!'); return false; }
document.getElementById('menuToggle')?.addEventListener('click',()=>{
  document.getElementById('nav').classList.toggle('open')
});
