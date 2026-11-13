# -*- coding: utf-8 -*-
# Official vs unofficial national symbols. Constitution of Nepal 2015 text via constituteproject.org:
# Art 8 flag (Schedule 1); Art 9(1) anthem (Schedule 2); Art 9(2) coat of arms (Schedule 3);
# Art 9(3) "Rhododendron Arboreum is the national flower, Crimson is the national color, the cow is the national animal" + Lophophorus national bird;
# Art 6 all mother tongues are national languages; Art 7 Nepali (Devanagari) language of official business.
# Cabinet items per our own pages: volleyball 22 May 2017 (sport page); orange recognised by Council of Ministers 12 Apr 2024 (Rising Nepal, fruit page).
def _row(href, name, basis, lang='en'):
    pre = '/ne' if lang == 'ne' else ''
    return '            <tr><td><a href="%s/%s/">%s</a></td><td>%s</td></tr>\n' % (pre, href, name, basis)
def _table(rows, h1, h2, lang):
    return '      <div class="table-wrap">\n        <table>\n          <thead><tr><th>%s</th><th>%s</th></tr></thead>\n          <tbody>\n%s          </tbody>\n        </table>\n      </div>\n' % (h1, h2, ''.join(_row(h, n, b, lang) for h, n, b in rows))

A_EN = [('national-flag','Flag','Article 8; drawing method in Schedule 1'),('national-anthem','Anthem','Article 9(1); text in Schedule 2'),('national-emblem','Emblem (coat of arms)','Article 9(2); Schedule 3'),
        ('national-flower','Flower — Rhododendron','Article 9(3): "The Rhododendron Arboreum is the national flower"'),('national-color','Colour — Crimson','Article 9(3): "Crimson is the national color"'),
        ('national-animal','Animal — Cow','Article 9(3): "the cow is the national animal"'),('national-bird','Bird — Danphe (Lophophorus)','Article 9(3): the Lophophorus is named as the national bird'),
        ('national-language','Language','Article 6: all mother tongues are national languages. Article 7: Nepali in Devanagari is the language of official business')]
B_EN = [('national-sport','Sport — Volleyball','Declared by the Government of Nepal on 22 May 2017 (Cabinet decision, as reported on our sport page)'),('national-fruit','Fruit — Orange','Recognised by the Council of Ministers on 12 April 2024 (news report; the species named in the decision text is not confirmed)')]
C_EN = [('national-calendar','Calendar — Bikram Sambat','The calendar used in official business; it is not one of the symbols named in Articles 8–9'),('national-currency','Currency — Nepalese rupee','The legal currency, issued by Nepal Rastra Bank; it is not one of the symbols named in Articles 8–9')]
D_EN = [('national-tree','Tree — Peepal','No designated national tree confirmed'),('national-fish','Fish — Asala (Golden Mahseer)','No designated national fish confirmed'),('national-butterfly','Butterfly — Krishna Peacock','Popularly cited; no formal declaration found'),
        ('national-food','Food — Dal Bhat','No Government of Nepal declaration confirmed'),('national-weapon','Weapon — Khukuri','Widely called the national weapon; no official declaration confirmed'),
        ('national-dress','Dress — Daura Suruwal and Gunyu Cholo','Widely regarded as national dress; no declaration confirmed by us'),('national-dance','Dance — Deuda and Maruni','Widely regarded as national dances; no declaration confirmed by us'),
        ('national-monument','Monument — Dharahara','Widely regarded; no designation confirmed'),('national-cave','Cave — Siddha Gufa','Most often named; no law designates a national cave'),
        ('national-museum','Museum — National Museum of Nepal','National by name and function; not a symbol designation'),('national-everest','Highest peak — Sagarmatha (Everest)','Nepal\'s highest peak; no "national mountain" designation')]
