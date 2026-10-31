#!/usr/bin/env python3
"""Adds schema.org about / mentions (with Wikipedia sameAs) to each page's Article JSON-LD
(and to the WebSite block of the two hubs). Idempotent. Only confirmed en.wikipedia.org pages are used."""
import re, json, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = 'https://en.wikipedia.org/wiki/'
E = {  # key: (English name, Nepali name, wikipedia title or None)
 'nepal': ('Nepal', 'नेपाल', 'Nepal'),
 'symbols': ('National symbols of Nepal', 'नेपालका राष्ट्रिय चिन्हहरू', 'National_symbols_of_Nepal'),
 'cattle': ('Cow (cattle)', 'गाई', 'Cattle'),
 'hinduism': ('Hinduism', 'हिन्दू धर्म', 'Hinduism'),
 'buddhism': ('Buddhism', 'बौद्ध धर्म', 'Buddhism'),
 'jainism': ('Jainism', 'जैन धर्म', 'Jainism'),
 'monal': ('Himalayan monal (Lophophorus impejanus)', 'डाँफे (हिमाली मोनाल)', 'Himalayan_monal'),
 'arboreum': ('Rhododendron arboreum (Lali Gurans)', 'लालीगुराँस', 'Rhododendron_arboreum'),
 'campanulatum': ('Rhododendron campanulatum', 'Rhododendron campanulatum', 'Rhododendron_campanulatum'),
 'peepal': ('Peepal (Ficus religiosa)', 'पीपल', 'Ficus_religiosa'),
 'mahseer': ('Golden mahseer (Tor putitora)', 'गोल्डेन महासीर', 'Tor_putitora'),
 'krishna': ('Krishna peacock (Papilio krishna)', 'कृष्ण मयूर', 'Papilio_krishna'),
 'flag': ('Flag of Nepal', 'नेपालको झण्डा', 'Flag_of_Nepal'),
 'constitution': ('Constitution of Nepal', 'नेपालको संविधान', 'Constitution_of_Nepal'),
 'prithvi': ('Prithvi Narayan Shah', 'पृथ्वीनारायण शाह', 'Prithvi_Narayan_Shah'),
 'anthem': ('Sayaun Thunga Phulka', 'सयौं थुँगा फूलका', 'Sayaun_Thunga_Phulka'),
 'gurung': ('Amber Gurung', 'अम्बर गुरुङ', 'Amber_Gurung'),
 'nepali': ('Nepali language', 'नेपाली भाषा', 'Nepali_language'),
 'languages': ('Languages of Nepal', 'नेपालका भाषाहरू', 'Languages_of_Nepal'),
 'devanagari': ('Devanagari', 'देवनागरी', 'Devanagari'),
 'crimson': ('Crimson', 'गाढा रातो', 'Crimson'),
 'daura': ('Daura-Suruwal', 'दौरा सुरुवाल', 'Daura-Suruwal'),
 'dhaka': ('Dhaka topi', 'ढाका टोपी', 'Dhaka_topi'),
 'jang': ('Jung Bahadur Rana', 'जंगबहादुर राणा', 'Jung_Bahadur_Rana'),
 'volleyball': ('Volleyball', 'भलिबल', 'Volleyball'),
 'vikram': ('Vikram Samvat (Bikram Sambat)', 'बिक्रम संवत्', 'Vikram_Samvat'),
 'newar': ('Nepal Sambat', 'नेपाल संवत्', 'Nepal_Sambat'),
 'deuda': ('Deuda and Maruni dances', 'देउडा र मारुनी', None),
 'emblem': ('Emblem of Nepal', 'नेपालको राष्ट्रिय राजचिन्ह', 'Emblem_of_Nepal'),
 'everest': ('Mount Everest (Sagarmatha)', 'सगरमाथा', 'Mount_Everest'),
 'snp': ('Sagarmatha National Park', 'सगरमाथा राष्ट्रिय निकुञ्ज', 'Sagarmatha_National_Park'),
 'dharahara': ('Dharahara', 'धरहरा', 'Dharahara'),
 'quake': ('April 2015 Nepal earthquake', 'सन् २०१५ को नेपाल भूकम्प', 'April_2015_Nepal_earthquake'),
 'bhimsen': ('Bhimsen Thapa', 'भीमसेन थापा', 'Bhimsen_Thapa'),
 'museum': ('National Museum of Nepal', 'नेपालको राष्ट्रिय संग्रहालय', 'National_Museum_of_Nepal'),
 'rupee': ('Nepalese rupee', 'नेपाली रुपैयाँ', 'Nepalese_rupee'),
 'siddha': ('Siddha Gufa', 'सिद्ध गुफा', None),
 'mahendra': ('Mahendra Cave', 'महेन्द्र गुफा', 'Mahendra_Cave'),
 'gupteshwor': ('Gupteshwor Mahadev Cave', 'गुप्तेश्वर महादेव गुफा', 'Gupteshwor_Mahadev_Cave'),
}
P = {  # page -> (about, [mentions])
 'national-animal': ('cattle', ['nepal', 'hinduism', 'symbols']),
 'national-bird': ('monal', ['nepal', 'symbols']),
 'national-flower': ('arboreum', ['campanulatum', 'nepal', 'symbols']),
 'national-tree': ('peepal', ['hinduism', 'buddhism', 'jainism', 'nepal']),
 'national-fish': ('mahseer', ['nepal', 'symbols']),
 'national-butterfly': ('krishna', ['nepal', 'symbols']),
 'national-flag': ('flag', ['nepal', 'constitution', 'prithvi']),
 'national-anthem': ('anthem', ['nepal', 'gurung']),
 'national-language': ('nepali', ['languages', 'constitution', 'devanagari']),
 'national-color': ('crimson', ['flag', 'arboreum', 'nepal']),
 'national-dress': ('daura', ['dhaka', 'jang', 'nepal']),
 'national-sport': ('volleyball', ['nepal', 'symbols']),
 'national-calendar': ('vikram', ['newar', 'nepal']),
 'national-dance': ('deuda', ['nepal', 'symbols']),
 'national-emblem': ('emblem', ['everest', 'arboreum', 'nepal']),
 'national-everest': ('everest', ['snp', 'nepal']),
 'national-monument': ('dharahara', ['quake', 'bhimsen', 'nepal']),
 'national-museum': ('museum', ['nepal', 'symbols']),
 'national-currency': ('rupee', ['nepal', 'symbols']),
 'national-cave': ('siddha', ['mahendra', 'gupteshwor', 'nepal']),
 '': ('symbols', ['nepal', 'flag', 'emblem']),
}
def ent(k, ne):
    en_n, ne_n, w = E[k]
    d = {"@type": "Thing", "name": ne_n if ne else en_n}
    if ne and ne_n != en_n: d["alternateName"] = en_n
    if w: d["sameAs"] = W + w
    return d
for slug, (about, ment) in P.items():
    for ne in (False, True):
        f = ('ne/' if ne else '') + (slug + '/' if slug else '') + 'index.html'
        if not os.path.exists(f): continue
        s = open(f, encoding='utf8').read(); o = s
        want = 'WebSite' if slug == '' else 'Article'
        def fix(m):
            try: d = json.loads(m.group(2))
            except Exception: return m.group(0)
            if d.get('@type') != want: return m.group(0)
            d['about'] = ent(about, ne); d['mentions'] = [ent(k, ne) for k in ment]
            return m.group(1) + json.dumps(d, ensure_ascii=False, indent=2) + m.group(3)
        s = re.sub(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', fix, s, flags=re.S)
        if s != o: open(f, 'w', encoding='utf8').write(s); print('updated', f)
