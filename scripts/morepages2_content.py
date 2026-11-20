# -*- coding: utf-8 -*-
# Pages: /national-parks-of-nepal/, /nepal-tiger-census-2026/, /national-days-of-nepal/ (EN + NE). Uses _mk/_en/_ne from morepages_content.py.
# Sources:
#  - Parks: Wikipedia "List of protected areas of Nepal" (13 national parks, areas, years, reserves, conservation areas); Wikipedia "Chhayanath National Park"
#    (established 29 Aug 2025, Mugu, ~843.36 km2, 13th park); Himalayan Tribune 6 Sep 2025 (decision, carved out of Shey Phoksundo, 843.36 km2). Shey Phoksundo 3,555 km2 (WorldAtlas)
#    minus 843 = 2,712 km2 (consistent). Some lists give other areas for Chhayanath; page says "about". WorldAtlas for park features.
#  - Tigers: IUCN story 29 Jul 2026; Kathmandu Post 30 Jul 2026 (429 tigers, camera traps 31 Dec 2025-23 Apr 2026, per-park counts, NTNC deaths 10 in FY2025-26, 85 over eight years, Baral 400-500).
#  - National days: dates computed with converter.thenepal.io BS tables; descriptions from the converter pages for each day; Republic Day: Wikipedia "Republic Day (Nepal)" (28 May 2008).
FIG = '<figure style="margin:20px 0"><img src="/photos/{f}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" style="width:100%;height:auto;border-radius:12px"><figcaption style="font-size:.9rem;opacity:.8;margin-top:6px">{cap}</figcaption></figure>'
def fig(f, alt, cap, w=1200, h=675): return FIG.format(f=f, alt=alt, cap=cap, w=w, h=h)

REL_NP = [('world-heritage-sites', 'World Heritage Sites'), ('national-animal', 'National Animal'), ('national-everest', 'Mount Everest'), ('nepal-tiger-census-2026', 'Tiger Census 2026')]
REL_NP_NE = [('world-heritage-sites', 'विश्व सम्पदा स्थल'), ('national-animal', 'राष्ट्रिय पशु'), ('national-everest', 'सगरमाथा'), ('nepal-tiger-census-2026', 'बाघ गणना २०२६')]
REL_TG = [('national-parks-of-nepal', 'National Parks of Nepal'), ('national-animal', 'National Animal'), ('world-heritage-sites', 'World Heritage Sites'), ('official-vs-unofficial', 'Official vs Unofficial Symbols')]
REL_TG_NE = [('national-parks-of-nepal', 'नेपालका राष्ट्रिय निकुञ्ज'), ('national-animal', 'राष्ट्रिय पशु'), ('world-heritage-sites', 'विश्व सम्पदा स्थल'), ('official-vs-unofficial', 'आधिकारिक कि परम्परागत')]
REL_ND2 = [('national-day', 'National Day of Nepal'), ('national-flag', 'National Flag'), ('national-anthem', 'National Anthem'), ('sources', 'Sources & Methodology')]
REL_ND2_NE = [('national-day', 'नेपालको राष्ट्रिय दिवस'), ('national-flag', 'राष्ट्रिय झण्डा'), ('national-anthem', 'राष्ट्रगान'), ('sources', 'स्रोत र कार्यविधि')]

