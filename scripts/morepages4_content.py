# -*- coding: utf-8 -*-
# Page: /national-symbols-with-pictures/ (EN + NE): gallery of all 23 symbols with pictures, names and legal status. Uses _mk/_en/_ne/fig.
# Status basis: Constitution of Nepal 2015 Arts 8-9 (see /official-vs-unofficial/ and its sources); volleyball 22 May 2017 and orange 12 Apr 2024 as on our sport and fruit pages.
GAL = [  # slug, EN name, NE name, group (c=constitution, d=declared, u=official use, k=customary)
 ('national-flag', 'Flag', 'झण्डा', 'c'), ('national-anthem', 'Anthem: Sayaun Thunga Phulka', 'राष्ट्रगान: सयौँ थुँगा फूलका', 'c'), ('national-emblem', 'Emblem (coat of arms)', 'प्रतीक चिन्ह', 'c'),
 ('national-flower', 'Flower: Rhododendron', 'फूल: लालीगुराँस', 'c'), ('national-color', 'Colour: Crimson', 'रङ: सिन्दुरे रातो', 'c'), ('national-animal', 'Animal: Cow', 'पशु: गाई', 'c'),
 ('national-bird', 'Bird: Danphe (Himalayan Monal)', 'चरा: डाँफे', 'c'), ('national-language', 'Language: Nepali', 'भाषा: नेपाली', 'c'),
 ('national-sport', 'Game: Volleyball', 'खेल: भलिबल', 'd'), ('national-fruit', 'Fruit: Orange', 'फल: सुन्तला', 'd'),
 ('national-calendar', 'Calendar: Bikram Sambat', 'पात्रो: विक्रम सम्वत्', 'u'), ('national-currency', 'Currency: Nepalese rupee', 'मुद्रा: नेपाली रुपैयाँ', 'u'),
 ('national-tree', 'Tree: Peepal', 'रूख: पीपल', 'k'), ('national-fish', 'Fish: Asala (Golden Mahseer)', 'माछा: असला', 'k'), ('national-butterfly', 'Butterfly: Krishna Peacock', 'पुतली: कृष्ण मयूर', 'k'),
 ('national-food', 'Food: Dal Bhat', 'खाना: दालभात', 'k'), ('national-weapon', 'Weapon: Khukuri', 'हतियार: खुकुरी', 'k'), ('national-dress', 'Dress: Daura Suruwal, Gunyu Cholo', 'पोशाक: दौरा सुरुवाल, गुन्यू चोलो', 'k'),
 ('national-dance', 'Dance: Deuda and Maruni', 'नृत्य: देउडा र मारुनी', 'k'), ('national-monument', 'Monument: Dharahara', 'स्मारक: धरहरा', 'k'), ('national-cave', 'Cave: Siddha Gufa', 'गुफा: सिद्ध गुफा', 'k'),
 ('national-museum', 'Museum: National Museum', 'संग्रहालय: राष्ट्रिय संग्रहालय', 'k'), ('national-everest', 'Highest peak: Sagarmatha (Everest)', 'अग्लो शिखर: सगरमाथा', 'k'),
]
GRP_EN = {'c': ('1. Named in the Constitution (2015)', 'Flag, anthem, emblem, flower, colour, animal and bird are written into Articles 8 and 9. The language provisions are in Articles 6 and 7.'),
          'd': ('2. Declared by the government', 'Not in the Constitution, but announced by the Government of Nepal.'),
          'u': ('3. In official use', 'Used by the state, but not among the symbols named in Articles 8 and 9.'),
          'k': ('4. Customary or popular', 'Widely called "national" but with no confirmed legal designation. See the <a href="/official-vs-unofficial/">official vs unofficial</a> guide.')}
