#!/usr/bin/env python3
"""Original infographic/hero images for the data pages. Every image carries the @thenepal.io watermark.
Data comes from scripts/morepages2_content.py facts (see sources there). Output: photos/*.webp"""
import os, io
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRIM, BLUE, NAVY, CREAM = '#C8102E', '#003893', '#0B1B3F', '#FBF4E8'
CSS = f'''*{{box-sizing:border-box;margin:0}}body{{font-family:"DejaVu Sans","Liberation Sans",Arial,sans-serif;color:#fff}}
.wm{{position:absolute;right:28px;bottom:20px;font-size:30px;font-weight:700;color:#fff;opacity:.82;letter-spacing:.5px;text-shadow:0 1px 3px rgba(0,0,0,.45)}}
.hero{{width:1760px;height:680px;position:relative;overflow:hidden;background:linear-gradient(135deg,{NAVY} 0%,#13306b 55%,{BLUE} 100%)}}
.hero:before{{content:"";position:absolute;right:-120px;top:-160px;width:760px;height:1000px;background:{CRIM};opacity:.92;clip-path:polygon(0 0,100% 0,100% 100%,0 100%,40% 55%)}}
.hero .in{{position:absolute;left:410px;width:940px;top:0;bottom:60px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.k{{font-size:28px;letter-spacing:5px;text-transform:uppercase;color:#ffd9de;font-weight:700}}
.big{{font-size:190px;font-weight:800;line-height:1;margin:10px 0}}
h1{{font-size:60px;line-height:1.05;font-weight:800;margin:14px 0}}
.sub{{font-size:33px;opacity:.92;max-width:900px;line-height:1.3}}
.chart{{width:1200px;height:675px;position:relative;background:{CREAM};color:#1d2433;padding:34px 44px}}
.chart h2{{font-size:46px;font-weight:800;color:{NAVY}}}.chart .s{{font-size:27px;color:#5a6378;margin:6px 0 18px}}
.chart .wm{{color:{NAVY};text-shadow:none;opacity:.7;font-size:32px}}
.row{{display:flex;align-items:center;margin:8px 0;font-size:28px}}.lab{{width:330px;font-weight:600;text-align:right;padding-right:14px}}
.bar{{height:34px;border-radius:0 6px 6px 0;background:{CRIM}}}.val{{padding-left:10px;font-weight:700;color:{NAVY}}}
'''
def hero(big, kicker, title, sub):
    return f'<style>{CSS}</style><div class="hero"><div class="in"><div class="k">{kicker}</div>' + (f'<div class="big">{big}</div>' if big else '') + f'<h1>{title}</h1><div class="sub">{sub}</div></div><div class="wm" style="font-size:34px;right:auto;left:880px;transform:translateX(-50%);bottom:26px">@thenepal.io</div></div>'
def chart(title, sub, body):
    return f'<style>{CSS}</style><div class="chart"><h2>{title}</h2><div class="s">{sub}</div>{body}<div class="wm">@thenepal.io</div></div>'
def hbars(rows, maxv, w=700, color=CRIM):
    out = ''
    for lab, v, txt in rows:
        out += f'<div class="row"><div class="lab">{lab}</div><div class="bar" style="width:{int(w*v/maxv)}px;background:{color}"></div><div class="val">{txt}</div></div>'
    return out
parks = [('Shey Phoksundo (2084 NS)',0,0)]
PARKS = [('Shey Phoksundo', 2712, '1984'), ('Langtang', 1710, '1976'), ('Makalu Barun', 1500, '1992'), ('Sagarmatha', 1148, '1976'), ('Bardiya', 968, '1988'),
         ('Chitwan', 952.63, '1973'), ('Chhayanath', 843.36, '2025'), ('Parsa', 637, '1984 / NP 2017'), ('Banke', 550, '2010'), ('Shuklaphanta', 305, '1976 / NP 2017'),
         ('Khaptad', 225, '1984'), ('Shivapuri Nagarjun', 159, '2002'), ('Rara', 106, '1976')]
def pk_body():
    rows = [(n, a, f'{a:,.0f} · {y}') for n, a, y in PARKS]
    return hbars(rows, 2712, 330)
def trend_body():
    data = [('2009', 121), ('2013', 198), ('2018', 235), ('2022', 355), ('2026', 429)]
    return hbars([(y, v, f'{v}') for y, v in data], 429, 560)
def park_body():
    data = [('Chitwan', 128, 145), ('Bardiya', 125, 112), ('Parsa', 41, 71), ('Banke', 25, 51), ('Shuklaphanta', 36, 50)]
    out = f'<div style="font-size:27px;margin:0 0 6px 344px"><span style="display:inline-block;width:18px;height:18px;background:#8fa0c8;vertical-align:-3px"></span> 2022 &nbsp; <span style="display:inline-block;width:18px;height:18px;background:{CRIM};vertical-align:-3px"></span> 2026</div>'
    for n, a, b in data:
        out += f'<div class="row" style="margin:12px 0 0"><div class="lab">{n}</div><div><div class="bar" style="width:{int(520*a/145)}px;background:#8fa0c8;height:30px;margin-bottom:4px"></div><div class="bar" style="width:{int(520*b/145)}px;height:30px"></div></div><div class="val" style="line-height:1.3">{a} → <b style="color:{CRIM}">{b}</b></div></div>'
    return out