PARK_ROWS = [  # name, region, established, area, known for (EN), known for (NE)
 ('Chitwan', 'Terai', '1973', '953', 'One-horned rhinoceros, tigers; World Heritage Site', 'एक सिङ्गे गैँडा, बाघ; विश्व सम्पदा स्थल'),
 ('Sagarmatha', 'Himalaya', '1976', '1,148', 'Mount Everest; World Heritage Site', 'सगरमाथा; विश्व सम्पदा स्थल'),
 ('Langtang', 'Himalaya', '1976', '1,710', 'Gosainkunda lake at about 4,300 m', 'करिब ४,३०० मिटरमा गोसाइँकुण्ड'),
 ('Rara', 'Himalaya', '1976', '106', 'Rara Lake; smallest national park', 'रारा ताल; सबैभन्दा सानो निकुञ्ज'),
 ('Khaptad', 'Hill/Himalaya', '1984', '225', 'Himalayan monal (danphe), high meadows', 'डाँफे, उच्च पहाडी चौर'),
 ('Shey Phoksundo', 'Himalaya', '1984', '2,712', 'Phoksundo Lake, snow leopard; largest park', 'फोक्सुन्डो ताल, हिउँचितुवा; सबैभन्दा ठूलो निकुञ्ज'),
 ('Bardiya', 'Terai', '1988', '968', 'Tigers, gharial', 'बाघ, घडियाल'),
 ('Makalu Barun', 'Himalaya', '1992', '1,500', 'Snow peaks and tropical forest in one park', 'हिमाल र उष्ण वन एकै निकुञ्जमा'),
 ('Shivapuri Nagarjun', 'Hill (Kathmandu)', '2002', '159', 'Closest park to Kathmandu; pangolin', 'काठमाडौंसँग नजिकको निकुञ्ज; सालक'),
 ('Banke', 'Terai', '2010', '550', 'Tigers, four-horned antelope', 'बाघ, चौसिङ्गे'),
 ('Shuklaphanta', 'Terai', '1976 (reserve); park 2017', '305', 'Swamp deer, tigers, rhinos', 'बारहसिङ्गा, बाघ, गैँडा'),
 ('Parsa', 'Terai', '1984 (reserve); park 2017', '637', 'Tigers, gaur, elephants', 'बाघ, गौरी गाई, हात्ती'),
 ('Chhayanath', 'Himalaya (Mugu)', '2025', '843 (approx.)', 'Snow leopard, blue sheep, danphe', 'हिउँचितुवा, नाउर, डाँफे'),
]
def _rows(ne):
    return ''.join('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (r[0], r[2], r[3], r[5] if ne else r[4]) for r in PARK_ROWS)

NP_EN_BODY = '''    <section>
      <p class="lede"><strong>Nepal has 13 national parks.</strong> The 13th, <strong>Chhayanath National Park</strong> in Mugu district, was created in 2025. Before that, Nepal had 12, which is why many older lists still say "12 national parks".</p>
    </section>

    <section id="list">
      <h2>List of National Parks of Nepal (2026)</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>National park</th><th>Established</th><th>Area (km²)</th><th>Known for</th></tr></thead>
          <tbody>
''' + _rows(False) + '''
          </tbody>
        </table>
      </div>
      <p class="source">Source: List of protected areas of Nepal (Wikipedia); Chhayanath National Park (Wikipedia); Himalayan Tribune, 6 September 2025; WorldAtlas for park highlights. Areas differ slightly between sources, so treat them as approximate and check the Department of National Parks and Wildlife Conservation for legal figures.</p>
      ''' + fig('nepal_national_parks_area', 'Bar chart of the 13 national parks of Nepal ranked by area, with year established', 'Nepal national parks ranked by area. Shey Phoksundo is the largest and Rara the smallest.', h=900) + '''
    </section>

    <section id="newest">
      <h2>Chhayanath: The 13th National Park</h2>
      <p>The government decided in 2025 to create Chhayanath National Park in Mugu district, Karnali Province, on a proposal from the Ministry of Forests and Environment. It covers about 843 km² and was carved out of Shey Phoksundo National Park, which is why Shey Phoksundo's area is now listed as 2,712 km² instead of the older 3,555 km². Wikipedia gives its establishment date as 29 August 2025, while some other lists show early September 2025, so we say "2025" in the table.</p>
      <div class="status warn">
        <b>Why you still see "12 national parks".</b> Shuklaphanta and Parsa were upgraded from wildlife reserves to national parks in 2017, which made 12. Chhayanath made 13. Older exam guides and travel sites have not all been updated.
      </div>
      <p class="source">Source: Himalayan Tribune, "Creation of Chhayanath National Park elates locals" (6 September 2025); Wikipedia, Chhayanath National Park.</p>
    </section>

    <section id="others">
      <h2>Other Protected Areas in Nepal</h2>
      <p>National parks are only one category. Nepal also protects land as a wildlife reserve, a hunting reserve and conservation areas, where people live and use the land under a management plan.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Type</th><th>Name</th><th>Year</th><th>Area (km²)</th></tr></thead>
          <tbody>
            <tr><td>Wildlife reserve</td><td>Koshi Tappu</td><td>1976</td><td>175</td></tr>
            <tr><td>Hunting reserve</td><td>Dhorpatan</td><td>1987</td><td>1,325</td></tr>
            <tr><td>Conservation area</td><td>Annapurna</td><td>1992</td><td>7,629</td></tr>
            <tr><td>Conservation area</td><td>Kanchenjunga</td><td>1997</td><td>2,035</td></tr>
            <tr><td>Conservation area</td><td>Manaslu</td><td>1998</td><td>1,663</td></tr>
            <tr><td>Conservation area</td><td>Blackbuck</td><td>2009</td><td>17</td></tr>
            <tr><td>Conservation area</td><td>Api Nampa</td><td>2010</td><td>1,903</td></tr>
            <tr><td>Conservation area</td><td>Gaurishankar</td><td>2010</td><td>2,197</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: List of protected areas of Nepal (Wikipedia).</p>
    </section>

    <section id="heritage">
      <h2>Which Parks Are World Heritage Sites?</h2>
      <p>Two of the national parks are UNESCO World Heritage Sites: <strong>Sagarmatha</strong> (1979) and <strong>Chitwan</strong> (1984). See all four Nepali sites on our <a href="/world-heritage-sites/">World Heritage Sites page</a>. For the park that protects the highest mountain, read about <a href="/national-everest/">Mount Everest</a>. For the animal numbers behind the parks, see the <a href="/nepal-tiger-census-2026/">2026 tiger census</a>, the <a href="/nepal-rhino-count/">rhino count</a> and the <a href="/nepal-snow-leopard-population/">snow leopard estimate</a>.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>Chitwan, set up in 1973, is Nepal's oldest national park.</li>
          <li>Shivapuri Nagarjun is the national park closest to Kathmandu, near enough for a day trip.</li>
          <li>Five of the parks are in the Terai lowlands: Chitwan, Bardiya, Banke, Parsa and Shuklaphanta. They hold Nepal's wild tigers.</li>
        </ul>
      </div>
    </section>
'''
NP_EN_FAQ = [
 ("How many national parks are there in Nepal?", "Nepal has 13 national parks. The 13th, Chhayanath National Park in Mugu district, was created in 2025. Before that Nepal had 12."),
 ("What are the 13 national parks of Nepal?", "Chitwan, Sagarmatha, Langtang, Rara, Khaptad, Shey Phoksundo, Bardiya, Makalu Barun, Shivapuri Nagarjun, Banke, Shuklaphanta, Parsa and Chhayanath."),
 ("Which is the first national park of Nepal?", "Chitwan National Park, established in 1973, is Nepal's first national park."),
 ("Which is the largest national park in Nepal?", "Shey Phoksundo National Park, at about 2,712 km² after Chhayanath was carved out of it in 2025."),
 ("Which is the smallest national park in Nepal?", "Rara National Park, at about 106 km²."),
 ("Which is the newest national park of Nepal?", "Chhayanath National Park in Mugu district, created in 2025."),
 ("Which national parks of Nepal are World Heritage Sites?", "Sagarmatha National Park (inscribed 1979) and Chitwan National Park (1984)."),
 ("Which national park is near Kathmandu?", "Shivapuri Nagarjun National Park, established in 2002, lies on the northern edge of the Kathmandu Valley."),
]
NP_NE_BODY = '''    <section>
      <p class="lede"><strong>नेपालमा १३ वटा राष्ट्रिय निकुञ्ज छन्।</strong> १३ औँ, मुगु जिल्लाको <strong>छायाँनाथ राष्ट्रिय निकुञ्ज</strong>, सन् २०२५ मा बनेको हो। त्योअघि १२ वटा थिए, त्यसैले पुराना सूचीमा अझै "१२ राष्ट्रिय निकुञ्ज" लेखिएको भेटिन्छ।</p>
    </section>

    <section id="list">
      <h2>नेपालका राष्ट्रिय निकुञ्जको सूची (२०२६)</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>राष्ट्रिय निकुञ्ज</th><th>स्थापना</th><th>क्षेत्रफल (वर्ग कि.मी.)</th><th>प्रसिद्ध</th></tr></thead>
          <tbody>
''' + _rows(True) + '''
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: List of protected areas of Nepal (Wikipedia); Chhayanath National Park (Wikipedia); हिमालयन ट्रिब्युन, ६ सेप्टेम्बर २०२५; निकुञ्जका विशेषताका लागि WorldAtlas। क्षेत्रफल स्रोतअनुसार केही फरक पर्छ, त्यसैले अनुमानित मान्नुहोस् र कानुनी तथ्यांकका लागि राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभाग हेर्नुहोस्।</p>
      ''' + fig('nepal_national_parks_area', 'क्षेत्रफलअनुसार नेपालका १३ राष्ट्रिय निकुञ्जको बार चार्ट', 'क्षेत्रफलअनुसार नेपालका राष्ट्रिय निकुञ्ज। शे-फोक्सुन्डो सबैभन्दा ठूलो र रारा सबैभन्दा सानो हो।', h=900) + '''
    </section>

    <section id="newest">
      <h2>छायाँनाथ: १३ औँ राष्ट्रिय निकुञ्ज</h2>
      <p>वन तथा वातावरण मन्त्रालयको प्रस्तावमा सरकारले सन् २०२५ मा कर्णाली प्रदेशको मुगु जिल्लामा छायाँनाथ राष्ट्रिय निकुञ्ज बनाउने निर्णय गर्‍यो। यो करिब ८४३ वर्ग कि.मी. क्षेत्रफलमा फैलिएको छ र शे-फोक्सुन्डो राष्ट्रिय निकुञ्जबाट छुट्याइएको हो, त्यसैले शे-फोक्सुन्डोको क्षेत्रफल पुरानो ३,५५५ बाट २,७१२ वर्ग कि.मी. भएको छ। विकिपिडियाले स्थापना मिति सन् २०२५ अगस्ट २९ दिएको छ भने केही सूचीले सेप्टेम्बरको सुरु देखाउँछन्, त्यसैले तालिकामा "२०२५" लेखिएको छ।</p>
      <div class="status warn">
        <b>किन अझै "१२ राष्ट्रिय निकुञ्ज" देखिन्छ?</b> शुक्लाफाँटा र पर्सा सन् २०१७ मा वन्यजन्तु आरक्षबाट राष्ट्रिय निकुञ्जमा परिणत भएपछि १२ वटा भए। छायाँनाथ थपिएपछि १३ भयो। पुराना परीक्षा गाइड र पर्यटन साइटहरू सबैले अद्यावधिक गरेका छैनन्।
      </div>
      <p class="source">स्रोत: हिमालयन ट्रिब्युन, "Creation of Chhayanath National Park elates locals" (६ सेप्टेम्बर २०२५); Wikipedia, Chhayanath National Park।</p>
    </section>

    <section id="others">
      <h2>नेपालका अन्य संरक्षित क्षेत्र</h2>
      <p>राष्ट्रिय निकुञ्ज संरक्षित क्षेत्रको एउटा वर्ग मात्र हो। नेपालले वन्यजन्तु आरक्ष, शिकार आरक्ष र संरक्षण क्षेत्र पनि तोकेको छ। संरक्षण क्षेत्रमा मानिस बसोबास गर्छन् र व्यवस्थापन योजनाअनुसार भूमि प्रयोग गर्छन्।</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>प्रकार</th><th>नाम</th><th>साल</th><th>क्षेत्रफल (वर्ग कि.मी.)</th></tr></thead>
          <tbody>
            <tr><td>वन्यजन्तु आरक्ष</td><td>कोशीटप्पु</td><td>१९७६</td><td>१७५</td></tr>
            <tr><td>शिकार आरक्ष</td><td>ढोरपाटन</td><td>१९८७</td><td>१,३२५</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>अन्नपूर्ण</td><td>१९९२</td><td>७,६२९</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>कञ्चनजङ्घा</td><td>१९९७</td><td>२,०३५</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>मनास्लु</td><td>१९९८</td><td>१,६६३</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>कृष्णसार</td><td>२००९</td><td>१७</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>अपी नाम्पा</td><td>२०१०</td><td>१,९०३</td></tr>
            <tr><td>संरक्षण क्षेत्र</td><td>गौरीशङ्कर</td><td>२०१०</td><td>२,१९७</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: List of protected areas of Nepal (Wikipedia)।</p>
    </section>

    <section id="heritage">
      <h2>कुन निकुञ्ज विश्व सम्पदा स्थल हुन्?</h2>
      <p>दुईवटा राष्ट्रिय निकुञ्ज युनेस्कोका विश्व सम्पदा स्थल हुन्: <strong>सगरमाथा</strong> (१९७९) र <strong>चितवन</strong> (१९८४)। नेपालका चारवटै स्थल <a href="/ne/world-heritage-sites/">विश्व सम्पदा स्थल पृष्ठ</a> मा हेर्नुहोस्। सबैभन्दा अग्लो हिमालको जानकारीका लागि <a href="/ne/national-everest/">सगरमाथा</a> पृष्ठ र निकुञ्जका जनावरका लागि <a href="/ne/nepal-tiger-census-2026/">२०२६ को बाघ गणना</a>, <a href="/ne/nepal-rhino-count/">गैँडा गणना</a> र <a href="/ne/nepal-snow-leopard-population/">हिउँचितुवाको अनुमान</a> हेर्नुहोस्।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>सन् १९७३ मा स्थापना भएको चितवन नेपालको सबैभन्दा पुरानो राष्ट्रिय निकुञ्ज हो।</li>
          <li>शिवपुरी नागार्जुन काठमाडौंसँग सबैभन्दा नजिकको राष्ट्रिय निकुञ्ज हो, एकदिने भ्रमणका लागि उपयुक्त।</li>
          <li>तराईका पाँच निकुञ्ज चितवन, बर्दिया, बाँके, पर्सा र शुक्लाफाँटामा नेपालका जङ्गली बाघ छन्।</li>
        </ul>
      </div>
    </section>
'''
NP_NE_FAQ = [
 ("नेपालमा कतिवटा राष्ट्रिय निकुञ्ज छन्?", "नेपालमा १३ वटा राष्ट्रिय निकुञ्ज छन्। १३ औँ, मुगुको छायाँनाथ राष्ट्रिय निकुञ्ज, सन् २०२५ मा बनेको हो। त्योअघि १२ वटा थिए।"),
 ("नेपालका १३ राष्ट्रिय निकुञ्ज कुन कुन हुन्?", "चितवन, सगरमाथा, लाङटाङ, रारा, खप्तड, शे-फोक्सुन्डो, बर्दिया, मकालु बरुण, शिवपुरी नागार्जुन, बाँके, शुक्लाफाँटा, पर्सा र छायाँनाथ।"),
 ("नेपालको पहिलो राष्ट्रिय निकुञ्ज कुन हो?", "सन् १९७३ मा स्थापना भएको चितवन राष्ट्रिय निकुञ्ज नेपालको पहिलो राष्ट्रिय निकुञ्ज हो।"),
 ("नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज कुन हो?", "शे-फोक्सुन्डो राष्ट्रिय निकुञ्ज, सन् २०२५ मा छायाँनाथ छुट्टिएपछि करिब २,७१२ वर्ग कि.मी."),
 ("नेपालको सबैभन्दा सानो राष्ट्रिय निकुञ्ज कुन हो?", "रारा राष्ट्रिय निकुञ्ज, करिब १०६ वर्ग कि.मी."),
 ("नेपालको सबैभन्दा नयाँ राष्ट्रिय निकुञ्ज कुन हो?", "सन् २०२५ मा बनेको मुगु जिल्लाको छायाँनाथ राष्ट्रिय निकुञ्ज।"),
 ("नेपालका कुन राष्ट्रिय निकुञ्ज विश्व सम्पदा स्थल हुन्?", "सगरमाथा राष्ट्रिय निकुञ्ज (१९७९) र चितवन राष्ट्रिय निकुञ्ज (१९८४)।"),
 ("काठमाडौंसँग नजिकको राष्ट्रिय निकुञ्ज कुन हो?", "सन् २००२ मा स्थापना भएको शिवपुरी नागार्जुन राष्ट्रिय निकुञ्ज काठमाडौं उपत्यकाको उत्तरी किनारमा पर्छ।"),
]

# ---------------- Tigers ----------------
TG_EN_BODY = '''    <section>
      <p class="lede"><strong>Nepal has 429 wild tigers, according to the 2026 national tiger census.</strong> That is a record, up 74 from 355 in 2022. The Department of National Parks and Wildlife Conservation released the result on Global Tiger Day, 29 July 2026.</p>
    </section>

    <section id="numbers">
      <h2>Nepal Tiger Count by Year</h2>
      ''' + fig('nepal_tiger_census_trend', 'Bar chart of Nepal tiger counts: 121 in 2009, 198 in 2013, 235 in 2018, 355 in 2022 and 429 in 2026', 'Nepal wild tiger count by national census. The number has more than tripled since 2009.') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>Census</th><th>Tigers</th></tr></thead>
          <tbody>
            <tr><td>2009</td><td>121</td></tr>
            <tr><td>2013</td><td>198</td></tr>
            <tr><td>2018</td><td>235</td></tr>
            <tr><td>2022</td><td>355</td></tr>
            <tr><td><strong>2026</strong></td><td><strong>429</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: IUCN, "Tiger census: Nepal's tiger number increases to 429" (29 July 2026).</p>
    </section>

    <section id="parks">
      <h2>Tigers in Each National Park</h2>
      ''' + fig('nepal_tiger_census_parks', 'Grouped bar chart comparing tigers in Chitwan, Bardiya, Parsa, Banke and Shuklaphanta in 2022 and 2026', 'Tigers by park in 2022 and 2026. Four parks rose; only Bardiya fell.') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>Park</th><th>2022</th><th>2026</th><th>Change</th></tr></thead>
          <tbody>
            <tr><td>Chitwan (park and buffer zone)</td><td>128</td><td>145</td><td>+17</td></tr>
            <tr><td>Bardiya</td><td>125</td><td>112</td><td>-13</td></tr>
            <tr><td>Parsa</td><td>41</td><td>71</td><td>+30</td></tr>
            <tr><td>Banke</td><td>25</td><td>51</td><td>+26</td></tr>
            <tr><td>Shuklaphanta</td><td>36</td><td>50</td><td>+14</td></tr>
            <tr><td><strong>Total</strong></td><td>355</td><td><strong>429</strong></td><td>+74</td></tr>
          </tbody>
        </table>
      </div>
      <p>Chitwan remains the largest tiger habitat. The biggest jumps were in Parsa and Banke. Bardiya was the only park to decline, from 125 to 112. Read more about the parks on our <a href="/national-parks-of-nepal/">national parks of Nepal</a> page, and compare with the <a href="/nepal-rhino-count/">rhino count</a> and <a href="/nepal-snow-leopard-population/">snow leopard estimate</a> in our <a href="/nepal-wildlife-population/">wildlife counts</a> guide.</p>
      <p class="source">Source: The Kathmandu Post, "Habitat concerns grow as Nepal counts a record 429 tigers" (30 July 2026); IUCN (29 July 2026).</p>
    </section>

    <section id="method">
      <h2>How the Tigers Were Counted</h2>
      <p>The census used camera traps and ran from 31 December 2025 to 23 April 2026, according to the Kathmandu Post. The IUCN says the Department of National Parks and Wildlife Conservation ran it with the Department of Forests and Soil Conservation, provincial governments, the Nepal Army and conservation partners. It is run every four years, so the next full census would be expected around 2030.</p>
    </section>

    <section id="conflict">
      <h2>The Other Side: Conflict and Space</h2>
      <div class="status warn">
        <b>More tigers also means more conflict.</b> The NTNC reported 10 people killed by tigers in fiscal year 2025-26, the first rise after four years of decline: Banke 4, Parsa 3, Bardiya 2 and Chitwan 1. Over eight years, 85 people were killed. Wildlife expert Hem Sagar Baral told the Post that Nepal could support roughly 400 to 500 tigers, so the country may be nearing its limit.
      </div>
      <p class="source">Source: The Kathmandu Post, 30 July 2026.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>The tiger is not Nepal's national animal. The Constitution names the cow. See our <a href="/national-animal/">national animal page</a>.</li>
          <li>Nepal's 2026 count is more than three times the 121 tigers counted in 2009.</li>
        </ul>
      </div>
    </section>
'''
TG_EN_FAQ = [
 ("How many tigers are there in Nepal in 2026?", "The 2026 national tiger census counted 429 tigers in Nepal, a record and up from 355 in 2022."),
 ("Which national park in Nepal has the most tigers?", "Chitwan National Park and its buffer zone, with 145 tigers in the 2026 census, followed by Bardiya (112) and Parsa (71)."),
 ("How many tigers did Nepal have in 2022?", "Nepal had 355 tigers in the 2022 census."),
 ("Are tigers increasing in Nepal?", "Yes. The count rose from 121 in 2009 to 429 in 2026. Four of the five tiger parks increased in 2026; Bardiya fell from 125 to 112."),
 ("When was the Nepal tiger census 2026 released?", "It was released on Global Tiger Day, 29 July 2026, in Kathmandu."),
 ("How was the 2026 tiger census done?", "With camera traps, in a survey that ran from 31 December 2025 to 23 April 2026."),
 ("When is the next tiger census in Nepal?", "The census is run every four years, so the next one is expected around 2030."),
 ("Is the tiger the national animal of Nepal?", "No. The national animal under Nepal's Constitution is the cow."),
]
TG_NE_BODY = '''    <section>
      <p class="lede"><strong>सन् २०२६ को राष्ट्रिय बाघ गणनाअनुसार नेपालमा ४२९ वटा जङ्गली बाघ छन्।</strong> यो रेकर्ड हो, सन् २०२२ को ३५५ भन्दा ७४ ले बढी। राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभागले विश्व बाघ दिवस, २९ जुलाई २०२६ मा नतिजा सार्वजनिक गर्‍यो।</p>
    </section>

    <section id="numbers">
      <h2>वर्षअनुसार नेपालमा बाघको सङ्ख्या</h2>
      ''' + fig('nepal_tiger_census_trend', 'नेपालमा बाघको सङ्ख्या: २००९ मा १२१, २०१३ मा १९८, २०१८ मा २३५, २०२२ मा ३५५ र २०२६ मा ४२९', 'राष्ट्रिय गणनाअनुसार नेपालका जङ्गली बाघ। सन् २००९ पछि सङ्ख्या तीन गुणाभन्दा बढी भएको छ।') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>गणना</th><th>बाघ</th></tr></thead>
          <tbody>
            <tr><td>२००९</td><td>१२१</td></tr>
            <tr><td>२०१३</td><td>१९८</td></tr>
            <tr><td>२०१८</td><td>२३५</td></tr>
            <tr><td>२०२२</td><td>३५५</td></tr>
            <tr><td><strong>२०२६</strong></td><td><strong>४२९</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: IUCN, "Tiger census: Nepal's tiger number increases to 429" (२९ जुलाई २०२६)।</p>
    </section>

    <section id="parks">
      <h2>प्रत्येक राष्ट्रिय निकुञ्जमा बाघ</h2>
      ''' + fig('nepal_tiger_census_parks', 'चितवन, बर्दिया, पर्सा, बाँके र शुक्लाफाँटामा सन् २०२२ र २०२६ का बाघको तुलना', 'सन् २०२२ र २०२६ मा निकुञ्जअनुसार बाघ। चार निकुञ्जमा बढ्यो, बर्दियामा मात्र घट्यो।') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>निकुञ्ज</th><th>२०२२</th><th>२०२६</th><th>परिवर्तन</th></tr></thead>
          <tbody>
            <tr><td>चितवन (निकुञ्ज र मध्यवर्ती क्षेत्र)</td><td>१२८</td><td>१४५</td><td>+१७</td></tr>
            <tr><td>बर्दिया</td><td>१२५</td><td>११२</td><td>-१३</td></tr>
            <tr><td>पर्सा</td><td>४१</td><td>७१</td><td>+३०</td></tr>
            <tr><td>बाँके</td><td>२५</td><td>५१</td><td>+२६</td></tr>
            <tr><td>शुक्लाफाँटा</td><td>३६</td><td>५०</td><td>+१४</td></tr>
            <tr><td><strong>जम्मा</strong></td><td>३५५</td><td><strong>४२९</strong></td><td>+७४</td></tr>
          </tbody>
        </table>
      </div>
      <p>चितवन बाघको सबैभन्दा ठूलो बासस्थान नै रह्यो। सबैभन्दा धेरै वृद्धि पर्सा र बाँकेमा देखियो। बर्दिया मात्र घट्यो, १२५ बाट ११२ मा। निकुञ्जबारे थप <a href="/ne/national-parks-of-nepal/">नेपालका राष्ट्रिय निकुञ्ज</a> पृष्ठमा पढ्नुहोस् र <a href="/ne/nepal-wildlife-population/">वन्यजन्तुको सङ्ख्या</a> सँग तुलना गर्नुहोस्।</p>
      <p class="source">स्रोत: द काठमाडौं पोस्ट, "Habitat concerns grow as Nepal counts a record 429 tigers" (३० जुलाई २०२६); IUCN (२९ जुलाई २०२६)।</p>
    </section>

    <section id="method">
      <h2>बाघ कसरी गणना गरियो?</h2>
      <p>काठमाडौं पोस्टका अनुसार गणनामा क्यामेरा ट्र्याप प्रयोग गरियो र यो सन् २०२५ डिसेम्बर ३१ देखि २०२६ अप्रिल २३ सम्म चल्यो। IUCN का अनुसार राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभागले वन तथा भूसंरक्षण विभाग, प्रदेश सरकार, नेपाली सेना र संरक्षण साझेदारसँग मिलेर यो गरेको हो। गणना चार वर्षमा एकपटक हुन्छ, त्यसैले अर्को पूर्ण गणना करिब २०३० तिर अपेक्षित छ।</p>
    </section>

    <section id="conflict">
      <h2>अर्को पक्ष: द्वन्द्व र ठाउँ</h2>
      <div class="status warn">
        <b>बाघ बढ्दा मानव-बाघ द्वन्द्व पनि बढ्छ।</b> एनटीएनसीका अनुसार आर्थिक वर्ष २०२५-२६ मा बाघको आक्रमणबाट १० जनाको मृत्यु भयो, चार वर्षको गिरावटपछिको पहिलो वृद्धि: बाँके ४, पर्सा ३, बर्दिया २ र चितवन १। आठ वर्षमा ८५ जनाको मृत्यु भएको छ। वन्यजन्तु विशेषज्ञ हेमसागर बरालले पोस्टलाई नेपालले करिब ४०० देखि ५०० बाघ धान्न सक्ने बताए, अर्थात् देश सीमा नजिक पुग्दै हुन सक्छ।
      </div>
      <p class="source">स्रोत: द काठमाडौं पोस्ट, ३० जुलाई २०२६।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>बाघ नेपालको राष्ट्रिय पशु होइन। संविधानले गाईलाई तोकेको छ। <a href="/ne/national-animal/">राष्ट्रिय पशु पृष्ठ</a> हेर्नुहोस्।</li>
          <li>सन् २००९ मा गणना गरिएको १२१ भन्दा सन् २०२६ को सङ्ख्या तीन गुणाभन्दा बढी हो।</li>
        </ul>
      </div>
    </section>
'''
TG_NE_FAQ = [
 ("सन् २०२६ मा नेपालमा कति बाघ छन्?", "सन् २०२६ को राष्ट्रिय बाघ गणनाले नेपालमा ४२९ वटा बाघ गणना गर्‍यो, जुन रेकर्ड हो र सन् २०२२ को ३५५ भन्दा बढी हो।"),
 ("नेपालको कुन राष्ट्रिय निकुञ्जमा सबैभन्दा धेरै बाघ छन्?", "२०२६ को गणनामा चितवन राष्ट्रिय निकुञ्ज र मध्यवर्ती क्षेत्रमा १४५, त्यसपछि बर्दिया (११२) र पर्सा (७१)।"),
 ("सन् २०२२ मा नेपालमा कति बाघ थिए?", "सन् २०२२ को गणनामा नेपालमा ३५५ बाघ थिए।"),
 ("के नेपालमा बाघ बढ्दै छन्?", "बढ्दै छन्। सङ्ख्या सन् २००९ को १२१ बाट २०२६ मा ४२९ पुग्यो। पाँचमध्ये चार बाघ निकुञ्जमा बढ्यो, बर्दियामा १२५ बाट ११२ मा घट्यो।"),
 ("नेपाल बाघ गणना २०२६ कहिले सार्वजनिक भयो?", "यो विश्व बाघ दिवस, २९ जुलाई २०२६ मा काठमाडौंमा सार्वजनिक भयो।"),
 ("२०२६ को बाघ गणना कसरी गरियो?", "क्यामेरा ट्र्यापबाट, सन् २०२५ डिसेम्बर ३१ देखि २०२६ अप्रिल २३ सम्म चलेको सर्वेक्षणमा।"),
 ("नेपालमा अर्को बाघ गणना कहिले हुन्छ?", "गणना चार वर्षमा एकपटक हुन्छ, त्यसैले अर्को करिब २०३० तिर अपेक्षित छ।"),
 ("के बाघ नेपालको राष्ट्रिय पशु हो?", "होइन। नेपालको संविधानअनुसार राष्ट्रिय पशु गाई हो।"),
]

# ---------------- National days ----------------
ND2_EN_BODY = '''    <section>
      <p class="lede">Nepal marks <strong>five major national days</strong>, each on a fixed Bikram Sambat (BS) date: <strong>Republic Day</strong> (Jestha 15), <strong>National Day</strong> (Ashoj 3), <strong>National Unity Day</strong> (Poush 27), <strong>Martyrs' Day</strong> (Magh 16) and <strong>Democracy Day</strong> (Falgun 7).</p>
    </section>

    <section id="list">
      <h2>National Days of Nepal and What They Mark</h2>
      ''' + fig('nepal_national_days_calendar', 'Timeline of five national days of Nepal in BS order: Jestha 15, Ashoj 3, Poush 27, Magh 16 and Falgun 7', 'Nepal national days in Bikram Sambat order.') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>Day</th><th>BS date</th><th>What it marks</th><th>Next date</th></tr></thead>
          <tbody>
            <tr><td>National Unity Day (Prithvi Jayanti)</td><td>Poush 27</td><td>Birth anniversary of Prithvi Narayan Shah (1723 to 1775)</td><td>Mon, 11 Jan 2027</td></tr>
            <tr><td>Martyrs' Day (Shahid Diwas)</td><td>Magh 16</td><td>Four martyrs executed in the Rana period</td><td>Sat, 30 Jan 2027</td></tr>
            <tr><td>Democracy Day (Prajatantra Diwas)</td><td>Falgun 7</td><td>End of the Rana regime, 2007 BS (1951)</td><td>Fri, 19 Feb 2027</td></tr>
            <tr><td>Republic Day (Ganatantra Diwas)</td><td>Jestha 15</td><td>Nepal became a federal democratic republic, 28 May 2008</td><td>Sat, 29 May 2027</td></tr>
            <tr><td>National Day / Constitution Day</td><td>Ashoj 3</td><td>Constitution promulgated, 20 Sep 2015</td><td>Sun, 19 Sep 2027</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Dates calculated from the BS calendar tables on <a href="https://converter.thenepal.io/bs-to-ad/" rel="noopener">converter.thenepal.io</a>; the English date can differ by a day in other years. Republic Day source: Wikipedia, Republic Day (Nepal).</p>
    </section>

    <section id="each">
      <h2>The Five Days in Detail</h2>
      <h3>National Unity Day: Poush 27</h3>
      <p>Observed on the birth anniversary of Prithvi Narayan Shah, the king of Gorkha who began the unification of Nepal. Also called Prithvi Jayanti. See the <a href="https://converter.thenepal.io/2083/prithvi-jayanti" rel="noopener">Prithvi Jayanti 2083 date</a>.</p>
      <h3>Martyrs' Day: Magh 16</h3>
      <p>Remembers four people executed during the Rana period: Shukraraj Shastri, Dharma Bhakta Mathema, Gangalal Shrestha and Dashrath Chand. Wreaths are laid at memorials. See the <a href="https://converter.thenepal.io/2083/shahid-diwas" rel="noopener">Martyrs' Day 2083 date</a>.</p>
      <h3>Democracy Day: Falgun 7</h3>
      <p>Marks the end of Rana rule on Falgun 7, 2007 BS (February 1951) and the start of democratic politics. See the <a href="https://converter.thenepal.io/2083/prajatantra-diwas" rel="noopener">Democracy Day 2083 date</a>.</p>
      <h3>Republic Day: Jestha 15</h3>
      <p>Jestha 15, 2065 BS is 28 May 2008, when Nepal became a federal democratic republic after the Constituent Assembly ended the monarchy. Wikipedia notes that the holiday has been cut since 2019 and the day is marked with programmes at workplaces, while our holiday list still shows it, so check your office or school notice.</p>
      <h3>National Day: Ashoj 3</h3>
      <p>The day the current Constitution was promulgated, on 20 September 2015. It is the official National Day by Cabinet decision. Read the full story on our <a href="/national-day/">National Day of Nepal page</a>.</p>
      <div class="status warn">
        <b>Which one is "the" national day?</b> The Cabinet decided in 2016 that <strong>20 September (Ashoj 3)</strong> is National Day. An earlier government had picked 28 May, the date Nepal became a republic, according to the Kathmandu Post. The other four are national days of remembrance or celebration but are not "the" National Day.
      </div>
    </section>

    <section id="holidays">
      <h2>Are They Public Holidays?</h2>
      <p>Prithvi Jayanti, Martyrs' Day, Democracy Day and Constitution Day are national holidays in the 2083 holiday list. In 2083, Martyrs' Day (Saturday, 30 January 2027) falls on a weekly holiday. See the full <a href="https://converter.thenepal.io/2083/nepal-public-holidays" rel="noopener">Nepal public holidays 2083</a> list, and the <a href="https://converter.thenepal.io/bs-to-ad/" rel="noopener">BS to AD converter</a> to check any date.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>All five days follow the Bikram Sambat calendar, so their English dates shift by a day between years.</li>
          <li>The national flag, anthem and emblem are fixed by the Constitution, but none of these national days is written into it.</li>
        </ul>
      </div>
    </section>
'''
ND2_EN_FAQ = [
 ("What are the national days of Nepal?", "Republic Day (Jestha 15), National Day (Ashoj 3), National Unity Day (Poush 27), Martyrs' Day (Magh 16) and Democracy Day (Falgun 7)."),
 ("Which is the national day of Nepal?", "National Day is 20 September (Ashoj 3), the day the Constitution was promulgated in 2015, as decided by the Cabinet in 2016."),
 ("When is Republic Day in Nepal?", "Republic Day is on Jestha 15 each year. Jestha 15, 2084 BS is Saturday, 29 May 2027."),
 ("When is Democracy Day in Nepal?", "Democracy Day is on Falgun 7. In 2083 BS it is Friday, 19 February 2027."),
 ("When is Martyrs' Day in Nepal?", "Martyrs' Day is on Magh 16. In 2083 BS it is Saturday, 30 January 2027."),
 ("When is National Unity Day (Prithvi Jayanti)?", "Prithvi Jayanti is on Poush 27. In 2083 BS it is Monday, 11 January 2027."),
 ("Who are the four martyrs of Nepal?", "Shukraraj Shastri, Dharma Bhakta Mathema, Gangalal Shrestha and Dashrath Chand, remembered on Magh 16."),
 ("Why do national days change dates in English?", "They follow the Bikram Sambat calendar, whose months do not match English months exactly, so the English date can shift by a day."),
]
ND2_NE_BODY = '''    <section>
      <p class="lede">नेपालले विक्रम संवत्को निश्चित मितिमा <strong>पाँचवटा प्रमुख राष्ट्रिय दिवस</strong> मनाउँछ: <strong>गणतन्त्र दिवस</strong> (जेठ १५), <strong>राष्ट्रिय दिवस</strong> (असोज ३), <strong>राष्ट्रिय एकता दिवस</strong> (पौष २७), <strong>शहीद दिवस</strong> (माघ १६) र <strong>प्रजातन्त्र दिवस</strong> (फागुन ७)।</p>
    </section>

    <section id="list">
      <h2>नेपालका राष्ट्रिय दिवस र ती के सम्झिन्छन्</h2>
      ''' + fig('nepal_national_days_calendar', 'विक्रम संवत् क्रममा नेपालका पाँच राष्ट्रिय दिवसको समयरेखा: जेठ १५, असोज ३, पौष २७, माघ १६ र फागुन ७', 'विक्रम संवत् क्रममा नेपालका राष्ट्रिय दिवस।') + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>दिवस</th><th>वि.सं. मिति</th><th>के सम्झिन्छ</th><th>अर्को मिति</th></tr></thead>
          <tbody>
            <tr><td>राष्ट्रिय एकता दिवस (पृथ्वी जयन्ती)</td><td>पौष २७</td><td>पृथ्वीनारायण शाहको जन्मजयन्ती (१७२३ देखि १७७५)</td><td>सोमबार, ११ जनवरी २०२७</td></tr>
            <tr><td>शहीद दिवस</td><td>माघ १६</td><td>राणाकालमा मृत्युदण्ड पाएका चार शहीद</td><td>शनिबार, ३० जनवरी २०२७</td></tr>
            <tr><td>प्रजातन्त्र दिवस</td><td>फागुन ७</td><td>राणा शासनको अन्त्य, २००७ साल (१९५१)</td><td>शुक्रबार, १९ फेब्रुअरी २०२७</td></tr>
            <tr><td>गणतन्त्र दिवस</td><td>जेठ १५</td><td>नेपाल सङ्घीय लोकतान्त्रिक गणतन्त्र बन्यो, २८ मे २००८</td><td>शनिबार, २९ मे २०२७</td></tr>
            <tr><td>राष्ट्रिय दिवस / संविधान दिवस</td><td>असोज ३</td><td>संविधान जारी, २० सेप्टेम्बर २०१५</td><td>आइतबार, १९ सेप्टेम्बर २०२७</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">मितिहरू <a href="https://converter.thenepal.io/bs-to-ad/" rel="noopener">converter.thenepal.io</a> का वि.सं. तालिकाबाट गणना गरिएको हो; अन्य वर्षमा अंग्रेजी मिति एक दिन फरक पर्न सक्छ। गणतन्त्र दिवसको स्रोत: Wikipedia, Republic Day (Nepal)।</p>
    </section>

    <section id="each">
      <h2>पाँच दिवसको विस्तार</h2>
      <h3>राष्ट्रिय एकता दिवस: पौष २७</h3>
      <p>नेपाल एकीकरण सुरु गर्ने गोरखाका राजा पृथ्वीनारायण शाहको जन्मजयन्तीमा मनाइन्छ। यसलाई पृथ्वी जयन्ती पनि भनिन्छ। <a href="https://converter.thenepal.io/2083/prithvi-jayanti" rel="noopener">पृथ्वी जयन्ती २०८३ को मिति</a> हेर्नुहोस्।</p>
      <h3>शहीद दिवस: माघ १६</h3>
      <p>राणाकालमा मृत्युदण्ड पाएका चार जना शुक्रराज शास्त्री, धर्मभक्त माथेमा, गंगालाल श्रेष्ठ र दशरथ चन्दको सम्झना गरिन्छ। स्मारकमा माल्यार्पण हुन्छ। <a href="https://converter.thenepal.io/2083/shahid-diwas" rel="noopener">शहीद दिवस २०८३ को मिति</a> हेर्नुहोस्।</p>
      <h3>प्रजातन्त्र दिवस: फागुन ७</h3>
      <p>फागुन ७, २००७ साल (फेब्रुअरी १९५१) मा राणा शासन अन्त्य भई लोकतान्त्रिक राजनीति सुरु भएको दिन। <a href="https://converter.thenepal.io/2083/prajatantra-diwas" rel="noopener">प्रजातन्त्र दिवस २०८३ को मिति</a> हेर्नुहोस्।</p>
      <h3>गणतन्त्र दिवस: जेठ १५</h3>
      <p>जेठ १५, २०६५ साल अर्थात् २८ मे २००८ मा संविधानसभाले राजतन्त्र अन्त्य गरेपछि नेपाल सङ्घीय लोकतान्त्रिक गणतन्त्र बन्यो। विकिपिडियाका अनुसार सन् २०१९ देखि यो बिदा कटौती गरिएको छ र कार्यालयमा कार्यक्रम गरी मनाइन्छ, जबकि हाम्रो बिदा सूचीमा अझै देखिन्छ, त्यसैले आफ्नो कार्यालय वा विद्यालयको सूचना हेर्नुहोस्।</p>
      <h3>राष्ट्रिय दिवस: असोज ३</h3>
      <p>सन् २०१५ सेप्टेम्बर २० मा हालको संविधान जारी भएको दिन। मन्त्रिपरिषद्को निर्णयले यही आधिकारिक राष्ट्रिय दिवस हो। पूरा कथा <a href="/ne/national-day/">नेपालको राष्ट्रिय दिवस</a> पृष्ठमा पढ्नुहोस्।</p>
      <div class="status warn">
        <b>"राष्ट्रिय दिवस" कुन हो?</b> मन्त्रिपरिषद्ले सन् २०१६ मा <strong>२० सेप्टेम्बर (असोज ३)</strong> लाई राष्ट्रिय दिवस तोक्यो। द काठमाडौं पोस्टका अनुसार अघिल्लो सरकारले नेपाल गणतन्त्र बनेको मिति २८ मे तोकेको थियो। अन्य चार स्मरण वा उत्सवका राष्ट्रिय दिवस हुन्, तर "राष्ट्रिय दिवस" होइनन्।
      </div>
    </section>

    <section id="holidays">
      <h2>के यी सार्वजनिक बिदा हुन्?</h2>
      <p>पृथ्वी जयन्ती, शहीद दिवस, प्रजातन्त्र दिवस र संविधान दिवस २०८३ को बिदा सूचीमा राष्ट्रिय बिदा हुन्। २०८३ मा शहीद दिवस (शनिबार, ३० जनवरी २०२७) साप्ताहिक बिदामा पर्छ। पूरा <a href="https://converter.thenepal.io/2083/nepal-public-holidays" rel="noopener">नेपाल सार्वजनिक बिदा २०८३</a> सूची र कुनै पनि मिति जाँच्न <a href="https://converter.thenepal.io/bs-to-ad/" rel="noopener">BS to AD कन्भर्टर</a> हेर्नुहोस्।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>पाँचै दिवस विक्रम संवत् अनुसार पर्छन्, त्यसैले अंग्रेजी मिति वर्षपिच्छे एक दिन सर्न सक्छ।</li>
          <li>राष्ट्रिय झण्डा, राष्ट्रगान र प्रतीक चिन्ह संविधानले तोकेको हो, तर यी राष्ट्रिय दिवसमध्ये कुनै संविधानमा लेखिएको छैन।</li>
        </ul>
      </div>
    </section>
'''
ND2_NE_FAQ = [
 ("नेपालका राष्ट्रिय दिवस कुन कुन हुन्?", "गणतन्त्र दिवस (जेठ १५), राष्ट्रिय दिवस (असोज ३), राष्ट्रिय एकता दिवस (पौष २७), शहीद दिवस (माघ १६) र प्रजातन्त्र दिवस (फागुन ७)।"),
 ("नेपालको राष्ट्रिय दिवस कुन हो?", "राष्ट्रिय दिवस २० सेप्टेम्बर (असोज ३) हो, जुन दिन सन् २०१५ मा संविधान जारी भयो। मन्त्रिपरिषद्ले २०१६ मा यो तोक्यो।"),
 ("गणतन्त्र दिवस कहिले हो?", "गणतन्त्र दिवस हरेक वर्ष जेठ १५ मा पर्छ। २०८४ साल जेठ १५ शनिबार, २९ मे २०२७ हो।"),
 ("प्रजातन्त्र दिवस कहिले हो?", "प्रजातन्त्र दिवस फागुन ७ मा पर्छ। २०८३ मा शुक्रबार, १९ फेब्रुअरी २०२७ हो।"),
 ("शहीद दिवस कहिले हो?", "शहीद दिवस माघ १६ मा पर्छ। २०८३ मा शनिबार, ३० जनवरी २०२७ हो।"),
 ("राष्ट्रिय एकता दिवस (पृथ्वी जयन्ती) कहिले हो?", "पृथ्वी जयन्ती पौष २७ मा पर्छ। २०८३ मा सोमबार, ११ जनवरी २०२७ हो।"),
 ("नेपालका चार शहीद को हुन्?", "शुक्रराज शास्त्री, धर्मभक्त माथेमा, गंगालाल श्रेष्ठ र दशरथ चन्द, जसलाई माघ १६ मा सम्झिन्छ।"),
 ("राष्ट्रिय दिवसको अंग्रेजी मिति किन फेरिन्छ?", "यी विक्रम संवत् अनुसार पर्छन्, जसका महिना अंग्रेजी महिनासँग ठ्याक्कै मिल्दैनन्, त्यसैले अंग्रेजी मिति एक दिन सर्न सक्छ।"),
]

EXTRA_PAGES = EXTRA_PAGES + [
 _mk('national-parks-of-nepal', 'nepal_national_parks_hero.webp', 'National parks of Nepal', 'https://en.wikipedia.org/wiki/List_of_protected_areas_of_Nepal',
  _en('National Parks of Nepal: List of All 13 Parks (Area and Year)',
      'Nepal has 13 national parks, including the new Chhayanath (2025). Full list with year, area, highlights, plus reserves and conservation areas.',
      'National Parks of Nepal: All 13 Parks', 'All 13 national parks of Nepal with year, area and highlights, updated for Chhayanath National Park (2025).',
      'The 13 national parks of Nepal with year established, area, wildlife highlights, reserves and conservation areas.', 'National Parks of Nepal',
      'Infographic: 13 national parks of Nepal', 'National Parks', 'National Parks <em>of Nepal</em>',
      '<strong>Nepal has 13 national parks.</strong> The newest, Chhayanath in Mugu, was added in 2025. Full list with year, area and highlights.',
      ['13 parks', 'Chhayanath 2025', 'Updated 2026'],
      [('Total', '13 national parks', False), ('Oldest', 'Chitwan, 1973', False), ('Newest', 'Chhayanath, 2025', False), ('Largest', 'Shey Phoksundo, about 2,712 km²', False), ('Smallest', 'Rara, about 106 km²', False), ('World Heritage', 'Sagarmatha, Chitwan', False)],
      ('राष्ट्रिय निकुञ्ज', 'Rastriya Nikunja', 'raash-tree-ya ni-kun-ja'), NP_EN_BODY, NP_EN_FAQ, REL_NP, 'National parks protect Nepal\'s national animals, birds and landscapes.'),
  _ne('नेपालका राष्ट्रिय निकुञ्ज: सबै १३ को सूची (क्षेत्रफल र साल)',
      'नेपालमा १३ राष्ट्रिय निकुञ्ज छन्, नयाँ छायाँनाथ (२०२५) सहित। साल, क्षेत्रफल, विशेषता, आरक्ष र संरक्षण क्षेत्रसहितको पूरा सूची।',
      'नेपालका राष्ट्रिय निकुञ्ज: सबै १३', 'नेपालका सबै १३ राष्ट्रिय निकुञ्ज साल, क्षेत्रफल र विशेषतासहित, छायाँनाथ राष्ट्रिय निकुञ्ज (२०२५) सहित अद्यावधिक।',
      'नेपालका १३ राष्ट्रिय निकुञ्ज: स्थापना साल, क्षेत्रफल, वन्यजन्तुका विशेषता, आरक्ष र संरक्षण क्षेत्र।', 'नेपालका राष्ट्रिय निकुञ्ज',
      'नेपालका १३ राष्ट्रिय निकुञ्जको इन्फोग्राफिक', 'राष्ट्रिय निकुञ्ज', 'नेपालका <em>राष्ट्रिय निकुञ्ज</em>',
      '<strong>नेपालमा १३ वटा राष्ट्रिय निकुञ्ज छन्।</strong> सबैभन्दा नयाँ, मुगुको छायाँनाथ, सन् २०२५ मा थपियो। साल, क्षेत्रफल र विशेषतासहितको पूरा सूची।',
      ['१३ निकुञ्ज', 'छायाँनाथ २०२५', 'अद्यावधिक २०२६'],
      [('जम्मा', '१३ राष्ट्रिय निकुञ्ज', False), ('सबैभन्दा पुरानो', 'चितवन, १९७३', False), ('सबैभन्दा नयाँ', 'छायाँनाथ, २०२५', False), ('सबैभन्दा ठूलो', 'शे-फोक्सुन्डो, करिब २,७१२ वर्ग कि.मी.', False), ('सबैभन्दा सानो', 'रारा, करिब १०६ वर्ग कि.मी.', False), ('विश्व सम्पदा', 'सगरमाथा, चितवन', False)],
      ('राष्ट्रिय निकुञ्ज', 'Rastriya Nikunja', 'राष्ट्रिय निकुञ्ज'), NP_NE_BODY, NP_NE_FAQ, REL_NP_NE, 'राष्ट्रिय निकुञ्जहरूले नेपालका राष्ट्रिय पशुपंक्षी र भूदृश्य जोगाउँछन्।')),
 _mk('nepal-tiger-census-2026', 'nepal_tiger_census_hero.webp', 'Tiger census of Nepal 2026', 'https://en.wikipedia.org/wiki/Bengal_tiger',
  _en('Nepal Tiger Census 2026: 429 Tigers, Park by Park Count',
      "Nepal's 2026 tiger census counted a record 429 tigers, up from 355 in 2022. Count by park, how it was done, and the conflict concerns.",
      'Nepal Tiger Census 2026: 429 Tigers', 'A record 429 tigers in Nepal. Park-by-park counts for 2022 and 2026, method and human-tiger conflict figures.',
      "Nepal's 2026 national tiger census: 429 tigers, counts by park, method and conflict figures.", 'Tiger Census 2026',
      'Infographic: Nepal counted 429 tigers in 2026', 'Tiger census 2026', 'Nepal Tiger Census <em>2026</em>',
      '<strong>Nepal has 429 wild tigers, a record.</strong> The 2026 national census, released on Global Tiger Day, is up 74 from 355 in 2022.',
      ['429 tigers', 'Up 74 since 2022', 'Released 29 July 2026'],
      [('Tigers (2026)', '429', False), ('Tigers (2022)', '355', False), ('Largest park', 'Chitwan, 145', False), ('Only decline', 'Bardiya, 125 to 112', False), ('Method', 'Camera traps, Dec 2025 to Apr 2026', False), ('Released', '29 July 2026', False)],
      ('बाघ', 'Bagh', 'bagh'), TG_EN_BODY, TG_EN_FAQ, REL_TG, 'The tiger census reflects the health of Nepal\'s Terai national parks.'),
  _ne('नेपालमा बाघको सङ्ख्या २०२६: ४२९ बाघ, निकुञ्जअनुसार गणना',
      'नेपालको २०२६ को बाघ गणनाले रेकर्ड ४२९ बाघ भेट्यो, सन् २०२२ को ३५५ बाट। निकुञ्जअनुसार गणना, विधि र द्वन्द्वका चिन्ता।',
      'नेपालमा बाघ गणना २०२६: ४२९ बाघ', 'नेपालमा रेकर्ड ४२९ बाघ। २०२२ र २०२६ को निकुञ्जअनुसार गणना, विधि र मानव-बाघ द्वन्द्वका तथ्यांक।',
      'नेपालको २०२६ को राष्ट्रिय बाघ गणना: ४२९ बाघ, निकुञ्जअनुसार गणना, विधि र द्वन्द्वका तथ्यांक।', 'बाघ गणना २०२६',
      'नेपालमा सन् २०२६ मा ४२९ बाघ गणना भएको इन्फोग्राफिक', 'बाघ गणना २०२६', 'नेपालमा बाघ गणना <em>२०२६</em>',
      '<strong>नेपालमा ४२९ वटा जङ्गली बाघ छन्, रेकर्ड सङ्ख्या।</strong> विश्व बाघ दिवसमा सार्वजनिक २०२६ को गणना सन् २०२२ को ३५५ भन्दा ७४ ले बढी छ।',
      ['४२९ बाघ', '२०२२ भन्दा ७४ बढी', '२९ जुलाई २०२६ मा सार्वजनिक'],
      [('बाघ (२०२६)', '४२९', False), ('बाघ (२०२२)', '३५५', False), ('सबैभन्दा ठूलो निकुञ्ज', 'चितवन, १४५', False), ('एक मात्र घटेको', 'बर्दिया, १२५ बाट ११२', False), ('विधि', 'क्यामेरा ट्र्याप, डिसेम्बर २०२५ देखि अप्रिल २०२६', False), ('सार्वजनिक', '२९ जुलाई २०२६', False)],
      ('बाघ', 'Bagh', 'बाघ'), TG_NE_BODY, TG_NE_FAQ, REL_TG_NE, 'बाघ गणनाले नेपालका तराईका राष्ट्रिय निकुञ्जको अवस्था देखाउँछ।')),
 _mk('national-days-of-nepal', 'nepal_national_days_hero.webp', 'National days of Nepal', 'https://en.wikipedia.org/wiki/Republic_Day_(Nepal)',
  _en('National Days of Nepal: 5 Days, BS Dates and Next Date',
      'The 5 national days of Nepal with BS dates and next English dates: Republic Day, National Day, Unity Day, Martyrs\' Day and Democracy Day.',
      'National Days of Nepal: 5 Days and Dates', 'Republic Day, National Day, Unity Day, Martyrs\' Day and Democracy Day: BS dates, meaning and the next date.',
      'The five national days of Nepal with Bikram Sambat dates, what each marks and the next English dates.', 'National Days of Nepal',
      'Infographic: national days of Nepal', 'National days', 'National Days <em>of Nepal</em>',
      '<strong>Nepal has five major national days:</strong> Republic Day (Jestha 15), National Day (Ashoj 3), Unity Day (Poush 27), Martyrs\' Day (Magh 16) and Democracy Day (Falgun 7).',
      ['5 days', 'Fixed BS dates', 'Next dates 2027'],
      [('Unity Day', 'Poush 27 (11 Jan 2027)', False), ('Martyrs\' Day', 'Magh 16 (30 Jan 2027)', False), ('Democracy Day', 'Falgun 7 (19 Feb 2027)', False), ('Republic Day', 'Jestha 15 (29 May 2027)', False), ('National Day', 'Ashoj 3 (19 Sep 2027)', False)],
      ('राष्ट्रिय दिवस', 'Rastriya Diwas', 'raash-tree-ya di-was'), ND2_EN_BODY, ND2_EN_FAQ, REL_ND2, 'National days sit alongside the official symbols of the country.'),
  _ne('नेपालका राष्ट्रिय दिवस: गणतन्त्र, एकता, शहीद, प्रजातन्त्र दिवसको मिति',
      'नेपालका ५ राष्ट्रिय दिवस वि.सं. मिति र अर्को अंग्रेजी मितिसहित: गणतन्त्र, राष्ट्रिय, एकता, शहीद र प्रजातन्त्र दिवस।',
      'नेपालका राष्ट्रिय दिवस: ५ दिन र मिति', 'गणतन्त्र, राष्ट्रिय, एकता, शहीद र प्रजातन्त्र दिवस: वि.सं. मिति, अर्थ र अर्को मिति।',
      'नेपालका पाँच राष्ट्रिय दिवस वि.सं. मिति, के सम्झिन्छ र अर्को अंग्रेजी मितिसहित।', 'नेपालका राष्ट्रिय दिवस',
      'नेपालका राष्ट्रिय दिवसको इन्फोग्राफिक', 'राष्ट्रिय दिवस', 'नेपालका <em>राष्ट्रिय दिवस</em>',
      '<strong>नेपालमा पाँचवटा प्रमुख राष्ट्रिय दिवस छन्:</strong> गणतन्त्र (जेठ १५), राष्ट्रिय (असोज ३), एकता (पौष २७), शहीद (माघ १६) र प्रजातन्त्र दिवस (फागुन ७)।',
      ['५ दिवस', 'निश्चित वि.सं. मिति', '२०२७ का अर्को मिति'],
      [('एकता दिवस', 'पौष २७ (११ जनवरी २०२७)', False), ('शहीद दिवस', 'माघ १६ (३० जनवरी २०२७)', False), ('प्रजातन्त्र दिवस', 'फागुन ७ (१९ फेब्रुअरी २०२७)', False), ('गणतन्त्र दिवस', 'जेठ १५ (२९ मे २०२७)', False), ('राष्ट्रिय दिवस', 'असोज ३ (१९ सेप्टेम्बर २०२७)', False)],
      ('राष्ट्रिय दिवस', 'Rastriya Diwas', 'राष्ट्रिय दिवस'), ND2_NE_BODY, ND2_NE_FAQ, REL_ND2_NE, 'राष्ट्रिय दिवस देशका आधिकारिक चिन्हहरूसँगै पर्छन्।')),
]