GRP_NE = {'c': ('१. संविधान (२०१५) मा उल्लेखित', 'झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु र चरा धारा ८ र ९ मा लेखिएका छन्। भाषासम्बन्धी व्यवस्था धारा ६ र ७ मा छन्।'),
          'd': ('२. सरकारले घोषणा गरेका', 'संविधानमा छैनन्, तर नेपाल सरकारले घोषणा गरेको।'),
          'u': ('३. सरकारी प्रयोगमा', 'राज्यले प्रयोग गर्छ, तर धारा ८ र ९ मा नाम उल्लेख गरिएका चिन्हमा पर्दैनन्।'),
          'k': ('४. परम्परागत वा लोकप्रिय', '"राष्ट्रिय" भनिए पनि कानुनी तोक्ने पुष्टि भएको छैन। <a href="/ne/official-vs-unofficial/">आधिकारिक कि परम्परागत</a> पृष्ठ हेर्नुहोस्।')}
def _grid(lang):
    pre = '' if lang == 'en' else '/ne'; GRP = GRP_EN if lang == 'en' else GRP_NE; out = ''
    for g in 'cduk':
        cards = ''.join('<a href="%s/%s/" style="display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid rgba(0,0,0,.1);border-radius:12px;overflow:hidden">'
                        '<img src="/photos/thumbs/%s.webp" alt="%s" width="480" height="300" loading="lazy" decoding="async" style="width:100%%;height:auto;display:block">'
                        '<span style="display:block;padding:10px 12px;font-weight:600;font-size:.95rem;line-height:1.3">%s</span></a>' % (pre, s, s, (n_en if lang == 'en' else n_ne), (n_en if lang == 'en' else n_ne))
                        for s, n_en, n_ne, gg in GAL if gg == g)
        out += '    <section id="g-%s">\n      <h2>%s</h2>\n      <p>%s</p>\n      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin:14px 0 26px">%s</div>\n    </section>\n' % (g, GRP[g][0], GRP[g][1], cards)
    return out