def days_body():
    days = [('Jestha 15', 'Republic Day', 'Federal democratic republic declared (28 May 2008)'), ('Ashoj 3', 'National Day / Constitution Day', 'Constitution promulgated, 20 Sep 2015'),
            ('Poush 27', 'National Unity Day', 'Prithvi Narayan Shah birth anniversary'), ('Magh 16', "Martyrs' Day", 'Four martyrs remembered'), ('Falgun 7', 'Democracy Day', 'End of Rana rule, 2007 BS')]
    out = ''
    for i, (d, n, t) in enumerate(days):
        out += f'<div style="display:flex;align-items:center;margin:11px 0"><div style="width:210px;height:76px;background:{CRIM if i%2==0 else BLUE};color:#fff;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800">{d}</div><div style="margin-left:22px"><div style="font-size:36px;font-weight:800;color:{NAVY}">{n}</div><div style="font-size:25px;color:#5a6378">{t}</div></div></div>'
    return out
IMAGES = {
 'nepal_national_parks_hero': (hero('13', 'Nepal · Protected areas', 'National Parks of Nepal', 'Full list with area and year, updated for Chhayanath (2025)'), 1760, 680),
 'nepal_national_parks_area': (chart('National parks of Nepal by area (km²)', 'Area in km² · year established', pk_body()), 1200, 900),
 'nepal_tiger_census_hero': (hero('429', 'Nepal · National tiger census 2026', 'Tigers in Nepal', 'Record count released on Global Tiger Day, 29 July 2026'), 1760, 680),
 'nepal_tiger_census_trend': (chart('Nepal tiger count by census year', 'Wild tigers counted nationwide', trend_body()), 1200, 675),
 'nepal_tiger_census_parks': (chart('Tigers by park: 2022 vs 2026', 'Only Bardiya recorded a decline', park_body()), 1200, 675),
 'nepal_national_days_hero': (hero('', 'Nepal · Calendar', 'National Days of Nepal', 'Five days: dates, meaning and next dates'), 1760, 680),
 'nepal_national_days_calendar': (chart('Five national days in Bikram Sambat order', 'Each falls on the same BS date every year', days_body()), 1200, 675),
}

def trio_hero():
    cells = ''.join(f'<div style="flex:1;text-align:center"><div style="font-size:118px;font-weight:800;line-height:1">{n}</div><div style="font-size:27px;opacity:.92;margin-top:6px">{l}</div></div>' for n, l in [('429', 'tigers 2026'), ('752', 'rhinos 2021'), ('397', 'snow leopards 2025')])
    return f'<style>{CSS}</style><div class="hero"><div class="in"><div class="k">Nepal · Wildlife</div><h1 style="font-size:56px;margin:12px 0 26px">Wild animals in Nepal</h1><div style="display:flex;gap:10px;width:940px">{cells}</div></div><div class="wm" style="font-size:34px;right:auto;left:880px;transform:translateX(-50%);bottom:26px">@thenepal.io</div></div>'
def rhino_body():
    rows = [('Chitwan', 694, '694'), ('Bardiya', 38, '38'), ('Shuklaphanta', 17, '17'), ('Parsa', 3, '3')]
    return hbars(rows, 694, 560) + '<div style="font-size:30px;margin-top:22px;color:#0B1B3F"><b>Total 752</b> in 2021, up from 645 in 2015</div>'
def snow_body():
    return hbars([('Nepal', 397, '397'), ('India', 718, '718')], 718, 560, BLUE) + '<div style="font-size:26px;margin-top:22px;color:#5a6378;max-width:1050px">Nepal: DNPWC report, data 2015-2024. India: January 2024 status report, as cited by Down To Earth.</div>'
IMAGES.update({
 'nepal_rhino_count_hero': (hero('752', 'Nepal · Rhino census', 'Rhinos in Nepal', 'Last counted in 2021. Next census being redesigned.'), 1760, 680),
 'nepal_rhino_count_chart': (chart('Rhinos by park, 2021 census', 'Greater one-horned rhinoceros', rhino_body()), 1200, 470),
 'nepal_snow_leopard_hero': (hero('397', 'Nepal · Snow leopard survey', 'Snow Leopards in Nepal', 'First national estimate, released April 2025'), 1760, 680),
 'nepal_snow_leopard_chart': (chart('Snow leopard estimates: Nepal and India', 'Number of individuals', snow_body()), 1200, 470),
 'nepal_wildlife_counts_hero': (trio_hero(), 1760, 680),
})

if __name__ == '__main__':
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, (html, w, h) in IMAGES.items():
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.set_content(f'<body style="margin:0">{html}</body>')
            pg.add_style_tag(content=f'.chart{{height:{h}px!important}}')
            png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(ROOT, 'photos', name + '.webp'), quality=88, method=6)
            print(name)
        b.close()
