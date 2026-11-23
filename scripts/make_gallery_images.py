#!/usr/bin/env python3
"""Watermarked 480x300 thumbnails (photos/thumbs/<slug>.webp) for the symbols gallery page, and the shareable chart
photos/nepal_national_symbols_chart.webp (all 23 symbols, 1600x1250). Every image carries the @thenepal.io watermark."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYMBOLS = [  # slug, short label, source photo
 ('national-flag', 'Flag', 'national_flag_nepal'), ('national-anthem', 'Anthem', 'National_anthem_of_Nepal'), ('national-emblem', 'Emblem', 'national_emblem_of_nepal'),
 ('national-flower', 'Flower', 'national_flower_of_nepal'), ('national-color', 'Colour', 'national_color_of_nepal'), ('national-animal', 'Animal', 'national_animal_of_nepal'),
 ('national-bird', 'Bird', 'national_bird_of_nepal'), ('national-language', 'Language', 'national_language_of_nepal'), ('national-sport', 'Game', 'national_sport_of_nepal'),
 ('national-fruit', 'Fruit', 'national_fruit_of_nepal'), ('national-calendar', 'Calendar', 'national_calendar_of_nepal'), ('national-currency', 'Currency', 'nepal_currency_of_nepal'),
 ('national-tree', 'Tree', 'national_tree_of_nepal'), ('national-fish', 'Fish', 'national_fish_of_nepal'), ('national-butterfly', 'Butterfly', 'national_butterfly_of_nepal'),
 ('national-food', 'Food', 'national_dish_of_nepal'), ('national-weapon', 'Weapon', 'national_weapon_of_nepal'), ('national-dress', 'Dress', 'national_dress_of_nepal'),
 ('national-dance', 'Dance', 'national_dance_of_nepal'), ('national-monument', 'Monument', 'national_monument_nepal'), ('national-cave', 'Cave', 'national_cave_of_nepal'),
 ('national-museum', 'Museum', 'national_museum_nepal'), ('national-everest', 'Highest peak', 'national_everest_of_nepal'),
]
def font(sz, bold=True):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
def cover(im, w, h):
    r = max(w / im.width, h / im.height); im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2; return im.crop((x, y, x + w, y + h))
def wm(im, size, pad=8):
    d = ImageDraw.Draw(im, 'RGBA'); f = font(size); t = '@thenepal.io'; b = d.textbbox((0, 0), t, font=f)
    x, y = im.width - (b[2] - b[0]) - pad - 6, im.height - (b[3] - b[1]) - pad - 4
    d.rounded_rectangle((x - 6, y - 3, x + (b[2] - b[0]) + 6, y + (b[3] - b[1]) + 7), 6, fill=(11, 27, 63, 150)); d.text((x, y), t, font=f, fill=(255, 255, 255, 235))
def main():
    os.makedirs(os.path.join(ROOT, 'photos', 'thumbs'), exist_ok=True)
    thumbs = {}
    for slug, label, ph in SYMBOLS:
        im = cover(Image.open(os.path.join(ROOT, 'photos', ph + '.webp')).convert('RGB'), 480, 300); wm(im, 20)
        im.save(os.path.join(ROOT, 'photos', 'thumbs', slug + '.webp'), quality=82, method=6); thumbs[slug] = (label, im)
    cw, ch, gx, gy, top, cols = 250, 156, 16, 40, 150, 6
    W = cols * cw + (cols + 1) * gx; rows = 4; H = top + rows * (ch + gy) + 70
    P = Image.new('RGB', (W, H), (251, 244, 232)); d = ImageDraw.Draw(P)
    d.rectangle((0, 0, W, 120), fill=(11, 27, 63)); d.rectangle((W - 260, 0, W, 120), fill=(200, 16, 46))
    d.text((gx + 10, 18), 'National Symbols of Nepal', font=font(54), fill='white'); d.text((gx + 12, 84), 'All 23 symbols with pictures and names', font=font(26, False), fill=(220, 226, 240))
    for i, (slug, label, ph) in enumerate(SYMBOLS):
        r, c = divmod(i, cols); x = gx + c * (cw + gx); y = top + r * (ch + gy)
        t = thumbs[slug][1].resize((cw, ch), Image.LANCZOS); P.paste(t, (x, y)); d.text((x, y + ch + 6), label, font=font(21), fill=(11, 27, 63))
    d.text((gx + 10, H - 52), 'Official (Constitution): flag, anthem, emblem, flower, colour, animal, bird. Others are declared or customary.', font=font(20, False), fill=(90, 99, 120))
    wm(P, 30, 14); P.save(os.path.join(ROOT, 'photos', 'nepal_national_symbols_chart.webp'), quality=88, method=6); print('chart', P.size)
if __name__ == '__main__': main()
