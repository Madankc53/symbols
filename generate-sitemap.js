const fs = require('fs');
const path = require('path');

// Configuration
const BASE_URL = 'https://symbols.thenepal.io';
const OUTPUT_DIR = '.';

// Page metadata with actual lastmod dates and image info
const pages = [
  {
    loc: '/',
    priority: '1.0',
    changefreq: 'weekly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_flag_nepal.webp', title: 'Flag of Nepal', caption: 'The national flag of Nepal' }
    ]
  },
  {
    loc: '/national-animal/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_animal_of_nepal.webp', title: 'Cow - National Animal of Nepal', caption: 'The sacred cow (Gai), national animal of Nepal' }
    ]
  },
  {
    loc: '/national-bird/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_bird_of_nepal.webp', title: 'Himalayan Monal - National Bird of Nepal', caption: 'Danphe, the Himalayan Monal' }
    ]
  },
  {
    loc: '/national-flower/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_flower_of_nepal.webp', title: 'Rhododendron - National Flower of Nepal', caption: 'Lali Gurans, the national flower of Nepal' }
    ]
  },
  {
    loc: '/national-tree/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_tree_of_nepal.webp', title: 'Peepal Tree - National Tree of Nepal', caption: 'The sacred Peepal tree' }
    ]
  },
  {
    loc: '/national-fish/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_fish_of_nepal.webp', title: 'Golden Mahseer - National Fish of Nepal', caption: 'Asala, the Golden Mahseer' }
    ]
  },
  {
    loc: '/national-butterfly/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_butterfly_of_nepal.webp', title: 'Krishna Peacock - National Butterfly of Nepal', caption: 'Krishna Peacock butterfly' }
    ]
  },
  {
    loc: '/national-flag/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_flag_nepal.webp', title: 'Flag of Nepal', caption: "The world's only non-rectangular national flag" }
    ]
  },
  {
    loc: '/national-anthem/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_anthem_of_nepal.webp', title: 'National Anthem of Nepal', caption: 'Sayaun Thunga Phulka' }
    ]
  },
  {
    loc: '/national-language/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_language_of_nepal.webp', title: 'Nepali Language', caption: 'Nepali, the official language of Nepal' }
    ]
  },
  {
    loc: '/national-color/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_color_of_nepal.webp', title: 'Crimson Red - National Colour of Nepal', caption: 'Crimson red, the national colour' }
    ]
  },
  {
    loc: '/national-dress/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_dress_of_nepal.webp', title: 'National Dress of Nepal', caption: 'Daura Suruwal and Gunyu Cholo' }
    ]
  },
  {
    loc: '/national-sport/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_sport_of_nepal.webp', title: 'Volleyball - National Sport of Nepal', caption: 'Volleyball, the official national sport' }
    ]
  },
  {
    loc: '/national-calendar/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_calendar_of_nepal.webp', title: 'Bikram Sambat - National Calendar of Nepal', caption: 'Bikram Sambat, the official calendar' }
    ]
  },
  {
    loc: '/national-dance/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_dance_of_nepal.webp', title: 'Deuda and Maruni - National Dance of Nepal', caption: 'Traditional Nepali folk dances' }
    ]
  },
  {
    loc: '/national-emblem/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_emblem_of_nepal.webp', title: 'National Emblem of Nepal', caption: 'The official national emblem of Nepal' }
    ]
  },
  {
    loc: '/national-monument/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_monument_nepal.webp', title: 'Dharahara Tower - National Monument of Nepal', caption: 'Dharahara Tower, Nepal\'s national monument' }
    ]
  },
  {
    loc: '/national-everest/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_everest_of_nepal.webp', title: 'Mount Everest - Sagarmatha', caption: 'Sagarmatha (Mt Everest), the highest peak' }
    ]
  },
  {
    loc: '/national-cave/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_cave_of_nepal.webp', title: 'Siddha Gufa - National Cave of Nepal', caption: 'Siddha Gufa, the largest cave in South Asia' }
    ]
  },
  {
    loc: '/national-museum/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/national_museum_nepal.webp', title: 'National Museum of Nepal', caption: 'The National Museum of Nepal in Kathmandu' }
    ]
  },
  {
    loc: '/national-currency/',
    priority: '0.8',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: [
      { loc: '/photos/nepal_currency_of_nepal.webp', title: 'Nepalese Rupee - National Currency', caption: 'Nepalese Rupee banknotes and coins' }
    ]
  },
  // Nepali versions
  {
    loc: '/ne/',
    priority: '0.8',
    changefreq: 'weekly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-animal/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-bird/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-flower/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-tree/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-fish/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-butterfly/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-flag/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-anthem/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-language/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-color/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-dress/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-sport/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-calendar/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-dance/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-emblem/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-monument/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-everest/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-cave/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-museum/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  },
  {
    loc: '/ne/national-currency/',
    priority: '0.7',
    changefreq: 'monthly',
    lastmod: '2026-07-21',
    images: []
  }
];

