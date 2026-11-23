#!/usr/bin/env python3
"""Nepali (Devanagari) version of the all-symbols chart: photos/nepal_national_symbols_chart_ne.webp, 1612x1004, watermarked @thenepal.io.
Rendered in Chromium (proper Devanagari shaping) with Noto Sans Devanagari (OFL) from scripts/fonts. Needs photos/thumbs/*.webp from make_gallery_images.py."""
import os, io
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = [('national-flag', 'झण्डा'), ('national-anthem', 'राष्ट्रगान'), ('national-emblem', 'प्रतीक चिन्ह'), ('national-flower', 'फूल'), ('national-color', 'रङ'), ('national-animal', 'पशु'),
 ('national-bird', 'चरा'), ('national-language', 'भाषा'), ('national-sport', 'खेल'), ('national-fruit', 'फल'), ('national-calendar', 'पात्रो'), ('national-currency', 'मुद्रा'),
 ('national-tree', 'रूख'), ('national-fish', 'माछा'), ('national-butterfly', 'पुतली'), ('national-food', 'खाना'), ('national-weapon', 'हतियार'), ('national-dress', 'पोशाक'),
 ('national-dance', 'नृत्य'), ('national-monument', 'स्मारक'), ('national-cave', 'गुफा'), ('national-museum', 'संग्रहालय'), ('national-everest', 'अग्लो शिखर')]
F = os.path.join(ROOT, 'scripts', 'fonts')
cells = ''.join(f'<div class="c"><img src="file://{ROOT}/photos/thumbs/{s}.webp"><span>{n}</span></div>' for s, n in L)
HTML = f'''<style>
@font-face{{font-family:ND;font-weight:400;src:url(file://{F}/noto-sans-devanagari-devanagari-400-normal.woff2)}}
@font-face{{font-family:ND;font-weight:700;src:url(file://{F}/noto-sans-devanagari-devanagari-700-normal.woff2)}}
body{{margin:0;width:1612px;height:1004px;background:#fbf4e8;font-family:ND,sans-serif;position:relative;overflow:hidden}}
.h{{height:120px;background:#0b1b3f;color:#fff;position:relative}}.h:after{{content:"";position:absolute;right:0;top:0;width:260px;height:120px;background:#c8102e}}
.h b{{position:absolute;left:26px;top:10px;font-size:52px;line-height:1.3}}.h i{{position:absolute;left:28px;top:74px;font-size:27px;font-style:normal;color:#dce2f0;line-height:1.4}}
.g{{position:absolute;left:16px;top:136px;display:grid;grid-template-columns:repeat(6,250px);column-gap:16px;row-gap:6px}}
.c img{{width:250px;height:156px;display:block}}.c span{{display:block;font-weight:700;font-size:23px;color:#0b1b3f;line-height:1.45;height:34px;padding-top:0}}
.f{{position:absolute;left:26px;bottom:12px;font-size:21px;color:#5a6378;line-height:1.5}}
.w{{position:absolute;right:20px;bottom:18px;background:rgba(11,27,63,.6);color:#fff;font:700 30px DejaVu Sans,sans-serif;padding:3px 12px;border-radius:6px}}
</style><div class="h"><b>नेपालका राष्ट्रिय चिन्ह</b><i>सबै २३ चिन्ह तस्बिर र नामसहित</i></div><div class="g">{cells}</div>
<div class="f">संविधानमा उल्लेखित: झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु, चरा। अरू सरकारले घोषणा गरेका वा परम्परागत हुन्।</div><div class="w">@thenepal.io</div>'''
def main():
    tmp = os.path.join(ROOT, 'photos', '_ne_chart.html'); open(tmp, 'w', encoding='utf-8').write(HTML)
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--allow-file-access-from-files']); pg = b.new_page(viewport={'width': 1612, 'height': 1004})
        pg.goto('file://' + tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
        png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1612, 'height': 1004}); b.close()
    os.remove(tmp)
    Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(ROOT, 'photos', 'nepal_national_symbols_chart_ne.webp'), quality=88, method=6); print('ok')
if __name__ == '__main__': main()