OF_EN_BODY = '''    <section>
      <p class="lede">Lists of "national symbols of Nepal" often mix what the law says with what people simply say. This page separates the two for all 23 symbols on this site. <b>Seven symbols, plus the language provisions, are written into the Constitution of Nepal (2015).</b> Two more were declared by the government. The rest are customary.</p>
      <div class="status warn"><b>How to read this page.</b> "Not confirmed" means we could not find a law or government decision, not that none exists. Check the Constitution, the Nepal Gazette or the relevant ministry before citing a symbol as official.</div>
    </section>

    <section id="constitution">
      <h2>1. Named in the Constitution of Nepal (2015)</h2>
      <p>Articles 8 and 9 set out the flag, the anthem, the coat of arms and the national flower, colour, animal and bird. Articles 6 and 7 deal with language.</p>
''' + _table(A_EN, 'Symbol', 'Constitutional basis', 'en') + '''      <div class="callout"><strong>On "national language."</strong> Article 6 says all mother tongues spoken in Nepal are national languages. Nepali in the Devanagari script is the language of official business under Article 7, and provinces may add others. So "the national language" is Nepali only in the official-business sense.</div>
      <p class="source">Source: Constitution of Nepal 2015, text on Constitute Project (Articles 6, 7, 8 and 9).</p>
    </section>

    <section id="government">
      <h2>2. Declared by the Government (outside the Constitution)</h2>
''' + _table(B_EN, 'Symbol', 'Basis', 'en') + '''    </section>

    <section id="official-other">
      <h2>3. Official in use, but not a symbol declaration</h2>
''' + _table(C_EN, 'Item', 'Status', 'en') + '''    </section>

    <section id="customary">
      <h2>4. Customary or widely cited — no declaration confirmed</h2>
      <p>These are real and widely loved parts of Nepali identity. We found no law or government decision naming them as official national symbols.</p>
''' + _table(D_EN, 'Symbol', 'Status', 'en') + '''      <div class="dyk">
        <h3>✦ Why this matters</h3>
        <ul>
          <li>Many websites repeat the same list as if every item were gazetted. Quiz books and school notes often copy it.</li>
          <li>If you need an official answer (an exam, a thesis, a news story), use section 1 and cite the Article.</li>
          <li>Section 4 is not a lesser category for culture: the peepal, the khukuri and dal bhat matter to Nepalis whatever their legal status.</li>
        </ul>
      </div>
    </section>
'''
OF_EN_FAQ = [
 ("Which national symbols of Nepal are in the Constitution?", "The flag (Article 8), the anthem and the coat of arms (Article 9), and the national flower (rhododendron), colour (crimson), animal (cow) and bird (Danphe, the Lophophorus), all in Article 9(3). Articles 6 and 7 cover language."),
 ("Is there an official national tree of Nepal?", "We could not confirm one. The peepal is the tree most often named, but it is not among the symbols listed in the Constitution."),
 ("Is the khukuri officially the national weapon?", "We found no official declaration. It is widely called the national weapon, so we describe it as customary."),
 ("Is Nepali the national language of Nepal?", "Article 6 makes all mother tongues spoken in Nepal national languages. Article 7 makes Nepali in Devanagari the language of official business."),
 ("Is volleyball officially Nepal's national sport?", "Yes. The Government of Nepal declared it on 22 May 2017, according to our sport page. Dandi Biyo and kabaddi are called traditional games but were not declared."),
 ("Is the orange officially Nepal's national fruit?", "A Council of Ministers decision on 12 April 2024 was reported as recognising the orange. We have not seen the decision text, so the exact species is not confirmed."),
 ("Is Mount Everest Nepal's national mountain?", "No national-mountain designation is confirmed. Sagarmatha (Everest) is Nepal's highest peak and the nearest thing to one."),
 ("Why do some websites list a national tree, fish or river as official?", "Many lists copy each other and treat popular choices as declared ones. Check the Constitution, the Nepal Gazette or the ministry concerned before citing one."),
]
def _rows_ne(rows): return rows
A_NE = [('national-flag','झण्डा','धारा ८; बनाउने विधि अनुसूची १ मा'),('national-anthem','राष्ट्रगान','धारा ९(१); पाठ अनुसूची २ मा'),('national-emblem','प्रतीक चिन्ह (राष्ट्रिय चिन्ह)','धारा ९(२); अनुसूची ३'),
        ('national-flower','फूल — लालीगुराँस','धारा ९(३): लालीगुराँस राष्ट्रिय फूल'),('national-color','रङ — गाढा रातो','धारा ९(३): गाढा रातो राष्ट्रिय रङ'),
        ('national-animal','पशु — गाई','धारा ९(३): गाई राष्ट्रिय पशु'),('national-bird','पन्छी — डाँफे','धारा ९(३): डाँफे राष्ट्रिय पन्छी'),
        ('national-language','भाषा','धारा ६: नेपालमा बोलिने सबै मातृभाषा राष्ट्रभाषा हुन्। धारा ७: देवनागरी लिपिमा लेखिने नेपाली भाषा सरकारी कामकाजको भाषा')]
