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

  // ---------- Vault search (every page) ----------
  initVaultSearch();
  initVaultArrival();

  function initVaultSearch() {
    const root = document.querySelector('[data-nav-search]');
    if (!root) return;
    const toggle  = root.querySelector('.nav-search-toggle');
    const input   = root.querySelector('.nav-search-input');
    const results = root.querySelector('.nav-search-results');
    if (!toggle || !input || !results) return;

    const MAX_RESULTS = 14;
    const onVault = /(^|\/)vault\.html$/.test(window.location.pathname) ||
                    document.getElementById('wing-1') !== null;

    let index = null;          // loaded entries
    let indexPromise = null;   // de-dupes the fetch
    let activeIdx = -1;        // keyboard-highlighted result
    let rendered = [];         // current result entries

    const escapeHtml = (s) => s.replace(/[&<>"']/g, c => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    ));

    const buildIndex = (data) => data.map(e => {
      const blob = [
        e.title, e.description, e.medium, e.section, e.sectionFull,
        e.exhibit, (e.characters || []).join(' '), (e.artTypes || []).join(' '),
        (e.tags || []).join(' ')
      ].join(' ').toLowerCase();
      return { e, blob };
    });

    // Lazily load the index once. Primary source is search-index.json (fetched
    // on GitHub Pages); if fetch is blocked or fails (e.g. opened over file://),
    // fall back to the embedded window.STARFELL_SEARCH_INDEX from search-index.js.
    const loadIndex = () => {
      if (indexPromise) return indexPromise;
      indexPromise = fetch('search-index.json')
        .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(data => { index = buildIndex(data); return index; })
        .catch(() => {
          const embedded = window.STARFELL_SEARCH_INDEX;
          index = Array.isArray(embedded) ? buildIndex(embedded) : [];
          return index;
        });
      return indexPromise;
    };

    const scoreEntry = (rec, terms, query) => {
      const { e, blob } = rec;
      // AND semantics: every term must appear somewhere in the entry.
      if (!terms.every(t => blob.includes(t))) return -1;
      const title = e.title.toLowerCase();
      const chars = (e.characters || []).join(' ').toLowerCase();
      const section = (e.section || '').toLowerCase();
      let score = 0;
      if (title.includes(query)) score += 12;
      if (title.startsWith(query)) score += 6;
      if (chars.includes(query)) score += 8;
      if (section.includes(query)) score += 5;
      terms.forEach(t => {
        if (title.includes(t)) score += 4;
        if (chars.includes(t)) score += 3;
        if (section.includes(t)) score += 2;
        score += 1; // term is present (guaranteed by AND filter)
      });
      return score;
    };

    const highlight = (text, terms) => {
      let out = escapeHtml(text);
      terms.forEach(t => {
        if (!t) return;
        const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
        out = out.replace(re, '<mark>$1</mark>');
      });
      return out;
    };

    const render = (query) => {
      const q = query.trim().toLowerCase();
      activeIdx = -1;
      if (!q) { hideResults(); return; }
      if (!index) {
        results.innerHTML = '<div class="nav-search-status">Loading the archive…</div>';
        showResults();
        return;
      }
      if (index.length === 0) {
        results.innerHTML = '<div class="nav-search-status">Search index unavailable.</div>';
        showResults();
        return;
      }
      const terms = q.split(/\s+/).filter(Boolean);
      const matches = [];
      for (const rec of index) {
        const s = scoreEntry(rec, terms, q);
        if (s >= 0) matches.push({ rec, s });
      }
      matches.sort((a, b) => b.s - a.s || a.rec.e.title.localeCompare(b.rec.e.title));
      rendered = matches.slice(0, MAX_RESULTS).map(m => m.rec.e);

      const total = matches.length;
      const count = total === 0
        ? 'No matches'
        : `${total} image${total === 1 ? '' : 's'}${total > rendered.length ? ' · showing ' + rendered.length : ''}`;

      let html = `<div class="nav-search-status">${count}</div>`;
      html += rendered.map((e, i) => {
        const meta = [e.section, e.medium].filter(Boolean)
          .map(escapeHtml).join('<span class="dot">·</span>');
        return `<a class="nav-search-result" href="vault.html#${e.id}" data-idx="${i}" role="option">
          <img class="nav-search-result-thumb" src="${escapeHtml(e.path)}" alt="" loading="lazy">
          <span class="nav-search-result-body">
            <span class="nav-search-result-title">${highlight(e.title, terms)}</span>
            <span class="nav-search-result-meta">${meta}</span>
          </span>
        </a>`;
      }).join('');
      results.innerHTML = html;
      showResults();
    };

    const showResults = () => results.classList.add('is-visible');
    const hideResults = () => { results.classList.remove('is-visible'); results.innerHTML = ''; rendered = []; activeIdx = -1; };

    const openSearch = () => {
      root.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      loadIndex().then(() => { if (input.value.trim()) render(input.value); });
      input.focus();
    };
    const closeSearch = () => {
      root.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      hideResults();
    };

    toggle.addEventListener('click', () => {
      if (root.classList.contains('open')) {
        if (input.value) { input.value = ''; hideResults(); }
        else closeSearch();
      } else {
        openSearch();
      }
    });

    let debounce;
    input.addEventListener('input', () => {
      clearTimeout(debounce);
      debounce = setTimeout(() => loadIndex().then(() => render(input.value)), 110);
    });

    const setActive = (idx) => {
      const items = results.querySelectorAll('.nav-search-result');
      if (!items.length) return;
      activeIdx = (idx + items.length) % items.length;
      items.forEach((el, i) => el.classList.toggle('is-active', i === activeIdx));
      items[activeIdx].scrollIntoView({ block: 'nearest' });
    };

    input.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown') { e.preventDefault(); setActive(activeIdx + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(activeIdx - 1); }
      else if (e.key === 'Enter') {
        const items = results.querySelectorAll('.nav-search-result');
        if (activeIdx >= 0 && items[activeIdx]) { e.preventDefault(); items[activeIdx].click(); }
      } else if (e.key === 'Escape') {
        if (input.value) { input.value = ''; hideResults(); }
        else closeSearch();
      }
    });

    // Intercept result clicks: stay on the page when already in the Vault.
    results.addEventListener('click', (e) => {
      const link = e.target.closest('.nav-search-result');
      if (!link) return;
      const id = link.getAttribute('href').split('#')[1];
      if (onVault && id) {
        e.preventDefault();
        closeSearch();
        input.value = '';
        gotoVaultItem(id);
      } else {
        closeSearch();
      }
    });

    // Close when clicking outside the search.
    document.addEventListener('click', (e) => {
      if (root.classList.contains('open') && !root.contains(e.target)) closeSearch();
    });
  }

  // Scroll to a Vault card and flash it. Shared by in-page search + hash arrival.
  function gotoVaultItem(id) {
    const el = document.getElementById(id);
    if (!el) return;
    try { if (history.replaceState) history.replaceState(null, '', '#' + id); }
    catch (_) { /* some environments reject replaceState; scrolling still works */ }
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    el.classList.remove('search-flash');
    void el.offsetWidth; // restart the animation
    el.classList.add('search-flash');
    el.addEventListener('animationend', () => el.classList.remove('search-flash'), { once: true });
  }

  // On vault.html, honor #vault-item-N on load and on hash changes.
  function initVaultArrival() {
    if (!document.getElementById('wing-1')) return;
    const fromHash = () => {
      const id = window.location.hash.slice(1);
      if (/^vault-item-\d+$/.test(id)) {
        // Wait a beat for layout/lazy images before scrolling.
        setTimeout(() => gotoVaultItem(id), 60);
      }
    };
    if (document.readyState === 'complete') fromHash();
    else window.addEventListener('load', fromHash);
    window.addEventListener('hashchange', fromHash);
  }
})();
