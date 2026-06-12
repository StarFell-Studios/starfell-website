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

  // ---------- The Vault: lightbox + wing-nav (vault.html) ----------
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const lbImg     = lightbox.querySelector('.lightbox-image');
    const lbTitle   = lightbox.querySelector('.lightbox-title');
    const lbMedium  = lightbox.querySelector('.lightbox-medium');
    const lbCaption = lightbox.querySelector('.lightbox-caption');
    const lbClose   = lightbox.querySelector('.lightbox-close');
    const lbPrev    = lightbox.querySelector('.lightbox-prev');
    const lbNext    = lightbox.querySelector('.lightbox-next');
    const frames    = Array.from(document.querySelectorAll('.frame'));
    let currentIdx  = -1;

    const openLightbox = (idx) => {
      const f = frames[idx];
      if (!f) return;
      currentIdx = idx;
      lbImg.src = f.getAttribute('href');
      lbImg.alt = f.dataset.title || '';
      lbTitle.textContent = f.dataset.title || '';
      lbMedium.textContent = f.dataset.medium || '';
      lbCaption.textContent = f.dataset.caption || '';
      lightbox.hidden = false;
      requestAnimationFrame(() => lightbox.classList.add('open'));
      document.body.classList.add('lightbox-open');
    };

    const closeLightbox = () => {
      lightbox.classList.remove('open');
      document.body.classList.remove('lightbox-open');
      setTimeout(() => { lightbox.hidden = true; lbImg.src = ''; }, 260);
    };

    const step = (delta) => openLightbox((currentIdx + delta + frames.length) % frames.length);

    frames.forEach((f, i) => {
      f.addEventListener('click', (e) => { e.preventDefault(); openLightbox(i); });
    });
    lbClose.addEventListener('click', closeLightbox);
    lbPrev.addEventListener('click', () => step(-1));
    lbNext.addEventListener('click', () => step(1));
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
      if (lightbox.hidden) return;
      if (e.key === 'Escape') closeLightbox();
      else if (e.key === 'ArrowLeft')  step(-1);
      else if (e.key === 'ArrowRight') step(1);
    });

    // Touch swipe — page through like a comic
    let touchStartX = null;
    lightbox.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].clientX;
    }, { passive: true });
    lightbox.addEventListener('touchend', (e) => {
      if (touchStartX === null) return;
      const dx = e.changedTouches[0].clientX - touchStartX;
      touchStartX = null;
      if (Math.abs(dx) > 40) step(dx > 0 ? -1 : 1);
    }, { passive: true });
  }

  // ---------- Sticky chip-nav active state on scroll ----------
  // Works for both .wing-chip / .wing (Museum) and .section-chip / .page-section (Story & Media).
  const sectionChips = document.querySelectorAll('.wing-chip, .section-chip');
  const sectionTargets = document.querySelectorAll('.wing, .page-section');
  if (sectionChips.length && sectionTargets.length && 'IntersectionObserver' in window) {
    const setActive = (id) => {
      sectionChips.forEach(c => c.classList.toggle('active', c.getAttribute('href') === `#${id}`));
    };
    const io = new IntersectionObserver((entries) => {
      const visible = entries.filter(e => e.isIntersecting)
                             .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]) setActive(visible[0].target.id);
    }, { rootMargin: '-30% 0px -55% 0px', threshold: [0, 0.1, 0.5] });
    sectionTargets.forEach(w => io.observe(w));
  }

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