B_NE = [('national-sport','खेल — भलिबल','नेपाल सरकारले २०१७ मे २२ (२०७४ जेठ ८) मा घोषणा गरेको (हाम्रो खेल पृष्ठमा उल्लिखित मन्त्रिपरिषद् निर्णय अनुसार)'),('national-fruit','फल — सुन्तला','२०२४ अप्रिल १२ मा मन्त्रिपरिषद्ले मान्यता दिएको (समाचार प्रतिवेदन; निर्णयको पाठमा कुन प्रजाति उल्लेख छ भन्ने पुष्टि भएको छैन)')]
C_NE = [('national-calendar','पात्रो — बिक्रम सम्वत्','सरकारी कामकाजमा प्रयोग हुने पात्रो; धारा ८–९ मा उल्लेखित चिन्ह होइन'),('national-currency','मुद्रा — नेपाली रुपैयाँ','नेपाल राष्ट्र बैंकले जारी गर्ने वैध मुद्रा; धारा ८–९ मा उल्लेखित चिन्ह होइन')]
D_NE = [('national-tree','रूख — पीपल','तोकिएको राष्ट्रिय रूख पुष्टि भएको छैन'),('national-fish','माछा — असला (गोल्डेन महसिर)','तोकिएको राष्ट्रिय माछा पुष्टि भएको छैन'),('national-butterfly','पुतली — कृष्ण मयूर पुतली','लोकप्रिय रूपमा भनिन्छ; औपचारिक घोषणा भेटिएन'),
        ('national-food','खाना — दालभात','नेपाल सरकारको घोषणा पुष्टि भएको छैन'),('national-weapon','हतियार — खुकुरी','व्यापक रूपमा राष्ट्रिय हतियार भनिन्छ; आधिकारिक घोषणा पुष्टि भएको छैन'),
        ('national-dress','पोशाक — दौरा सुरुवाल र गुन्यू चोलो','राष्ट्रिय पोशाकका रूपमा व्यापक मान्यता; हामीले घोषणा पुष्टि गरेका छैनौँ'),('national-dance','नृत्य — देउडा र मारुनी','राष्ट्रिय नृत्यका रूपमा व्यापक मान्यता; हामीले घोषणा पुष्टि गरेका छैनौँ'),
        ('national-monument','स्मारक — धरहरा','व्यापक मान्यता; तोकिएको पुष्टि भएको छैन'),('national-cave','गुफा — सिद्ध गुफा','प्रायः यही नाम लिइन्छ; राष्ट्रिय गुफा तोक्ने कानुन छैन'),
        ('national-museum','संग्रहालय — राष्ट्रिय संग्रहालय','नाम र कामले राष्ट्रिय; चिन्हका रूपमा तोकिएको होइन'),('national-everest','सर्वोच्च शिखर — सगरमाथा','नेपालको सबैभन्दा अग्लो शिखर; "राष्ट्रिय हिमाल" तोकिएको छैन')]
