/* Shared search for the header on every inner page. Uses /assets/search-index.json. */
(function () {
  var form = document.querySelector('.nx-search');
  if (!form) return;
  var input = form.querySelector('input');
  var box = form.querySelector('.nx-suggest');
  var lang = (document.documentElement.lang || 'en').slice(0, 2) === 'ne' ? 'ne' : 'en';
  var data = null, loading = null, act = -1, shown = [];
  function load() {
    if (data) return Promise.resolve(data);
    if (!loading) loading = fetch('/assets/search-index.json').then(function (r) { return r.json(); })
      .then(function (j) { data = j[lang] || []; return data; }).catch(function () { data = []; return data; });
    return loading;
  }
  function norm(s) { return (s || '').toLowerCase(); }
  function find(q) {
    q = norm(q).trim();
    if (!q) return [];
    var terms = q.split(/\s+/);
    var out = [];
    data.forEach(function (e) {
      var title = norm(e.t + ' ' + e.n), hay = title + ' ' + norm(e.k + ' ' + e.c);
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        if (hay.indexOf(terms[i]) < 0) { score = -1; break; }
        score += title.indexOf(terms[i]) >= 0 ? 3 : 1;
      }
      if (score > 0) out.push([score, e]);
    });
    out.sort(function (a, b) { return b[0] - a[0]; });
    return out.slice(0, 8).map(function (x) { return x[1]; });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function render() {
    shown = find(input.value); act = -1;
    if (!input.value.trim()) { box.hidden = true; box.innerHTML = ''; return; }
    box.innerHTML = shown.length ? shown.map(function (e) {
      return '<a href="' + esc(e.u) + '"><span class="nx-t">' + esc(e.t) + '</span><span class="nx-m">' + esc(e.c) + (e.x ? ' · thenepal.io' : '') + '</span></a>';
    }).join('') : '<div class="nx-none">' + (lang === 'ne' ? 'कुनै चिन्ह भेटिएन। अर्को शब्द प्रयास गर्नुहोस्।' : 'No symbols found. Try another word.') + '</div>';
    box.hidden = false;
  }
  function mark() {
    var links = box.querySelectorAll('a');
    links.forEach(function (a, i) { a.classList.toggle('nx-act', i === act); });
  }
  input.addEventListener('input', function () { load().then(render); });
  input.addEventListener('focus', function () { load(); if (input.value.trim()) load().then(render); });
  input.addEventListener('keydown', function (e) {
    var n = shown.length;
    if (e.key === 'ArrowDown' && n) { e.preventDefault(); act = (act + 1) % n; mark(); }
    else if (e.key === 'ArrowUp' && n) { e.preventDefault(); act = (act - 1 + n) % n; mark(); }
    else if (e.key === 'Escape') { box.hidden = true; input.blur(); }
    else if (e.key === 'Enter' && act >= 0 && shown[act]) { e.preventDefault(); location.href = shown[act].u; }
  });
  form.addEventListener('submit', function (e) {
    var q = input.value.trim();
    if (!q) { e.preventDefault(); input.focus(); return; }
    if (data) { var r = find(q); if (r.length === 1) { e.preventDefault(); location.href = r[0].u; } }
    /* otherwise the form submits to the hub: /?q=... or /ne/?q=... */
  });
  document.addEventListener('click', function (e) { if (!form.contains(e.target)) box.hidden = true; });
  document.addEventListener('keydown', function (e) {
    var t = (e.target.tagName || '').toLowerCase();
    if (e.key === '/' && t !== 'input' && t !== 'textarea' && !e.target.isContentEditable) { e.preventDefault(); input.focus(); }
  });
})();
