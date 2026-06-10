// StarFell — site interactivity
// Restrained. Dread is slow.

(() => {
  'use strict';

  // ---------- Mobile nav ----------
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', links.classList.contains('open'));
    });
    // Close after tapping a link (mobile)
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('open'));
    });
  }

  // ---------- Character tabs ----------
  const tabs = document.querySelectorAll('.char-tab');
  const grids = document.querySelectorAll('.char-grid');

  const activateTab = (target, { scroll = true } = {}) => {
    const grid = document.getElementById(target);
    if (!grid || !grid.classList.contains('char-grid')) return false;
    tabs.forEach(t => t.classList.toggle('active', t.dataset.target === target));
    grids.forEach(g => g.classList.toggle('hidden', g.id !== target));
    if (scroll) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return true;
  };

  if (tabs.length && grids.length) {
    tabs.forEach(tab => {
      tab.addEventListener('click', () => activateTab(tab.dataset.target));
    });

    // Respect URL hash on initial load (#world-shakers, #voltaires, #supporting, #monsters)
    const hashLanding = () => {
      const hash = window.location.hash.slice(1);
      if (hash) activateTab(hash, { scroll: true });
    };
    if (document.readyState === 'complete') hashLanding();
    else window.addEventListener('load', hashLanding);

    // Also honor hash changes while the user is on the page
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.slice(1);
      if (hash) activateTab(hash);
    });
  }

  // ---------- Character bio expand ----------
  document.querySelectorAll('.char-card .more').forEach(btn => {
    btn.addEventListener('click', () => {
      const bio = btn.nextElementSibling;
      if (!bio) return;
      const isOpen = bio.classList.toggle('open');
      btn.textContent = isOpen ? '— Less' : '+ Read More';
    });
  });

  // ---------- Lazy-load helper (covers/backgrounds set via data-bg) ----------
  const lazyBg = document.querySelectorAll('[data-bg]');
  if ('IntersectionObserver' in window && lazyBg.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          el.style.backgroundImage = `url('${el.dataset.bg}')`;
          io.unobserve(el);
        }
      });
    }, { rootMargin: '200px' });
    lazyBg.forEach(el => io.observe(el));
  } else {
    lazyBg.forEach(el => { el.style.backgroundImage = `url('${el.dataset.bg}')`; });
  }
})();