OF_NE_BODY = '''    <section>
      <p class="lede">"नेपालका राष्ट्रिय चिन्ह" का सूचीमा कानुनले भनेको कुरा र मानिसले सामान्य रूपमा भन्ने कुरा प्रायः मिसिएका हुन्छन्। यो पृष्ठले यस साइटका सबै २३ चिन्हलाई ती दुई वर्गमा छुट्याउँछ। <b>सातवटा चिन्ह र भाषासम्बन्धी व्यवस्था नेपालको संविधान (२०७२) मा लेखिएका छन्।</b> दुईवटा सरकारले घोषणा गरेका हुन्। बाँकी परम्परागत हुन्।</p>
      <div class="status warn"><b>यो पृष्ठ कसरी पढ्ने।</b> "पुष्टि भएको छैन" को अर्थ हामीले कानुन वा सरकारी निर्णय भेटेनौँ भन्ने हो, नभएको भन्ने होइन। कुनै चिन्हलाई आधिकारिक भनेर उद्धृत गर्नुअघि संविधान, नेपाल राजपत्र वा सम्बन्धित मन्त्रालय जाँच्नुहोस्।</div>
    </section>

    <section id="constitution">
      <h2>१. नेपालको संविधान (२०७२) मा उल्लेख भएका</h2>
      <p>धारा ८ र ९ ले झण्डा, राष्ट्रगान, प्रतीक चिन्ह र राष्ट्रिय फूल, रङ, पशु र पन्छी तोकेका छन्। धारा ६ र ७ भाषासँग सम्बन्धित छन्।</p>
''' + _table(A_NE, 'चिन्ह', 'संवैधानिक आधार', 'ne') + '''      <div class="callout"><strong>"राष्ट्रभाषा" बारे।</strong> धारा ६ ले नेपालमा बोलिने सबै मातृभाषालाई राष्ट्रभाषा भनेको छ। धारा ७ अनुसार देवनागरी लिपिमा लेखिने नेपाली भाषा सरकारी कामकाजको भाषा हो, र प्रदेशले अरू भाषा थप्न सक्छन्। त्यसैले "राष्ट्रभाषा नेपाली" भन्नु सरकारी कामकाजको अर्थमा मात्र हो।</div>
      <p class="source">स्रोत: नेपालको संविधान २०७२, Constitute Project मा रहेको पाठ (धारा ६, ७, ८ र ९)।</p>
    </section>

    <section id="government">
      <h2>२. सरकारले घोषणा गरेका (संविधानबाहिर)</h2>
''' + _table(B_NE, 'चिन्ह', 'आधार', 'ne') + '''    </section>

    <section id="official-other">
      <h2>३. आधिकारिक प्रयोगमा, तर चिन्हको घोषणा होइन</h2>
''' + _table(C_NE, 'विषय', 'हैसियत', 'ne') + '''    </section>

    <section id="customary">
      <h2>४. परम्परागत वा व्यापक रूपमा भनिने — घोषणा पुष्टि भएको छैन</h2>
      <p>यी नेपाली पहिचानका साँच्चिकै प्रिय अंश हुन्। यिनलाई आधिकारिक राष्ट्रिय चिन्ह तोक्ने कानुन वा सरकारी निर्णय हामीले भेटेनौँ।</p>
''' + _table(D_NE, 'चिन्ह', 'हैसियत', 'ne') + '''      <div class="dyk">
        <h3>✦ यो किन महत्त्वपूर्ण छ</h3>
        <ul>
          <li>धेरै वेबसाइटले एउटै सूची दोहोर्‍याएर सबै कुरा राजपत्रमा परेको जस्तो देखाउँछन्। प्रश्नोत्तर पुस्तक र विद्यालयका नोटहरूले पनि प्रायः त्यही सार्छन्।</li>
          <li>परीक्षा, शोधपत्र वा समाचारका लागि आधिकारिक उत्तर चाहिए भागसङ्ख्या १ प्रयोग गरी धारा उद्धृत गर्नुहोस्।</li>
          <li>भागसङ्ख्या ४ संस्कृतिका लागि कमजोर वर्ग होइन: पीपल, खुकुरी र दालभात कानुनी हैसियत जे भए पनि नेपालीका लागि महत्त्वपूर्ण छन्।</li>
        </ul>
      </div>
    </section>
'''
OF_NE_FAQ = [
 ("नेपालका कुन राष्ट्रिय चिन्ह संविधानमा छन्?", "झण्डा (धारा ८), राष्ट्रगान र प्रतीक चिन्ह (धारा ९), तथा राष्ट्रिय फूल (लालीगुराँस), रङ (गाढा रातो), पशु (गाई) र पन्छी (डाँफे) धारा ९(३) मा। भाषा धारा ६ र ७ मा।"),
 ("नेपालको आधिकारिक राष्ट्रिय रूख छ?", "हामीले पुष्टि गर्न सकेनौँ। पीपल प्रायः नाम लिइने रूख हो, तर संविधानमा उल्लेखित चिन्हमा पर्दैन।"),
 ("खुकुरी आधिकारिक रूपमा राष्ट्रिय हतियार हो?", "हामीले आधिकारिक घोषणा भेटेनौँ। यसलाई व्यापक रूपमा राष्ट्रिय हतियार भनिन्छ, त्यसैले परम्परागत भनेर वर्णन गरेका छौँ।"),
 ("नेपाली नेपालको राष्ट्रभाषा हो?", "धारा ६ ले नेपालमा बोलिने सबै मातृभाषालाई राष्ट्रभाषा बनाएको छ। धारा ७ ले देवनागरी लिपिमा लेखिने नेपालीलाई सरकारी कामकाजको भाषा बनाएको छ।"),
 ("भलिबल आधिकारिक रूपमा नेपालको राष्ट्रिय खेल हो?", "हो। हाम्रो खेल पृष्ठ अनुसार नेपाल सरकारले २०१७ मे २२ मा घोषणा गरेको हो। दण्डीबियो र कबड्डीलाई परम्परागत खेल भनिन्छ तर घोषणा भएको छैन।"),
 ("सुन्तला आधिकारिक रूपमा नेपालको राष्ट्रिय फल हो?", "२०२४ अप्रिल १२ को मन्त्रिपरिषद् निर्णयले सुन्तलालाई मान्यता दिएको भनी रिपोर्ट भएको छ। हामीले निर्णयको पाठ देखेका छैनौँ, त्यसैले ठ्याक्कै कुन प्रजाति हो भन्ने पुष्टि भएको छैन।"),
 ("सगरमाथा नेपालको राष्ट्रिय हिमाल हो?", "राष्ट्रिय हिमाल तोकिएको पुष्टि भएको छैन। सगरमाथा नेपालको सबैभन्दा अग्लो शिखर र त्यसको सबैभन्दा नजिकको कुरा हो।"),
 ("केही वेबसाइटले राष्ट्रिय रूख, माछा वा नदीलाई आधिकारिक किन भन्छन्?", "धेरै सूचीले एकअर्काको नक्कल गरी लोकप्रिय छनोटलाई घोषित भनिदिन्छन्। उद्धृत गर्नुअघि संविधान, नेपाल राजपत्र वा सम्बन्धित मन्त्रालय जाँच्नुहोस्।"),
]
REL_OF = [('national-flag', 'National Flag'), ('national-animal', 'Cow — National Animal'), ('national-sport', 'Volleyball — National Sport'), ('national-tree', 'Peepal — National Tree')]
REL_OF_NE = [('national-flag', 'राष्ट्रिय झण्डा'), ('national-animal', 'गाई — राष्ट्रिय पशु'), ('national-sport', 'भलिबल — राष्ट्रिय खेल'), ('national-tree', 'पीपल — राष्ट्रिय रूख')]
EXTRA_PAGES = EXTRA_PAGES + [
 dict(slug='official-vs-unofficial', photo='official_vs_unofficial.webp', noitemlist=True, about_name='National symbols of Nepal', about_sameas='https://en.wikipedia.org/wiki/National_symbols_of_Nepal',
  en=dict(title='Official vs Unofficial National Symbols of Nepal — What the Law Says',
    desc='Which of Nepal\'s national symbols are in the Constitution (Articles 6–9), which were declared by the government, and which are only customary. All 23 symbols checked.',
    og_title='Official vs Unofficial National Symbols of Nepal', og_desc='Flag, anthem, emblem, flower, colour, animal and bird are in the Constitution. See which others are declared, official in use, or just customary.',
    ld_desc='A fact-check of all 23 national symbols of Nepal: which are named in the Constitution of Nepal 2015, which were declared by the government, and which are customary.',
    itemlist_desc='', crumb='Official vs Unofficial',
    img_alt='Illustration of a scale weighing a Constitution book against a flower, tree and khukuri', img_caption='Official or customary? Original illustration.',
    eyebrow='Fact-check — National Symbols of Nepal', h1='Official or Customary? <em>The Law vs the Lists</em>',
    hero='<strong>Seven symbols and the language rules are named in the Constitution of Nepal (2015).</strong> Two more were declared by the government, and eleven are customary or widely cited without a confirmed declaration.',
    tags=['Constitution: 7 symbols + language', 'Government decisions: 2', 'Customary: 11', 'Checked: 13 Nov 2026'],
    caption='Original illustration — not a photograph.',
    facts=[('In the Constitution', 'Flag, anthem, emblem, flower, colour, animal, bird', False), ('Language', 'Articles 6 and 7', False), ('Government decisions', 'Volleyball (2017), orange (2024)', False), ('Official in use', 'Calendar, currency', False), ('Customary', '11 symbols', False), ('Checked', '13 November 2026', False)],
    pron=('आधिकारिक', 'Adhikarik', 'ah-dhee-KAA-rik'), body=OF_EN_BODY, faq=OF_EN_FAQ,
    related=rel('en', REL_OF) + [(S + '/', 'All national symbols of Nepal →')], related_p='Read the full guide for any symbol, and see which are written into the law.'),
  ne=dict(title='नेपालका आधिकारिक र अनौपचारिक राष्ट्रिय चिन्ह — कानुनले के भन्छ',
    desc='नेपालका कुन राष्ट्रिय चिन्ह संविधान (धारा ६–९) मा छन्, कुन सरकारले घोषणा गरेको हो र कुन परम्परागत मात्र हुन्। सबै २३ चिन्ह जाँचिएको।',
    og_title='नेपालका आधिकारिक र अनौपचारिक राष्ट्रिय चिन्ह', og_desc='झण्डा, राष्ट्रगान, चिन्ह, फूल, रङ, पशु र पन्छी संविधानमा छन्। अरू कुन घोषित, आधिकारिक प्रयोगमा वा परम्परागत हुन् हेर्नुहोस्।',
    ld_desc='नेपालका सबै २३ राष्ट्रिय चिन्हको तथ्य जाँच: कुन नेपालको संविधान २०७२ मा उल्लेख छन्, कुन सरकारले घोषणा गरेको हो र कुन परम्परागत हुन्।',
    itemlist_desc='', crumb='आधिकारिक कि परम्परागत',
    img_alt='संविधानको पुस्तकलाई फूल, रूख र खुकुरीसँग तौलिरहेको तराजुको चित्रण', img_caption='आधिकारिक कि परम्परागत? मौलिक चित्रण।',
    eyebrow='तथ्य जाँच — नेपालका राष्ट्रिय चिन्ह', h1='आधिकारिक कि परम्परागत? <em>कानुन बनाम सूची</em>',
    hero='<strong>सातवटा चिन्ह र भाषासम्बन्धी नियम नेपालको संविधान (२०७२) मा उल्लेख छन्।</strong> दुईवटा थप सरकारले घोषणा गरेका हुन्, र एघारवटा घोषणा पुष्टि नभएका परम्परागत वा व्यापक रूपमा भनिने हुन्।',
    tags=['संविधान: ७ चिन्ह + भाषा', 'सरकारी निर्णय: २', 'परम्परागत: ११', 'जाँच: २०२६ नोभेम्बर १३'],
    caption='मौलिक चित्रण — तस्बिर होइन।',
    facts=[('संविधानमा', 'झण्डा, राष्ट्रगान, चिन्ह, फूल, रङ, पशु, पन्छी', False), ('भाषा', 'धारा ६ र ७', False), ('सरकारी निर्णय', 'भलिबल (२०१७), सुन्तला (२०२४)', False), ('आधिकारिक प्रयोगमा', 'पात्रो, मुद्रा', False), ('परम्परागत', '११ चिन्ह', False), ('जाँच मिति', '२०२६ नोभेम्बर १३', False)],
    pron=('आधिकारिक', 'Adhikarik', 'आधिकारिक'), body=OF_NE_BODY, faq=OF_NE_FAQ,
    related=rel('ne', REL_OF_NE) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p='कुनै पनि चिन्हको पूरा गाइड पढ्नुहोस् र कुन कानुनमा लेखिएका छन् हेर्नुहोस्।'),
 ),
]