// Helper: get alternate language URLs
function getAlternates(loc) {
  if (loc === '/') {
    return [
      { lang: 'en', href: `${BASE_URL}/` },
      { lang: 'ne', href: `${BASE_URL}/ne/` },
      { lang: 'x-default', href: `${BASE_URL}/` }
    ];
  }
  if (loc.startsWith('/ne/')) {
    const enLoc = loc.replace('/ne/', '/');
    return [
      { lang: 'en', href: `${BASE_URL}${enLoc}` },
      { lang: 'ne', href: `${BASE_URL}${loc}` },
      { lang: 'x-default', href: `${BASE_URL}${enLoc}` }
    ];
  }
  return [
    { lang: 'en', href: `${BASE_URL}${loc}` },
    { lang: 'ne', href: `${BASE_URL}/ne${loc}` },
    { lang: 'x-default', href: `${BASE_URL}${loc}` }
  ];
}

// Generate XML Sitemap
function generateXML() {
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
  xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n`;
  xml += `        xmlns:xhtml="http://www.w3.org/1999/xhtml"\n`;
  xml += `        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n`;

  for (const page of pages) {
    xml += `  <url>\n`;
    xml += `    <loc>${BASE_URL}${page.loc}</loc>\n`;
    xml += `    <lastmod>${page.lastmod}</lastmod>\n`;
    xml += `    <changefreq>${page.changefreq}</changefreq>\n`;
    xml += `    <priority>${page.priority}</priority>\n`;

    // Add hreflang alternates
    const alternates = getAlternates(page.loc);
    for (const alt of alternates) {
      xml += `    <xhtml:link rel="alternate" hreflang="${alt.lang}" href="${alt.href}"/>\n`;
    }

    // Add images
    for (const img of page.images) {
      xml += `    <image:image>\n`;
      xml += `      <image:loc>${BASE_URL}${img.loc}</image:loc>\n`;
      xml += `      <image:title>${escapeXml(img.title)}</image:title>\n`;
      xml += `      <image:caption>${escapeXml(img.caption)}</image:caption>\n`;
      xml += `    </image:image>\n`;
    }

    xml += `  </url>\n`;
  }

  xml += `</urlset>\n`;
  return xml;
}

// Generate HTML Sitemap
function generateHTML() {
  let html = `<!DOCTYPE html>\n<html lang="en">\n<head>\n`;
  html += `  <meta charset="UTF-8">\n`;
  html += `  <title>Sitemap - National Symbols of Nepal</title>\n`;
  html += `  <meta name="robots" content="noindex, follow">\n`;
  html += `  <style>\n`;
  html += `    body{font-family:system-ui,sans-serif;max-width:800px;margin:40px auto;padding:0 20px;color:#333;}\n`;
  html += `    h1{color:#7E2A2A;border-bottom:2px solid #D89B3C;padding-bottom:10px;}\n`;
  html += `    h2{color:#5C1E1E;margin-top:30px;font-size:1.1rem;}\n`;
  html += `    ul{list-style:none;padding:0;}\n`;
  html += `    li{margin:8px 0;padding:8px 12px;background:#f9f5f0;border-radius:6px;}\n`;
  html += `    a{color:#7E2A2A;text-decoration:none;font-weight:500;}\n`;
  html += `    a:hover{text-decoration:underline;}\n`;
  html += `    .lang{color:#888;font-size:.85rem;margin-left:8px;}\n`;
  html += `    .stats{background:#7E2A2A;color:#fff;padding:15px 20px;border-radius:8px;margin:20px 0;}\n`;
  html += `    .stats strong{font-size:1.3rem;}\n`;
  html += `  </style>\n</head>\n<body>\n`;
  html += `  <h1>📍 Sitemap — National Symbols of Nepal</h1>\n`;
  html += `  <div class="stats">\n`;
  html += `    <strong>${pages.length}</strong> pages indexed | Last updated: July 2026 | <a href="sitemap.xml" style="color:#D89B3C;">View XML Sitemap</a>\n`;
  html += `  </div>\n`;

  // English pages
  html += `  <h2>🇬🇧 English Pages</h2>\n  <ul>\n`;
  for (const page of pages.filter(p => !p.loc.startsWith('/ne/'))) {
    const name = page.loc === '/' ? 'Homepage' : page.loc.replace(/\/g, '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    html += `    <li><a href="${BASE_URL}${page.loc}">${name}</a> <span class="lang">(priority: ${page.priority})</span></li>\n`;
  }
  html += `  </ul>\n`;

  // Nepali pages
  html += `  <h2>🇳🇵 नेपाली पृष्ठहरू</h2>\n  <ul>\n`;
  for (const page of pages.filter(p => p.loc.startsWith('/ne/'))) {
    const name = page.loc === '/ne/' ? 'मुख्य पृष्ठ' : page.loc.replace('/ne/', '').replace(/\/g, '').replace(/-/g, ' ');
    html += `    <li><a href="${BASE_URL}${page.loc}">${name}</a> <span class="lang">(priority: ${page.priority})</span></li>\n`;
  }
  html += `  </ul>\n`;

  html += `  <p style="margin-top:40px;font-size:.85rem;color:#888;text-align:center;">\n`;
  html += `    © 2026 The Nepal · symbols.thenepal.io · Educational content\n`;
  html += `  </p>\n</body>\n</html>\n`;
  return html;
}

function escapeXml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

// Write files
fs.writeFileSync(path.join(OUTPUT_DIR, 'sitemap.xml'), generateXML());
fs.writeFileSync(path.join(OUTPUT_DIR, 'sitemap.html'), generateHTML());

console.log('✅ sitemap.xml generated with clean URLs, hreflang, and image sitemap');
console.log('✅ sitemap.html generated');
console.log(`📊 Total pages: ${pages.length}`);
