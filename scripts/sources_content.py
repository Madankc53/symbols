# -*- coding: utf-8 -*-
# /sources/ and /ne/sources/. Lists what each guide actually cites (taken from the 'Source:' lines on the pages)
# and how strong that source is. Only links we have used on the site are hyperlinked.
CONST = '<a href="https://www.constituteproject.org/constitution/Nepal_2015" rel="noopener">Constitution of Nepal 2015 (Constitute Project)</a>'
def _tbl(rows, h):
    r = ''.join('            <tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td></tr>\n' % x for x in rows)
    return '      <div class="table-wrap">\n        <table>\n          <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n          <tbody>\n%s          </tbody>\n        </table>\n      </div>\n' % (h[0], h[1], h[2], r)
# (href, symbol, cited on the guide, strength)
EN_ROWS = [
 ('/national-flag/', 'Flag', 'Constitution of Nepal, Article 8 and Schedule 1; Wikipedia, "Flag of Nepal"', 'Primary (law)'),
 ('/national-anthem/', 'Anthem', 'Constitution, Article 9(1) and Schedule 2; Nepal Law Commission; Wikipedia, "Sayaun Thunga Phulka"', 'Primary + secondary'),
 ('/national-emblem/', 'Emblem', 'Constitution, Article 9(2) and Schedule 3; Wikipedia, "Emblem of Nepal"; heraldry-wiki.com', 'Primary + secondary'),
 ('/national-flower/', 'Flower', 'Constitution, Article 9(3); Department of Forests and Soil Conservation; Department of Plant Resources; IUCN Red List', 'Primary + government + IUCN'),
 ('/national-color/', 'Colour', 'Constitution, Article 9(3) and Schedule 1; Wikipedia, "Flag of Nepal"', 'Primary (law)'),
 ('/national-animal/', 'Animal', 'Constitution, Article 9(3); Kathmandu Post (2019); Global Voices (2017)', 'Primary + news'),
 ('/national-bird/', 'Bird', 'Constitution, Article 9(3); Department of National Parks and Wildlife Conservation; IUCN Red List', 'Primary + government + IUCN'),
 ('/national-language/', 'Language', 'Constitution, Articles 6 and 7; Language Commission of Nepal (6 September 2021), as reported by Online Khabar and Radio Nepal', 'Primary + news'),
 ('/national-sport/', 'Sport', 'Cabinet decision of 22 May 2017 as reported by Onlinekhabar; Ministry of Youth and Sports', 'News report of a government decision'),
 ('/national-fruit/', 'Fruit', 'Rising Nepal, "Orange declared as national fruit" (12 April 2024); Nepal Horticulture Society; Kathmandu Post', 'News report; decision text not seen'),
 ('/national-calendar/', 'Calendar', 'Wikipedia, "Vikram Samvat" and "Nepal Sambat"; historical records', 'Secondary'),
 ('/national-currency/', 'Currency', 'Nepal Rastra Bank', 'Primary (issuer)'),
 ('/national-tree/', 'Tree', 'Department of Forests and Soil Conservation; IUCN', 'Government + IUCN; no official designation found'),
 ('/national-fish/', 'Fish', 'NARC; FAO Nepal fisheries profile; Department of Fisheries; IUCN Red List; Himalayan Times (Jan 2026); Kathmandu Post (2017)', 'Mixed; no official designation found'),
 ('/national-butterfly/', 'Butterfly', 'Inside Himalayas; Butterflies of Nepal research community; IUCN Red Data Book as summarised on Wikipedia', 'Secondary; no official designation found'),
 ('/national-food/', 'Food', 'Wikipedia, "Nepalese cuisine" and "Dal bhat"; no government source found', 'Secondary; no official designation found'),
 ('/national-weapon/', 'Weapon', 'Wikipedia, "Kukri" (which cites the Gurkha Brigade Association); Gurkha Brigade Association, "The Kukuri"', 'Secondary; no official designation found'),
 ('/national-dress/', 'Dress', 'No source lines yet — being added', 'To be improved'),
 ('/national-dance/', 'Dance', 'Wikipedia, "Dance in Nepal" and "Maruni"; ImNepal.com; Native Nepali Stage; OnlineKhabar; Kathmandu Post', 'Secondary; no official designation found'),
 ('/national-monument/', 'Monument', 'Government of Nepal earthquake reconstruction records; Kathmandu Metropolitan City', 'Government records (no designation found)'),
 ('/national-everest/', 'Highest peak', 'UNESCO World Heritage Centre; Montana State University Everest expedition; Alan Arnette; Ace the Himalaya', 'Mixed secondary'),
 ('/national-cave/', 'Cave', 'Lonely Planet; Wikipedia ("Siddha Cave", "Mustang Caves"); Nepal Tourism Board; Mountain Tiger Nepal; showcaves.com', 'Tourism and secondary; no designation found'),
 ('/national-museum/', 'Museum', 'Wikipedia, "National Museum of Nepal"; Department of Archaeology', 'Secondary + government'),
]
EN_BODY = '''    <section>
      <p class="lede">This page lists what each guide on this site actually cites, and how strong that source is. Nepal's national symbols are set partly by law and partly by custom, so the strength of the source changes what we can say.</p>
    </section>

    <section id="method">
      <h2>How We Rate Sources</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Level</th><th>What it is</th><th>What we do with it</th></tr></thead>
          <tbody>
            <tr><td><b>Primary</b></td><td>The Constitution, Nepal Gazette notices, a ministry or the issuing institution</td><td>State the fact and cite the Article or document where possible</td></tr>
            <tr><td><b>News report</b></td><td>A newspaper report of a government decision</td><td>State the decision, name the report and flag anything we could not confirm</td></tr>
            <tr><td><b>Secondary</b></td><td>Encyclopaedias, books, tourism boards, specialist sites</td><td>Use for background, not for "official" claims</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout"><strong>Our rule.</strong> We call a symbol "official" only when we have seen the law or a report of the government decision. Otherwise we say "no official declaration confirmed". The full breakdown is on the <a href="/official-vs-unofficial/">Official vs Unofficial</a> page.</div>
    </section>

    <section id="primary">
      <h2>The Main Legal Source</h2>
      <p>The <b>Constitution of Nepal (2015)</b> names the flag (Article 8), anthem and coat of arms (Article 9(1) and (2)), and the national flower, colour, animal and bird (Article 9(3)). Articles 6 and 7 cover language. Read it at: ''' + CONST + '''.</p>
      <p>Before citing a symbol as official in an exam, thesis or news story, check the Constitution, the Nepal Gazette or the ministry concerned. This site is educational and is not a substitute for them.</p>
    </section>

    <section id="by-symbol">
      <h2>Sources by Guide</h2>
''' + _tbl(EN_ROWS, ('Guide', 'Cited on the guide', 'Strength')) + '''      <p class="source">Compiled 13 November 2026 from the "Source" lines on each guide. Several guides name an institution or publication without a specific document; we are replacing those with exact citations over time.</p>
    </section>

    <section id="corrections">
      <h2>Spotted a Mistake?</h2>
      <p>If a fact is wrong or a better source exists, please tell us through the <a href="https://thenepal.io/contact/">contact page</a> with the page address and the source. We correct errors and update the "checked" dates on the guides.</p>
    </section>
'''
EN_FAQ = [
 ("Where does symbols.thenepal.io get its information?", "From the Constitution of Nepal where a symbol is named in law, from reports of government decisions, and from secondary sources such as encyclopaedias and specialist sites. Each guide lists its sources, and this page summarises them."),
 ("Which source is best for official national symbols?", "The Constitution of Nepal (2015), Articles 6 to 9, together with the Nepal Gazette and the relevant ministry. Use those when you need an official citation."),
 ("Why do some guides say 'no official declaration confirmed'?", "Because we could not find a law or government decision for them. It means unconfirmed, not that none exists."),
 ("How do I report an error or suggest a source?", "Use the contact page on thenepal.io and include the page address and the source."),
]
def _tbl_ne(rows, h):
    r = ''.join('            <tr><td><a href="/ne%s">%s</a></td><td>%s</td><td>%s</td></tr>\n' % (a, b, c, d) for a, b, c, d in rows)
    return '      <div class="table-wrap">\n        <table>\n          <thead><tr><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n          <tbody>\n%s          </tbody>\n        </table>\n      </div>\n' % (h[0], h[1], h[2], r)