GL_EN_BODY = '''    <section>
      <p class="lede"><strong>Nepal's national symbols with pictures: 23 symbols are covered on this site.</strong> Seven are named in the Constitution (flag, anthem, emblem, flower, colour, animal and bird), two were declared by the government, and the rest are customary. Tap any picture for the full guide.</p>
      ''' + fig('nepal_national_symbols_chart', 'Chart of all 23 national symbols of Nepal with pictures and names: flag, anthem, emblem, flower, colour, animal, bird, language, game, fruit and more', 'All 23 national symbols of Nepal on one chart. Official (Constitution): flag, anthem, emblem, flower, colour, animal, bird.', w=1612, h=1004) + '''
    </section>

''' + _grid('en') + '''    <section id="names">
      <h2>National Symbols of Nepal: Quick List With Names</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Symbol</th><th>Name</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>National flag</td><td>Twin-pennant crimson flag with sun and moon</td><td>Constitution, Article 8</td></tr>
            <tr><td>National anthem</td><td>Sayaun Thunga Phulka</td><td>Constitution, Article 9(1)</td></tr>
            <tr><td>National emblem</td><td>Coat of arms with Everest, hills, Terai and a rhododendron garland</td><td>Constitution, Article 9(2)</td></tr>
            <tr><td>National flower</td><td>Rhododendron (Lali Gurans)</td><td>Constitution, Article 9(3)</td></tr>
            <tr><td>National colour</td><td>Crimson</td><td>Constitution, Article 9(3)</td></tr>
            <tr><td>National animal</td><td>Cow</td><td>Constitution, Article 9(3)</td></tr>
            <tr><td>National bird</td><td>Danphe (Himalayan Monal)</td><td>Constitution, Article 9(3)</td></tr>
            <tr><td>National game</td><td>Volleyball</td><td>Declared 22 May 2017</td></tr>
            <tr><td>National fruit</td><td>Orange</td><td>Council of Ministers, 12 April 2024</td></tr>
            <tr><td>Tree, fish, butterfly, food, weapon, dress, dance, monument, cave, museum, peak</td><td>Peepal, Asala, Krishna Peacock, Dal Bhat, Khukuri, Daura Suruwal and Gunyu Cholo, Deuda and Maruni, Dharahara, Siddha Gufa, National Museum, Sagarmatha</td><td>Customary; no confirmed designation</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: Constitution of Nepal 2015, Articles 6-9 (via constituteproject.org); government decisions as reported on our <a href="/national-sport/">national game</a> and <a href="/national-fruit/">national fruit</a> pages. Full sources on the <a href="/sources/">Sources &amp; Methodology</a> page.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>Nepal's flag is the only non-rectangular national flag in the world. See the <a href="/national-flag/">flag guide</a>.</li>
          <li>Test yourself with the <a href="/quiz/">Nepal symbols quiz</a>.</li>
        </ul>
      </div>
    </section>
'''
GL_EN_FAQ = [
 ("How many national symbols does Nepal have?", "This site covers 23 national symbols. The Constitution of Nepal names seven (flag, anthem, emblem, flower, colour, animal and bird) plus language provisions. Two more were declared by the government and the rest are customary."),
 ("What are the official national symbols of Nepal?", "The flag, the anthem (Sayaun Thunga Phulka), the emblem, the rhododendron (flower), crimson (colour), the cow (animal) and the danphe (bird), all in Articles 8 and 9 of the Constitution."),
 ("What is the national game of Nepal?", "Volleyball, declared by the Government of Nepal on 22 May 2017. Dandi Biyo is also widely called a traditional national game."),
 ("What is the national fruit of Nepal?", "The orange, recognised by the Council of Ministers on 12 April 2024, according to news reports."),
 ("Does Nepal have a national tree, fish or butterfly?", "We found no confirmed official designation. Peepal, Asala (Golden Mahseer) and the Krishna Peacock are the ones most often named."),
 ("Where can I see Nepal's national symbols with pictures?", "On this page: a chart of all 23 symbols and a picture card for each, with links to the full guide for every symbol."),
]
GL_NE_BODY = '''    <section>
      <p class="lede"><strong>नेपालका राष्ट्रिय चिन्हहरू तस्बिरसहित: यस साइटमा २३ चिन्ह समेटिएका छन्।</strong> सातवटा संविधानमा उल्लेखित छन् (झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु र चरा), दुईवटा सरकारले घोषणा गरेको र बाँकी परम्परागत हुन्। पूरा गाइडका लागि कुनै पनि तस्बिरमा थिच्नुहोस्।</p>
      ''' + fig('nepal_national_symbols_chart_ne', 'नेपालका सबै २३ राष्ट्रिय चिन्हहरू तस्बिर र नामसहितको चार्ट: झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु, चरा, भाषा, खेल, फल र अन्य', 'नेपालका सबै २३ राष्ट्रिय चिन्ह एउटै चार्टमा। संविधानमा उल्लेखित: झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु, चरा।', w=1612, h=1004) + '''
    </section>

''' + _grid('ne') + '''    <section id="names">
      <h2>नेपालका राष्ट्रिय चिन्ह: नामसहित छोटो सूची</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>चिन्ह</th><th>नाम</th><th>स्थिति</th></tr></thead>
          <tbody>
            <tr><td>राष्ट्रिय झण्डा</td><td>सूर्य र चन्द्रमासहितको दुई त्रिकोणे सिन्दुरे रातो झण्डा</td><td>संविधान, धारा ८</td></tr>
            <tr><td>राष्ट्रगान</td><td>सयौँ थुँगा फूलका</td><td>संविधान, धारा ९(१)</td></tr>
            <tr><td>प्रतीक चिन्ह</td><td>सगरमाथा, पहाड, तराई र लालीगुराँसको माला भएको प्रतीक</td><td>संविधान, धारा ९(२)</td></tr>
            <tr><td>राष्ट्रिय फूल</td><td>लालीगुराँस</td><td>संविधान, धारा ९(३)</td></tr>
            <tr><td>राष्ट्रिय रङ</td><td>सिन्दुरे रातो</td><td>संविधान, धारा ९(३)</td></tr>
            <tr><td>राष्ट्रिय पशु</td><td>गाई</td><td>संविधान, धारा ९(३)</td></tr>
            <tr><td>राष्ट्रिय चरा</td><td>डाँफे</td><td>संविधान, धारा ९(३)</td></tr>
            <tr><td>राष्ट्रिय खेल</td><td>भलिबल</td><td>२०१७ मे २२ मा घोषणा</td></tr>
            <tr><td>राष्ट्रिय फल</td><td>सुन्तला</td><td>मन्त्रिपरिषद्, २०२४ अप्रिल १२</td></tr>
            <tr><td>रूख, माछा, पुतली, खाना, हतियार, पोशाक, नृत्य, स्मारक, गुफा, संग्रहालय, शिखर</td><td>पीपल, असला, कृष्ण मयूर, दालभात, खुकुरी, दौरा सुरुवाल र गुन्यू चोलो, देउडा र मारुनी, धरहरा, सिद्ध गुफा, राष्ट्रिय संग्रहालय, सगरमाथा</td><td>परम्परागत; पुष्टि भएको तोकाइ छैन</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: नेपालको संविधान २०१५, धारा ६-९ (constituteproject.org मार्फत); सरकारी निर्णयहरू हाम्रो <a href="/ne/national-sport/">राष्ट्रिय खेल</a> र <a href="/ne/national-fruit/">राष्ट्रिय फल</a> पृष्ठमा उल्लेखित अनुसार। पूरा स्रोत <a href="/ne/sources/">स्रोत र कार्यविधि</a> पृष्ठमा।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>नेपालको झण्डा विश्वको एक मात्र चतुर्भुज नभएको राष्ट्रिय झण्डा हो। <a href="/ne/national-flag/">झण्डा गाइड</a> हेर्नुहोस्।</li>
          <li><a href="/ne/quiz/">नेपाल चिन्ह क्विज</a> मा आफूलाई परीक्षा गर्नुहोस्।</li>
        </ul>
      </div>
    </section>
'''
GL_NE_FAQ = [
 ("नेपालका कतिवटा राष्ट्रिय चिन्ह छन्?", "यस साइटमा २३ चिन्ह समेटिएका छन्। नेपालको संविधानले सातवटा (झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु र चरा) र भाषासम्बन्धी व्यवस्था उल्लेख गरेको छ। दुईवटा सरकारले घोषणा गरेको र बाँकी परम्परागत हुन्।"),
 ("नेपालका आधिकारिक राष्ट्रिय चिन्ह कुन कुन हुन्?", "झण्डा, राष्ट्रगान (सयौँ थुँगा फूलका), प्रतीक चिन्ह, लालीगुराँस (फूल), सिन्दुरे रातो (रङ), गाई (पशु) र डाँफे (चरा), संविधानको धारा ८ र ९ मा।"),
 ("नेपालको राष्ट्रिय खेल कुन हो?", "भलिबल, नेपाल सरकारले २०१७ मे २२ मा घोषणा गरेको। डण्डीबियो पनि परम्परागत राष्ट्रिय खेल भनिन्छ।"),
 ("नेपालको राष्ट्रिय फल कुन हो?", "सुन्तला, समाचारअनुसार मन्त्रिपरिषद्ले २०२४ अप्रिल १२ मा मान्यता दिएको।"),
 ("के नेपालको राष्ट्रिय रूख, माछा वा पुतली छ?", "पुष्टि भएको आधिकारिक तोकाइ भेटिएन। पीपल, असला र कृष्ण मयूर सबैभन्दा धेरै भनिने हुन्।"),
 ("नेपालका राष्ट्रिय चिन्ह तस्बिरसहित कहाँ हेर्ने?", "यही पृष्ठमा: सबै २३ चिन्हको चार्ट र प्रत्येकको तस्बिर कार्ड, हरेकको पूरा गाइडको लिङ्कसहित।"),
]
REL_GL = [('official-vs-unofficial', 'Official vs Unofficial Symbols'), ('quiz', 'Nepal Symbols Quiz'), ('national-flag', 'National Flag'), ('sources', 'Sources & Methodology')]
REL_GL_NE = [('official-vs-unofficial', 'आधिकारिक कि परम्परागत'), ('quiz', 'नेपाल चिन्ह क्विज'), ('national-flag', 'राष्ट्रिय झण्डा'), ('sources', 'स्रोत र कार्यविधि')]
EXTRA_PAGES = EXTRA_PAGES + [
 _mk('national-symbols-with-pictures', 'nepal_symbols_pictures_hero.webp', 'National symbols of Nepal', 'https://en.wikipedia.org/wiki/National_symbols_of_Nepal',
  _en('National Symbols of Nepal With Pictures and Names (All 23 Listed)',
      "National symbols of Nepal with pictures and names: flag, anthem, emblem, flower, colour, animal, bird and more. Which 7 are official and which are customary.",
      'National Symbols of Nepal With Pictures and Names', 'All 23 national symbols of Nepal on one chart with pictures, names and legal status. Which are official and which are customary.',
      'All 23 national symbols of Nepal with pictures, names and legal status.', 'Symbols With Pictures',
      'National symbols of Nepal with pictures and names', 'Picture guide', 'National Symbols <em>of Nepal</em>',
      '<strong>Nepal has 23 national symbols on this site, and 7 are named in the Constitution.</strong> Pictures, names and status for every one.',
      ['23 symbols', '7 in the Constitution', 'Chart + pictures'],
      [('Symbols covered', '23', False), ('In the Constitution', '7 (flag, anthem, emblem, flower, colour, animal, bird)', False), ('Declared by government', 'Game (2017), fruit (2024)', False), ('Customary', '11 others', False)],
      ('राष्ट्रिय चिन्ह', 'Rastriya Chinha', 'raash-tree-ya chin-ha'), GL_EN_BODY, GL_EN_FAQ, REL_GL, 'Every national symbol of Nepal, with its status.'),
  _ne('नेपालका राष्ट्रिय चिन्हहरू तस्बिर र नामसहित (सबै २३ को सूची)',
      'नेपालका राष्ट्रिय चिन्ह तस्बिर र नामसहित: झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु, चरा र अन्य। कुन ७ आधिकारिक र कुन परम्परागत।',
      'नेपालका राष्ट्रिय चिन्ह तस्बिर र नामसहित', 'नेपालका सबै २३ राष्ट्रिय चिन्ह एउटै चार्टमा तस्बिर, नाम र कानुनी स्थितिसहित। कुन आधिकारिक र कुन परम्परागत।',
      'नेपालका सबै २३ राष्ट्रिय चिन्ह तस्बिर, नाम र कानुनी स्थितिसहित।', 'तस्बिरसहित चिन्ह',
      'नेपालका राष्ट्रिय चिन्ह तस्बिर र नामसहित', 'तस्बिर गाइड', 'नेपालका <em>राष्ट्रिय चिन्ह</em>',
      '<strong>यस साइटमा नेपालका २३ राष्ट्रिय चिन्ह छन्, र ७ संविधानमा उल्लेखित छन्।</strong> प्रत्येकको तस्बिर, नाम र स्थिति।',
      ['२३ चिन्ह', '७ संविधानमा', 'चार्ट + तस्बिर'],
      [('समेटिएका चिन्ह', '२३', False), ('संविधानमा', '७ (झण्डा, राष्ट्रगान, प्रतीक चिन्ह, फूल, रङ, पशु, चरा)', False), ('सरकारले घोषणा', 'खेल (२०१७), फल (२०२४)', False), ('परम्परागत', '११ अन्य', False)],
      ('राष्ट्रिय चिन्ह', 'Rastriya Chinha', 'राष्ट्रिय चिन्ह'), GL_NE_BODY, GL_NE_FAQ, REL_GL_NE, 'नेपालका हरेक राष्ट्रिय चिन्ह, तिनको स्थितिसहित।'),
 ),
]