NE_ROWS = [
 ('/national-flag/', 'झण्डा', 'संविधान, धारा ८ र अनुसूची १; Wikipedia, "Flag of Nepal"', 'प्राथमिक (कानुन)'),
 ('/national-anthem/', 'राष्ट्रगान', 'संविधान, धारा ९(१) र अनुसूची २; नेपाल कानुन आयोग; Wikipedia', 'प्राथमिक + द्वितीयक'),
 ('/national-emblem/', 'प्रतीक चिन्ह', 'संविधान, धारा ९(२) र अनुसूची ३; Wikipedia; heraldry-wiki.com', 'प्राथमिक + द्वितीयक'),
 ('/national-flower/', 'फूल', 'संविधान, धारा ९(३); वन तथा भू-संरक्षण विभाग; वनस्पति विभाग; IUCN', 'प्राथमिक + सरकारी + IUCN'),
 ('/national-color/', 'रङ', 'संविधान, धारा ९(३) र अनुसूची १; Wikipedia, "Flag of Nepal"', 'प्राथमिक (कानुन)'),
 ('/national-animal/', 'पशु', 'संविधान, धारा ९(३); काठमाडौँ पोस्ट (२०१९); Global Voices (२०१७)', 'प्राथमिक + समाचार'),
 ('/national-bird/', 'पन्छी', 'संविधान, धारा ९(३); राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभाग; IUCN', 'प्राथमिक + सरकारी + IUCN'),
 ('/national-language/', 'भाषा', 'संविधान, धारा ६ र ७; भाषा आयोग (२०२१ सेप्टेम्बर ६), अनलाइनखबर र रेडियो नेपालमा रिपोर्ट भएअनुसार', 'प्राथमिक + समाचार'),
 ('/national-sport/', 'खेल', '२०१७ मे २२ को मन्त्रिपरिषद् निर्णय (अनलाइनखबरको रिपोर्ट); युवा तथा खेलकुद मन्त्रालय', 'सरकारी निर्णयको समाचार'),
 ('/national-fruit/', 'फल', 'द राइजिङ नेपाल (२०२४ अप्रिल १२); नेपाल हर्टिकल्चर सोसाइटी; काठमाडौँ पोस्ट', 'समाचार; निर्णयको पाठ नदेखिएको'),
 ('/national-calendar/', 'पात्रो', 'Wikipedia, "Vikram Samvat" र "Nepal Sambat"; ऐतिहासिक अभिलेख', 'द्वितीयक'),
 ('/national-currency/', 'मुद्रा', 'नेपाल राष्ट्र बैंक', 'प्राथमिक (जारीकर्ता)'),
 ('/national-tree/', 'रूख', 'वन तथा भू-संरक्षण विभाग; IUCN', 'सरकारी + IUCN; आधिकारिक तोकिएको भेटिएन'),
 ('/national-fish/', 'माछा', 'NARC; FAO नेपाल; मत्स्य विकास विभाग; IUCN; हिमालयन टाइम्स (२०२६ जनवरी); काठमाडौँ पोस्ट (२०१७)', 'मिश्रित; आधिकारिक तोकिएको भेटिएन'),
 ('/national-butterfly/', 'पुतली', 'Inside Himalayas; नेपालका पुतली अनुसन्धान समुदाय; IUCN Red Data Book (Wikipedia मार्फत)', 'द्वितीयक; आधिकारिक तोकिएको भेटिएन'),
 ('/national-food/', 'खाना', 'Wikipedia, "Nepalese cuisine" र "Dal bhat"; सरकारी स्रोत भेटिएन', 'द्वितीयक; आधिकारिक तोकिएको भेटिएन'),
 ('/national-weapon/', 'हतियार', 'Wikipedia, "Kukri" (जसले गोर्खा ब्रिगेड एसोसिएसन उद्धृत गर्छ); Gurkha Brigade Association, "The Kukuri"', 'द्वितीयक; आधिकारिक तोकिएको भेटिएन'),
 ('/national-dress/', 'पोशाक', 'स्रोत लाइन अहिलेसम्म छैन — थपिँदै', 'सुधार गर्न बाँकी'),
 ('/national-dance/', 'नृत्य', 'Wikipedia, "Dance in Nepal" र "Maruni"; ImNepal.com; Native Nepali Stage; अनलाइनखबर; काठमाडौँ पोस्ट', 'द्वितीयक; आधिकारिक तोकिएको भेटिएन'),
 ('/national-monument/', 'स्मारक', 'नेपाल सरकारको भूकम्प पुनर्निर्माण अभिलेख; काठमाडौँ महानगरपालिका', 'सरकारी अभिलेख (तोकिएको भेटिएन)'),
 ('/national-everest/', 'सर्वोच्च शिखर', 'UNESCO विश्व सम्पदा केन्द्र; Montana State University; Alan Arnette; Ace the Himalaya', 'मिश्रित द्वितीयक'),
 ('/national-cave/', 'गुफा', 'Lonely Planet; Wikipedia; नेपाल पर्यटन बोर्ड; Mountain Tiger Nepal; showcaves.com', 'पर्यटन र द्वितीयक; तोकिएको भेटिएन'),
 ('/national-museum/', 'संग्रहालय', 'Wikipedia, "National Museum of Nepal"; पुरातत्त्व विभाग', 'द्वितीयक + सरकारी'),
]
NE_BODY = '''    <section>
      <p class="lede">यो पृष्ठमा यस साइटका हरेक गाइडले वास्तवमा के उद्धृत गर्छ र त्यो स्रोत कति बलियो छ भन्ने देखाइएको छ। नेपालका राष्ट्रिय चिन्ह केही कानुनले र केही परम्पराले तोकेका हुन्, त्यसैले स्रोतको बल अनुसार हामी के भन्न सक्छौँ फरक पर्छ।</p>
    </section>

    <section id="method">
      <h2>स्रोत कसरी मूल्याङ्कन गर्छौँ</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>तह</th><th>के हो</th><th>हामी के गर्छौँ</th></tr></thead>
          <tbody>
            <tr><td><b>प्राथमिक</b></td><td>संविधान, नेपाल राजपत्र, मन्त्रालय वा जारी गर्ने संस्था</td><td>तथ्य लेख्छौँ र सम्भव भए धारा वा कागजात उद्धृत गर्छौँ</td></tr>
            <tr><td><b>समाचार</b></td><td>सरकारी निर्णयबारे समाचार पत्रिकाको रिपोर्ट</td><td>निर्णय लेख्छौँ, रिपोर्टको नाम दिन्छौँ र पुष्टि गर्न नसकेको कुरा चिह्नित गर्छौँ</td></tr>
            <tr><td><b>द्वितीयक</b></td><td>विश्वकोश, पुस्तक, पर्यटन बोर्ड, विशेष साइट</td><td>पृष्ठभूमिका लागि प्रयोग गर्छौँ, "आधिकारिक" दाबीका लागि होइन</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout"><strong>हाम्रो नियम।</strong> कानुन वा सरकारी निर्णयको रिपोर्ट देखेपछि मात्र हामी कुनै चिन्हलाई "आधिकारिक" भन्छौँ। अन्यथा "आधिकारिक घोषणा पुष्टि भएको छैन" भन्छौँ। पूरा विवरण <a href="/ne/official-vs-unofficial/">आधिकारिक कि परम्परागत</a> पृष्ठमा छ।</div>
    </section>

    <section id="primary">
      <h2>मुख्य कानुनी स्रोत</h2>
      <p><b>नेपालको संविधान (२०७२)</b> ले झण्डा (धारा ८), राष्ट्रगान र प्रतीक चिन्ह (धारा ९(१) र (२)), तथा राष्ट्रिय फूल, रङ, पशु र पन्छी (धारा ९(३)) तोकेको छ। धारा ६ र ७ भाषासँग सम्बन्धित छन्। यहाँ पढ्नुहोस्: ''' + CONST + '''।</p>
      <p>परीक्षा, शोधपत्र वा समाचारमा कुनै चिन्हलाई आधिकारिक भनेर उद्धृत गर्नुअघि संविधान, नेपाल राजपत्र वा सम्बन्धित मन्त्रालय जाँच्नुहोस्। यो साइट शैक्षिक हो र ती स्रोतको विकल्प होइन।</p>
    </section>

    <section id="by-symbol">
      <h2>गाइडअनुसार स्रोत</h2>
''' + _tbl_ne(NE_ROWS, ('गाइड', 'गाइडमा उद्धृत', 'बल')) + '''      <p class="source">हरेक गाइडका "स्रोत" लाइनबाट २०२६ नोभेम्बर १३ मा संकलित। केही गाइडले ठ्याक्कै कागजात नदिई संस्था वा प्रकाशनको नाम मात्र दिएका छन्; ती क्रमशः सही उद्धरणले बदल्दैछौँ।</p>
    </section>

    <section id="corrections">
      <h2>गल्ती भेट्नुभयो?</h2>
      <p>कुनै तथ्य गलत छ वा राम्रो स्रोत छ भने पृष्ठको ठेगाना र स्रोतसहित <a href="https://thenepal.io/contact/">सम्पर्क पृष्ठ</a> मार्फत हामीलाई जानकारी दिनुहोस्। हामी गल्ती सच्याउँछौँ र गाइडका "जाँचिएको" मिति अद्यावधिक गर्छौँ।</p>
    </section>
'''
NE_FAQ = [
 ("symbols.thenepal.io ले जानकारी कहाँबाट लिन्छ?", "कानुनमा तोकिएको चिन्हका लागि नेपालको संविधानबाट, सरकारी निर्णयका रिपोर्टबाट, र विश्वकोश तथा विशेष साइटजस्ता द्वितीयक स्रोतबाट। हरेक गाइडले आफ्ना स्रोत सूचीबद्ध गर्छ र यो पृष्ठले ती सारांश गर्छ।"),
 ("आधिकारिक राष्ट्रिय चिन्हका लागि सबैभन्दा राम्रो स्रोत कुन हो?", "नेपालको संविधान (२०७२) को धारा ६ देखि ९, नेपाल राजपत्र र सम्बन्धित मन्त्रालय। आधिकारिक उद्धरण चाहिँदा ती प्रयोग गर्नुहोस्।"),
 ("केही गाइडमा 'आधिकारिक घोषणा पुष्टि भएको छैन' किन लेखिएको छ?", "किनभने हामीले ती चिन्हका लागि कानुन वा सरकारी निर्णय भेटेनौँ। यसको अर्थ पुष्टि भएको छैन भन्ने हो, नभएको भन्ने होइन।"),
 ("गल्ती कसरी जानकारी दिने वा स्रोत सुझाउने?", "thenepal.io को सम्पर्क पृष्ठ प्रयोग गर्नुहोस् र पृष्ठको ठेगाना तथा स्रोत लेख्नुहोस्।"),
]
REL_S = [('official-vs-unofficial', 'Official vs Unofficial Symbols'), ('quiz', 'Nepal Symbols Quiz'), ('national-flag', 'National Flag'), ('national-calendar', 'National Calendar')]
REL_S_NE = [('official-vs-unofficial', 'आधिकारिक कि परम्परागत'), ('quiz', 'नेपाल चिन्ह क्विज'), ('national-flag', 'राष्ट्रिय झण्डा'), ('national-calendar', 'राष्ट्रिय पात्रो')]
EXTRA_PAGES = EXTRA_PAGES + [
 dict(slug='sources', photo='nepal_symbols_quiz.webp', noitemlist=True, about_name='National symbols of Nepal', about_sameas='https://en.wikipedia.org/wiki/National_symbols_of_Nepal',
  en=dict(title='Sources & Methodology — How symbols.thenepal.io Checks Its Facts',
    desc='What each guide on symbols.thenepal.io cites and how strong the source is: the Constitution of Nepal, news reports of government decisions, and secondary references.',
    og_title='Sources & Methodology — Nepal National Symbols', og_desc='See the sources behind every Nepal national symbol guide, how we rate them, and how to report a correction.',
    ld_desc='The sources and methodology behind the national symbols guides: what each cites, how source strength is rated, and how to report errors.', itemlist_desc='', crumb='Sources',
    img_alt='A gold trophy, a crimson pennant and question marks (illustration)', img_caption='Original illustration.',
    eyebrow='Sources & Methodology', h1='Where Our Facts <em>Come From</em>',
    hero='<strong>Every guide lists its sources; this page puts them in one place and rates how strong each one is.</strong> The Constitution of Nepal is the main legal source for official symbols.',
    tags=['23 guides', 'Constitution first', 'Corrections welcome'], caption='Original illustration — not a photograph.',
    facts=[('Legal source', 'Constitution of Nepal 2015', False), ('Articles', '6, 7, 8 and 9', False), ('Rated', '23 guides', False), ('Compiled', '13 November 2026', False), ('Corrections', 'Via thenepal.io contact', False), ('Rule', '"Official" only when confirmed', False)],
    pron=('स्रोत', 'Srot', 'sro-t'), body=EN_BODY, faq=EN_FAQ, related=rel('en', REL_S) + [(S + '/', 'All national symbols of Nepal →')], related_p='Read how the facts are checked, then test yourself.'),
  ne=dict(title='स्रोत र कार्यविधि — symbols.thenepal.io ले तथ्य कसरी जाँच्छ',
    desc='symbols.thenepal.io का हरेक गाइडले के उद्धृत गर्छ र स्रोत कति बलियो छ: नेपालको संविधान, सरकारी निर्णयका समाचार र द्वितीयक सन्दर्भ।',
    og_title='स्रोत र कार्यविधि — नेपालका राष्ट्रिय चिन्ह', og_desc='हरेक राष्ट्रिय चिन्ह गाइडको स्रोत, हामी कसरी मूल्याङ्कन गर्छौँ र सच्याउन कसरी जानकारी दिने भन्ने हेर्नुहोस्।',
    ld_desc='राष्ट्रिय चिन्ह गाइडहरूका स्रोत र कार्यविधि: हरेकले के उद्धृत गर्छ, स्रोतको बल कसरी मापन हुन्छ र गल्ती कसरी जानकारी दिने।', itemlist_desc='', crumb='स्रोतहरू',
    img_alt='सुनौलो ट्रफी, गाढा रातो पताका र प्रश्नचिह्न (चित्रण)', img_caption='मौलिक चित्रण।',
    eyebrow='स्रोत र कार्यविधि', h1='हाम्रा तथ्य <em>कहाँबाट आउँछन्</em>',
    hero='<strong>हरेक गाइडले आफ्ना स्रोत सूचीबद्ध गर्छ; यो पृष्ठले ती एकै ठाउँमा राखी स्रोत कति बलियो छ भनी देखाउँछ।</strong> आधिकारिक चिन्हका लागि नेपालको संविधान मुख्य कानुनी स्रोत हो।',
    tags=['२३ गाइड', 'पहिले संविधान', 'सुधार स्वागतयोग्य'], caption='मौलिक चित्रण — तस्बिर होइन।',
    facts=[('कानुनी स्रोत', 'नेपालको संविधान २०७२', False), ('धाराहरू', '६, ७, ८ र ९', False), ('मूल्याङ्कन', '२३ गाइड', False), ('संकलन', '२०२६ नोभेम्बर १३', False), ('सुधार', 'thenepal.io सम्पर्क मार्फत', False), ('नियम', 'पुष्टि भएपछि मात्र "आधिकारिक"', False)],
    pron=('स्रोत', 'Srot', 'स्रोत'), body=NE_BODY, faq=NE_FAQ, related=rel('ne', REL_S_NE) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p='तथ्य कसरी जाँचिन्छ पढ्नुहोस्, अनि आफूलाई जाँच्नुहोस्।'),
 ),
]
