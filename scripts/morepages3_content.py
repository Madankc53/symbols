# -*- coding: utf-8 -*-
# Pages: /nepal-rhino-count/, /nepal-snow-leopard-population/, /nepal-wildlife-population/ (EN + NE). Uses _mk/_en/_ne/fig from earlier content files.
# Sources: Kathmandu Post 23 Sep 2026 (rhino census redesign; 2021: Chitwan 694, Bardiya 38, Shuklaphanta 17, Parsa 3, total 752);
#  Save the Rhino (2015: 645; 2021: 752, +107, 136 calves; 161 deaths 2015-2021, 6 poached); Mongabay 2025 (census cancelled 2025 over funding; every five years; method debate; IUCN Vulnerable);
#  eKantipur 17 Apr 2026 (delays: budget, equipment, technical discussions; was scheduled 2081 BS); Nepali Times 25 Apr 2025 + Down To Earth (397 snow leopards, 1.56 per 100 km2, seven study regions,
#  2015-2024, camera traps + scat genetics, DNPWC + DoFSC, WWF statement, India 718 Jan 2024); WWF (Kangchenjunga telemetry, threats); IUCN/Kathmandu Post (tigers 429).
REL_RH = [('nepal-tiger-census-2026', 'Tiger Census 2026'), ('national-parks-of-nepal', 'National Parks of Nepal'), ('nepal-wildlife-population', 'Wildlife Counts of Nepal'), ('national-animal', 'National Animal')]
REL_RH_NE = [('nepal-tiger-census-2026', 'बाघ गणना २०२६'), ('national-parks-of-nepal', 'नेपालका राष्ट्रिय निकुञ्ज'), ('nepal-wildlife-population', 'नेपालका वन्यजन्तुको सङ्ख्या'), ('national-animal', 'राष्ट्रिय पशु')]
REL_SL = [('national-parks-of-nepal', 'National Parks of Nepal'), ('nepal-wildlife-population', 'Wildlife Counts of Nepal'), ('national-everest', 'Mount Everest'), ('national-animal', 'National Animal')]
REL_SL_NE = [('national-parks-of-nepal', 'नेपालका राष्ट्रिय निकुञ्ज'), ('nepal-wildlife-population', 'नेपालका वन्यजन्तुको सङ्ख्या'), ('national-everest', 'सगरमाथा'), ('national-animal', 'राष्ट्रिय पशु')]
REL_WP = [('nepal-tiger-census-2026', 'Tiger Census 2026'), ('nepal-rhino-count', 'Rhino Count'), ('nepal-snow-leopard-population', 'Snow Leopard Population'), ('national-parks-of-nepal', 'National Parks of Nepal')]
REL_WP_NE = [('nepal-tiger-census-2026', 'बाघ गणना २०२६'), ('nepal-rhino-count', 'गैँडा गणना'), ('nepal-snow-leopard-population', 'हिउँचितुवाको सङ्ख्या'), ('national-parks-of-nepal', 'नेपालका राष्ट्रिय निकुञ्ज')]

RH_EN_BODY = '''    <section>
      <p class="lede"><strong>Nepal has 752 greater one-horned rhinoceroses</strong> according to the latest census, held in March 2021. The department still cites that figure. A new census has been delayed and its method is being redesigned.</p>
    </section>

    <section id="count">
      <h2>Rhino Count by Park (2021)</h2>
      ''' + fig('nepal_rhino_count_chart', 'Bar chart of Nepal rhinos by park in 2021: Chitwan 694, Bardiya 38, Shuklaphanta 17, Parsa 3', 'Rhinos by park in the 2021 census. Chitwan holds about 92 percent.', h=470) + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>Park</th><th>Rhinos (2021)</th></tr></thead>
          <tbody>
            <tr><td>Chitwan National Park</td><td>694</td></tr>
            <tr><td>Bardiya National Park</td><td>38</td></tr>
            <tr><td>Shuklaphanta National Park</td><td>17</td></tr>
            <tr><td>Parsa National Park</td><td>3</td></tr>
            <tr><td><strong>Total</strong></td><td><strong>752</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: The Kathmandu Post, "Nepal's rhino census is getting a scientific makeover" (23 September 2026).</p>
    </section>

    <section id="trend">
      <h2>How the Rhino Population Has Changed</h2>
      <p>The 2015 census counted 645 rhinos. The March 2021 census counted 752, an increase of 107, and included 136 calves. Save the Rhino reports that 161 rhinos died between 2015 and 2021, six of them killed by poachers. Mongabay reports that growth slowed from about 5 to 6 percent a year in 2011-2018 to about 3 percent a year in 2018-2021.</p>
      <p class="source">Source: Save the Rhino; Mongabay (May 2025).</p>
    </section>

    <section id="next">
      <h2>Why There Is No New Rhino Census Yet</h2>
      <p>Nepal counts rhinos about every five years, and the last count was in 2021. A census scheduled for 2081 BS was delayed because of budget problems, equipment shortages and technical discussions, according to eKantipur. Mongabay reported in 2025 that a funding shortfall after USAID support was withdrawn halted it, at an estimated cost of 115,000 to 155,000 US dollars.</p>
      <p>The department is now looking at a new method. The current one uses trained elephants to carry teams through the grassland, which is dangerous: in 2021 a technician was injured when a wild elephant charged a survey elephant. Options under study include dung DNA analysis, camera traps and a mix of both. A committee will first write a protocol and run pilot studies, and no date has been announced.</p>
      <div class="status warn">
        <b>The figure of 752 is five years old.</b> Until a new census is published, 752 remains the official number, even though the true population today may be higher or lower.
      </div>
      <p class="source">Source: eKantipur (17 April 2026); Mongabay (May 2025); The Kathmandu Post (23 September 2026).</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>The greater one-horned rhino is listed as Vulnerable by the IUCN and lives in tall grassland and riverine forest, such as along the Rapti river in Chitwan.</li>
          <li>Nepal counted a record 429 tigers in 2026. See the <a href="/nepal-tiger-census-2026/">tiger census page</a> and the <a href="/national-parks-of-nepal/">13 national parks</a>.</li>
        </ul>
      </div>
    </section>
'''
RH_EN_FAQ = [
 ("How many rhinos are there in Nepal?", "Nepal had 752 greater one-horned rhinoceroses in the March 2021 census, the latest official count."),
 ("Which national park in Nepal has the most rhinos?", "Chitwan National Park, with 694 of the 752 rhinos in the 2021 census."),
 ("How many rhinos were there in Nepal in 2015?", "The 2015 census counted 645 rhinos."),
 ("When is the next rhino census in Nepal?", "No date has been announced. It was due after 2021 but has been delayed, and the department is redesigning the method."),
 ("Why was Nepal's rhino census delayed?", "Because of budget problems, equipment shortages and technical discussions about the method, according to eKantipur. Mongabay linked a 2025 halt to lost USAID funding."),
 ("How are rhinos counted in Nepal?", "By direct sightings from the back of trained elephants. Dung DNA and camera traps are being considered for the next census."),
 ("Are rhinos endangered in Nepal?", "The greater one-horned rhino is classed as Vulnerable by the IUCN. Nepal's population grew from 645 in 2015 to 752 in 2021."),
 ("In which national parks do rhinos live in Nepal?", "Chitwan, Bardiya, Shuklaphanta and Parsa, according to the 2021 census."),
]
RH_NE_BODY = '''    <section>
      <p class="lede"><strong>पछिल्लो गणना, सन् २०२१ मार्चमा गरिएको, अनुसार नेपालमा ७५२ वटा एक सिङ्गे गैँडा छन्।</strong> विभागले अझै यही सङ्ख्या प्रयोग गर्छ। नयाँ गणना ढिलो भएको छ र विधि पुनर्संरचना हुँदैछ।</p>
    </section>

    <section id="count">
      <h2>निकुञ्जअनुसार गैँडाको सङ्ख्या (२०२१)</h2>
      ''' + fig('nepal_rhino_count_chart', '२०२१ मा निकुञ्जअनुसार नेपालका गैँडा: चितवन ६९४, बर्दिया ३८, शुक्लाफाँटा १७, पर्सा ३', '२०२१ को गणनामा निकुञ्जअनुसार गैँडा। चितवनमा करिब ९२ प्रतिशत छन्।', h=470) + '''
      <div class="table-wrap">
        <table>
          <thead><tr><th>निकुञ्ज</th><th>गैँडा (२०२१)</th></tr></thead>
          <tbody>
            <tr><td>चितवन राष्ट्रिय निकुञ्ज</td><td>६९४</td></tr>
            <tr><td>बर्दिया राष्ट्रिय निकुञ्ज</td><td>३८</td></tr>
            <tr><td>शुक्लाफाँटा राष्ट्रिय निकुञ्ज</td><td>१७</td></tr>
            <tr><td>पर्सा राष्ट्रिय निकुञ्ज</td><td>३</td></tr>
            <tr><td><strong>जम्मा</strong></td><td><strong>७५२</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: द काठमाडौं पोस्ट, "Nepal's rhino census is getting a scientific makeover" (२३ सेप्टेम्बर २०२६)।</p>
    </section>

    <section id="trend">
      <h2>गैँडाको सङ्ख्या कसरी बदलियो?</h2>
      <p>सन् २०१५ को गणनामा ६४५ गैँडा थिए। सन् २०२१ मार्चको गणनामा ७५२ भेटिए, १०७ को वृद्धि, जसमा १३६ बच्चा थिए। सेभ द राइनोका अनुसार २०१५ देखि २०२१ बीच १६१ गैँडा मरे, तीमध्ये ६ वटा सिकारीले मारेका। मोन्गाबेका अनुसार वृद्धिदर सन् २०११-२०१८ मा वार्षिक करिब ५ देखि ६ प्रतिशत थियो, २०१८-२०२१ मा करिब ३ प्रतिशतमा झर्‍यो।</p>
      <p class="source">स्रोत: Save the Rhino; Mongabay (मे २०२५)।</p>
    </section>

    <section id="next">
      <h2>नयाँ गैँडा गणना किन भएको छैन?</h2>
      <p>नेपालमा करिब पाँच वर्षमा एकपटक गैँडा गणना हुन्छ, पछिल्लो सन् २०२१ मा भयो। इकान्तिपुरका अनुसार २०८१ सालमा हुने तोकिएको गणना बजेट समस्या, उपकरणको अभाव र प्राविधिक छलफलका कारण ढिलो भयो। मोन्गाबेले सन् २०२५ मा अमेरिकी सहयोग (युएसएड) फिर्ता भएपछि करिब १,१५,००० देखि १,५५,००० अमेरिकी डलर लाग्ने गणना रोकिएको जनाएको थियो।</p>
      <p>विभाग अहिले नयाँ विधि हेर्दैछ। हालको विधिमा तालिम प्राप्त हात्तीको पिठ्युँमा बसेर घाँसेमैदान छिचोलिन्छ, जुन जोखिमपूर्ण छ: सन् २०२१ मा जङ्गली हात्तीले सर्वेक्षणको हात्तीमाथि आक्रमण गर्दा एक प्राविधिक घाइते भए। गोबरको डीएनए विश्लेषण, क्यामेरा ट्र्याप र दुवैको मिश्रण विचाराधीन छन्। पहिले समितिले प्रोटोकल बनाउनेछ र प्रयोगात्मक अध्ययन गर्नेछ। मिति तोकिएको छैन।</p>
      <div class="status warn">
        <b>७५२ पाँच वर्ष पुरानो सङ्ख्या हो।</b> नयाँ गणना प्रकाशित नभएसम्म ७५२ नै आधिकारिक सङ्ख्या हो, यद्यपि अहिलेको वास्तविक सङ्ख्या बढी वा कम हुन सक्छ।
      </div>
      <p class="source">स्रोत: इकान्तिपुर (१७ अप्रिल २०२६); Mongabay (मे २०२५); द काठमाडौं पोस्ट (२३ सेप्टेम्बर २०२६)।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>एक सिङ्गे गैँडा आइयुसीएनको "संवेदनशील" सूचीमा छ र चितवनको राप्ती किनार जस्ता अग्ला घाँसे मैदान र नदी किनारको जङ्गलमा बस्छ।</li>
          <li>सन् २०२६ मा नेपालमा रेकर्ड ४२९ बाघ गणना भयो। <a href="/ne/nepal-tiger-census-2026/">बाघ गणना पृष्ठ</a> र <a href="/ne/national-parks-of-nepal/">१३ राष्ट्रिय निकुञ्ज</a> हेर्नुहोस्।</li>
        </ul>
      </div>
    </section>
'''
RH_NE_FAQ = [
 ("नेपालमा कति गैँडा छन्?", "सन् २०२१ मार्चको गणनामा नेपालमा ७५२ एक सिङ्गे गैँडा थिए, जुन पछिल्लो आधिकारिक गणना हो।"),
 ("नेपालको कुन राष्ट्रिय निकुञ्जमा सबैभन्दा धेरै गैँडा छन्?", "चितवन राष्ट्रिय निकुञ्ज, २०२१ को गणनाका ७५२ मध्ये ६९४ गैँडा।"),
 ("सन् २०१५ मा नेपालमा कति गैँडा थिए?", "सन् २०१५ को गणनामा ६४५ गैँडा थिए।"),
 ("नेपालमा अर्को गैँडा गणना कहिले हुन्छ?", "मिति तोकिएको छैन। २०२१ पछि हुनुपर्ने थियो तर ढिलो भएको छ र विभागले विधि पुनर्संरचना गर्दैछ।"),
 ("नेपालको गैँडा गणना किन ढिलो भयो?", "इकान्तिपुरका अनुसार बजेट समस्या, उपकरण अभाव र विधिबारे प्राविधिक छलफलका कारण। मोन्गाबेले २०२५ को रोकावटलाई युएसएड सहयोग फिर्ता हुनुसँग जोडेको छ।"),
 ("नेपालमा गैँडा कसरी गणना गरिन्छ?", "तालिम प्राप्त हात्तीको पिठ्युँबाट प्रत्यक्ष हेरेर। अर्को गणनाका लागि गोबरको डीएनए र क्यामेरा ट्र्यापबारे विचार हुँदैछ।"),
 ("के नेपालमा गैँडा लोपोन्मुख छन्?", "एक सिङ्गे गैँडा आइयुसीएनको 'संवेदनशील' श्रेणीमा छ। नेपालमा सङ्ख्या २०१५ को ६४५ बाट २०२१ मा ७५२ पुग्यो।"),
 ("नेपालका कुन निकुञ्जमा गैँडा बस्छन्?", "२०२१ को गणनाअनुसार चितवन, बर्दिया, शुक्लाफाँटा र पर्सा।"),
]

SL_EN_BODY = '''    <section>
      <p class="lede"><strong>Nepal has an estimated 397 snow leopards.</strong> This is the country's first national estimate, from a Department of National Parks and Wildlife Conservation report released in April 2025 using data collected from 2015 to 2024.</p>
    </section>

    <section id="numbers">
      <h2>The 2025 Snow Leopard Estimate</h2>
      ''' + fig('nepal_snow_leopard_chart', 'Bar chart comparing the snow leopard estimates of Nepal (397) and India (718)', 'Snow leopard estimates: Nepal 397 and India 718.', h=470) + '''
      <div class="table-wrap">
        <table>
          <tbody>
            <tr><th>Estimate</th><td>397 snow leopards</td></tr>
            <tr><th>Density</th><td>Mean of 1.56 individuals per 100 km²</td></tr>
            <tr><th>Data</th><td>Seven study regions, collected 2015 to 2024</td></tr>
            <tr><th>Methods</th><td>Camera traps and genetic analysis of scat (droppings)</td></tr>
            <tr><th>Led by</th><td>Department of National Parks and Wildlife Conservation and Department of Forests and Soil Conservation, with WWF</td></tr>
            <tr><th>Compare</th><td>India: 718 (January 2024 report)</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: Down To Earth, "Nepal home to nearly 400 snow leopards, finds survey"; The Nepali Times, "397 snow leopards" (25 April 2025); WWF.</p>
    </section>

    <section id="habitat">
      <h2>Where Snow Leopards Live in Nepal</h2>
      <p>Snow leopards live in the high Himalaya, mostly at 3,000 to 5,500 metres. A telemetry study by WWF in the Kangchenjunga Conservation Area found that most collared animals preferred about 13,000 to 16,000 feet (roughly 4,000 to 4,900 metres), and the highest point recorded was 19,186 feet. Three of four collared animals crossed into China or India for part of their time, so protection depends on neighbouring countries too. Our <a href="/national-parks-of-nepal/">national parks page</a> lists the Himalayan parks, including Shey Phoksundo, Sagarmatha and Langtang.</p>
      <div class="status warn">
        <b>Much of the habitat is unprotected.</b> The director general of the Department of Forests and Soil Conservation said a significant share of snow leopard habitat lies outside protected areas.
      </div>
      <p class="source">Source: Down To Earth; WWF, "This year brings hopeful news for Nepal's snow leopards". The elevation range for the species is general knowledge and not from these reports.</p>
    </section>

    <section id="threats">
      <h2>Threats</h2>
      <p>WWF names habitat loss and fragmentation from infrastructure, climate change and human-wildlife conflict as the main pressures, and poaching is described as a persistent threat to the species. The IUCN lists the snow leopard as Vulnerable.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>The estimate is described as the first robust national figure, so earlier numbers you may see online were rough guesses.</li>
          <li>Snow leopards share Nepal's mountains with Mount Everest. See our <a href="/national-everest/">Mount Everest page</a>.</li>
        </ul>
      </div>
    </section>
'''
SL_EN_FAQ = [
 ("How many snow leopards are there in Nepal?", "An estimated 397, according to the first national estimate released in April 2025."),
 ("Who counted the snow leopards in Nepal?", "A report by the Department of National Parks and Wildlife Conservation and the Department of Forests and Soil Conservation, announced with WWF."),
 ("How was the snow leopard population estimated?", "With camera traps and genetic analysis of scat, using data collected across seven study regions from 2015 to 2024."),
 ("How many snow leopards are there in India?", "India's January 2024 status report estimated 718 snow leopards."),
 ("Are snow leopards endangered?", "The IUCN lists the snow leopard as Vulnerable. Main threats include habitat loss, climate change and human-wildlife conflict."),
 ("Where do snow leopards live in Nepal?", "In the high Himalaya, including protected areas such as Kangchenjunga Conservation Area. A significant part of their habitat is outside protected areas."),
]
SL_NE_BODY = '''    <section>
      <p class="lede"><strong>नेपालमा अनुमानित ३९७ हिउँचितुवा छन्।</strong> सन् २०१५ देखि २०२४ सम्म सङ्कलित तथ्यांकका आधारमा राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभागले सन् २०२५ अप्रिलमा सार्वजनिक गरेको प्रतिवेदनबाट आएको देशको पहिलो राष्ट्रिय अनुमान हो।</p>
    </section>

    <section id="numbers">
      <h2>सन् २०२५ को हिउँचितुवा अनुमान</h2>
      ''' + fig('nepal_snow_leopard_chart', 'नेपाल (३९७) र भारत (७१८) को हिउँचितुवा अनुमानको तुलना बार चार्ट', 'हिउँचितुवा अनुमान: नेपाल ३९७ र भारत ७१८।', h=470) + '''
      <div class="table-wrap">
        <table>
          <tbody>
            <tr><th>अनुमान</th><td>३९७ हिउँचितुवा</td></tr>
            <tr><th>घनत्व</th><td>प्रति १०० वर्ग कि.मी. औसत १.५६</td></tr>
            <tr><th>तथ्यांक</th><td>सात अध्ययन क्षेत्र, २०१५ देखि २०२४ सम्म सङ्कलित</td></tr>
            <tr><th>विधि</th><td>क्यामेरा ट्र्याप र मल (गोबर) को आनुवंशिक विश्लेषण</td></tr>
            <tr><th>नेतृत्व</th><td>राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभाग र वन तथा भूसंरक्षण विभाग, डब्ल्युडब्ल्युएफसँग</td></tr>
            <tr><th>तुलना</th><td>भारत: ७१८ (जनवरी २०२४ को प्रतिवेदन)</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: Down To Earth, "Nepal home to nearly 400 snow leopards, finds survey"; द नेपाली टाइम्स, "397 snow leopards" (२५ अप्रिल २०२५); WWF।</p>
    </section>

    <section id="habitat">
      <h2>नेपालमा हिउँचितुवा कहाँ बस्छन्?</h2>
      <p>हिउँचितुवा अग्ला हिमालमा, प्रायः ३,००० देखि ५,५०० मिटरमा बस्छ। कञ्चनजङ्घा संरक्षण क्षेत्रमा डब्ल्युडब्ल्युएफले गरेको टेलिमेट्री अध्ययनमा कलर लगाइएका अधिकांशले करिब १३,००० देखि १६,००० फिट (करिब ४,००० देखि ४,९०० मिटर) रुचाए र सबैभन्दा उच्च रेकर्ड १९,१८६ फिट थियो। कलर लगाइएका चारमध्ये तीन केही समय चीन वा भारततिर पुगे, त्यसैले संरक्षणमा छिमेकी देशको भूमिका पनि चाहिन्छ। हिमाली निकुञ्जहरू, शे-फोक्सुन्डो, सगरमाथा र लाङटाङ सहित, <a href="/ne/national-parks-of-nepal/">राष्ट्रिय निकुञ्ज पृष्ठ</a> मा छन्।</p>
      <div class="status warn">
        <b>धेरै बासस्थान असंरक्षित छ।</b> वन तथा भूसंरक्षण विभागका महानिर्देशकका अनुसार हिउँचितुवाको बासस्थानको उल्लेख्य भाग संरक्षित क्षेत्रबाहिर पर्छ।
      </div>
      <p class="source">स्रोत: Down To Earth; WWF, "This year brings hopeful news for Nepal's snow leopards"। प्रजातिको उचाइ दायरा सामान्य जानकारी हो, यी प्रतिवेदनबाट होइन।</p>
    </section>

    <section id="threats">
      <h2>खतराहरू</h2>
      <p>डब्ल्युडब्ल्युएफले पूर्वाधारबाट बासस्थान क्षति र विखण्डन, जलवायु परिवर्तन र मानव-वन्यजन्तु द्वन्द्वलाई मुख्य दबाब भनेको छ, र चोरीसिकारी प्रजातिको निरन्तर खतरा भनिएको छ। आइयुसीएनले हिउँचितुवालाई "संवेदनशील" सूचीमा राखेको छ।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>यो अनुमानलाई पहिलो भरपर्दो राष्ट्रिय सङ्ख्या भनिएको छ, त्यसैले अनलाइनमा देखिने अघिल्ला सङ्ख्या मोटामोटी अनुमान थिए।</li>
          <li>हिउँचितुवा सगरमाथा रहेको हिमाली क्षेत्र साझा गर्छ। <a href="/ne/national-everest/">सगरमाथा पृष्ठ</a> हेर्नुहोस्।</li>
        </ul>
      </div>
    </section>
'''
SL_NE_FAQ = [
 ("नेपालमा कति हिउँचितुवा छन्?", "सन् २०२५ अप्रिलमा सार्वजनिक पहिलो राष्ट्रिय अनुमानअनुसार अनुमानित ३९७।"),
 ("नेपालमा हिउँचितुवा कसले गणना गर्‍यो?", "राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण विभाग र वन तथा भूसंरक्षण विभागको प्रतिवेदन, डब्ल्युडब्ल्युएफसँग सार्वजनिक।"),
 ("हिउँचितुवाको सङ्ख्या कसरी अनुमान गरियो?", "सन् २०१५ देखि २०२४ सम्म सात अध्ययन क्षेत्रमा सङ्कलित तथ्यांकमा क्यामेरा ट्र्याप र मलको आनुवंशिक विश्लेषणबाट।"),
 ("भारतमा कति हिउँचितुवा छन्?", "भारतको जनवरी २०२४ को प्रतिवेदनले ७१८ हिउँचितुवा अनुमान गरेको थियो।"),
 ("के हिउँचितुवा लोपोन्मुख हो?", "आइयुसीएनले हिउँचितुवालाई 'संवेदनशील' सूचीमा राखेको छ। बासस्थान क्षति, जलवायु परिवर्तन र मानव-वन्यजन्तु द्वन्द्व मुख्य खतरा हुन्।"),
 ("नेपालमा हिउँचितुवा कहाँ बस्छन्?", "कञ्चनजङ्घा संरक्षण क्षेत्र जस्ता संरक्षित क्षेत्रसहित अग्ला हिमालमा। बासस्थानको उल्लेख्य भाग संरक्षित क्षेत्रबाहिर छ।"),
]

WP_EN_BODY = '''    <section>
      <p class="lede">Latest official counts: <strong>429 tigers</strong> (2026), <strong>752 rhinos</strong> (2021) and an estimated <strong>397 snow leopards</strong> (2025). Here is how each number was reached and how old it is.</p>
    </section>

    <section id="table">
      <h2>Wildlife Population of Nepal at a Glance</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Species</th><th>Latest count</th><th>Year</th><th>Earlier count</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Bengal tiger</td><td><strong>429</strong></td><td>2026</td><td>355 (2022)</td><td><a href="/nepal-tiger-census-2026/">Tiger census</a></td></tr>
            <tr><td>One-horned rhino</td><td><strong>752</strong></td><td>2021</td><td>645 (2015)</td><td><a href="/nepal-rhino-count/">Rhino count</a></td></tr>
            <tr><td>Snow leopard</td><td><strong>397</strong> (estimate)</td><td>2025</td><td>First national estimate</td><td><a href="/nepal-snow-leopard-population/">Snow leopards</a></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Sources: IUCN and The Kathmandu Post (tigers); The Kathmandu Post and Save the Rhino (rhinos); Down To Earth and The Nepali Times (snow leopards). See each page for details.</p>
    </section>

    <section id="notes">
      <h2>How to Read These Numbers</h2>
      <p>The tiger number is a 2026 camera-trap census. The rhino number is from 2021, counted from elephant-back, and a new census has been delayed. The snow leopard number is a model-based estimate from data gathered over nine years, so it is not a head count taken on one day. Counts of different animals are not directly comparable.</p>
      <div class="status warn">
        <b>Not on this page.</b> We have not found a current official count for elephants, red pandas or gharial, so we do not list one. We will add them when a source is published.
      </div>
      <p>The tiger and rhino numbers come from the Terai parks. Browse all <a href="/national-parks-of-nepal/">13 national parks</a>, and see why the cow, not the tiger, is the <a href="/national-animal/">national animal</a>.</p>
    </section>
'''
WP_EN_FAQ = [
 ("How many tigers are there in Nepal?", "429 in the 2026 census."),
 ("How many rhinos are there in Nepal?", "752 in the 2021 census, the latest official count."),
 ("How many snow leopards are there in Nepal?", "An estimated 397, from a report released in April 2025."),
 ("What is the national animal of Nepal?", "The cow. The tiger, rhino and snow leopard are important wildlife but are not national symbols."),
 ("Which animals are counted regularly in Nepal?", "Tigers are counted about every four years and rhinos about every five years. The snow leopard figure is a first national estimate."),
]
WP_NE_BODY = '''    <section>
      <p class="lede">पछिल्लो आधिकारिक गणना: <strong>४२९ बाघ</strong> (२०२६), <strong>७५२ गैँडा</strong> (२०२१) र अनुमानित <strong>३९७ हिउँचितुवा</strong> (२०२५)। प्रत्येक सङ्ख्या कसरी आयो र कति पुरानो छ भन्ने यहाँ छ।</p>
    </section>

    <section id="table">
      <h2>नेपालका वन्यजन्तुको सङ्ख्या एकै नजरमा</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>प्रजाति</th><th>पछिल्लो सङ्ख्या</th><th>साल</th><th>अघिल्लो सङ्ख्या</th><th>विवरण</th></tr></thead>
          <tbody>
            <tr><td>बङ्गाल बाघ</td><td><strong>४२९</strong></td><td>२०२६</td><td>३५५ (२०२२)</td><td><a href="/ne/nepal-tiger-census-2026/">बाघ गणना</a></td></tr>
            <tr><td>एक सिङ्गे गैँडा</td><td><strong>७५२</strong></td><td>२०२१</td><td>६४५ (२०१५)</td><td><a href="/ne/nepal-rhino-count/">गैँडा गणना</a></td></tr>
            <tr><td>हिउँचितुवा</td><td><strong>३९७</strong> (अनुमान)</td><td>२०२५</td><td>पहिलो राष्ट्रिय अनुमान</td><td><a href="/ne/nepal-snow-leopard-population/">हिउँचितुवा</a></td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: IUCN र द काठमाडौं पोस्ट (बाघ); द काठमाडौं पोस्ट र Save the Rhino (गैँडा); Down To Earth र द नेपाली टाइम्स (हिउँचितुवा)। विवरणका लागि प्रत्येक पृष्ठ हेर्नुहोस्।</p>
    </section>

    <section id="notes">
      <h2>यी सङ्ख्या कसरी पढ्ने?</h2>
      <p>बाघको सङ्ख्या सन् २०२६ को क्यामेरा ट्र्याप गणनाको हो। गैँडाको सङ्ख्या सन् २०२१ को हो, हात्तीको पिठ्युँबाट गणना गरिएको, र नयाँ गणना ढिलो भएको छ। हिउँचितुवाको सङ्ख्या नौ वर्षमा सङ्कलित तथ्यांकको मोडलमा आधारित अनुमान हो, एकै दिन गरिएको गणना होइन। फरक जनावरका सङ्ख्या सिधै तुलनायोग्य छैनन्।</p>
      <div class="status warn">
        <b>यो पृष्ठमा नभएका।</b> हात्ती, रातो पाण्डा वा घडियालको हालको आधिकारिक गणना हामीले भेटेका छैनौं, त्यसैले दिएका छैनौं। स्रोत प्रकाशित भएपछि थप्नेछौं।
      </div>
      <p>बाघ र गैँडाको सङ्ख्या तराईका निकुञ्जबाट आएको हो। सबै <a href="/ne/national-parks-of-nepal/">१३ राष्ट्रिय निकुञ्ज</a> हेर्नुहोस् र बाघ होइन गाई किन <a href="/ne/national-animal/">राष्ट्रिय पशु</a> हो भन्ने पनि पढ्नुहोस्।</p>
    </section>
'''
WP_NE_FAQ = [
 ("नेपालमा कति बाघ छन्?", "सन् २०२६ को गणनामा ४२९।"),
 ("नेपालमा कति गैँडा छन्?", "सन् २०२१ को गणनामा ७५२, जुन पछिल्लो आधिकारिक गणना हो।"),
 ("नेपालमा कति हिउँचितुवा छन्?", "सन् २०२५ अप्रिलमा सार्वजनिक प्रतिवेदनअनुसार अनुमानित ३९७।"),
 ("नेपालको राष्ट्रिय पशु कुन हो?", "गाई। बाघ, गैँडा र हिउँचितुवा महत्त्वपूर्ण वन्यजन्तु हुन्, तर राष्ट्रिय चिन्ह होइनन्।"),
 ("नेपालमा कुन जनावर नियमित गणना गरिन्छ?", "बाघ करिब चार वर्षमा र गैँडा करिब पाँच वर्षमा गणना हुन्छ। हिउँचितुवाको सङ्ख्या पहिलो राष्ट्रिय अनुमान हो।"),
]

EXTRA_PAGES = EXTRA_PAGES + [
 _mk('nepal-rhino-count', 'nepal_rhino_count_hero.webp', 'Rhino census of Nepal', 'https://en.wikipedia.org/wiki/Greater_one-horned_rhinoceros',
  _en('How Many Rhinos in Nepal? 752 (2021 Count) and Next Census',
      'Nepal has 752 one-horned rhinos (2021 census): Chitwan 694, Bardiya 38, Shuklaphanta 17, Parsa 3. Why the new census is delayed.',
      'How Many Rhinos in Nepal? 752', 'Nepal rhino count by park from the 2021 census, growth since 2015 and why the next census is delayed.',
      'Nepal rhino population: 752 in 2021, count by park, trend since 2015 and the delayed next census.', 'Rhino Count',
      'Infographic: 752 rhinos in Nepal', 'Rhino census', 'Rhinos <em>in Nepal</em>',
      '<strong>Nepal has 752 greater one-horned rhinos</strong> (March 2021 census). Chitwan holds 694 of them. The next census is delayed.',
      ['752 rhinos', 'Census 2021', 'Next census delayed'],
      [('Total (2021)', '752', False), ('Chitwan', '694', False), ('Bardiya', '38', False), ('Shuklaphanta', '17', False), ('Parsa', '3', False), ('2015 count', '645', False)],
      ('गैँडा', 'Gaida', 'gai-da'), RH_EN_BODY, RH_EN_FAQ, REL_RH, 'Rhino counts reflect the health of the Terai national parks.'),
  _ne('नेपालमा कति गैँडा छन्? ७५२ (२०२१ गणना), निकुञ्जअनुसार र अर्को गणना',
      'नेपालमा ७५२ एक सिङ्गे गैँडा छन् (२०२१): चितवन ६९४, बर्दिया ३८, शुक्लाफाँटा १७, पर्सा ३। नयाँ गणना किन ढिलो भयो।',
      'नेपालमा कति गैँडा छन्? ७५२', 'सन् २०२१ को गणनाअनुसार निकुञ्जगत गैँडा सङ्ख्या, २०१५ पछिको वृद्धि र अर्को गणना ढिलाइको कारण।',
      'नेपालमा गैँडाको सङ्ख्या: २०२१ मा ७५२, निकुञ्जअनुसार गणना, २०१५ पछिको प्रवृत्ति र ढिलो भएको अर्को गणना।', 'गैँडा गणना',
      'नेपालमा ७५२ गैँडाको इन्फोग्राफिक', 'गैँडा गणना', 'नेपालका <em>गैँडा</em>',
      '<strong>नेपालमा ७५२ एक सिङ्गे गैँडा छन्</strong> (मार्च २०२१ को गणना)। तीमध्ये ६९४ चितवनमा छन्। अर्को गणना ढिलो भएको छ।',
      ['७५२ गैँडा', 'गणना २०२१', 'अर्को गणना ढिलो'],
      [('जम्मा (२०२१)', '७५२', False), ('चितवन', '६९४', False), ('बर्दिया', '३८', False), ('शुक्लाफाँटा', '१७', False), ('पर्सा', '३', False), ('२०१५ को गणना', '६४५', False)],
      ('गैँडा', 'Gaida', 'गैँडा'), RH_NE_BODY, RH_NE_FAQ, REL_RH_NE, 'गैँडा गणनाले तराईका राष्ट्रिय निकुञ्जको अवस्था देखाउँछ।')),
 _mk('nepal-snow-leopard-population', 'nepal_snow_leopard_hero.webp', 'Snow leopard population of Nepal', 'https://en.wikipedia.org/wiki/Snow_leopard',
  _en('How Many Snow Leopards in Nepal? 397 (2025 Estimate)',
      "Nepal has an estimated 397 snow leopards, the first national estimate (2025). Method, density, habitat, threats and India's number.",
      'How Many Snow Leopards in Nepal? 397', "Nepal's first national snow leopard estimate: 397 animals. Method, density, habitat and threats.",
      "Nepal's snow leopard population: 397 estimated, how it was counted, habitat and threats.", 'Snow Leopard Population',
      'Infographic: 397 snow leopards in Nepal', 'Snow leopard survey', 'Snow Leopards <em>in Nepal</em>',
      '<strong>Nepal has an estimated 397 snow leopards.</strong> It is the first national estimate, released in April 2025 from data gathered 2015 to 2024.',
      ['397 estimated', 'First national estimate', 'Vulnerable (IUCN)'],
      [('Estimate', '397', False), ('Density', '1.56 per 100 km²', False), ('Data years', '2015 to 2024', False), ('Method', 'Camera traps, scat DNA', False), ('India (2024)', '718', False), ('IUCN status', 'Vulnerable', False)],
      ('हिउँचितुवा', 'Hiunchituwa', 'hi-un-chi-tu-wa'), SL_EN_BODY, SL_EN_FAQ, REL_SL, 'The snow leopard lives in the Himalayan parks and conservation areas.'),
  _ne('नेपालमा कति हिउँचितुवा छन्? ३९७ (पहिलो राष्ट्रिय अनुमान, २०२५)',
      'नेपालमा अनुमानित ३९७ हिउँचितुवा छन्, पहिलो राष्ट्रिय अनुमान (२०२५)। विधि, घनत्व, बासस्थान, खतरा र भारतको सङ्ख्या।',
      'नेपालमा कति हिउँचितुवा छन्? ३९७', 'नेपालको पहिलो राष्ट्रिय हिउँचितुवा अनुमान: ३९७। विधि, घनत्व, बासस्थान र खतरा।',
      'नेपालमा हिउँचितुवाको सङ्ख्या: अनुमानित ३९७, कसरी गणना भयो, बासस्थान र खतरा।', 'हिउँचितुवाको सङ्ख्या',
      'नेपालमा ३९७ हिउँचितुवाको इन्फोग्राफिक', 'हिउँचितुवा सर्वेक्षण', 'नेपालका <em>हिउँचितुवा</em>',
      '<strong>नेपालमा अनुमानित ३९७ हिउँचितुवा छन्।</strong> सन् २०१५ देखि २०२४ को तथ्यांकबाट सन् २०२५ अप्रिलमा सार्वजनिक पहिलो राष्ट्रिय अनुमान।',
      ['३९७ अनुमानित', 'पहिलो राष्ट्रिय अनुमान', 'संवेदनशील (आइयुसीएन)'],
      [('अनुमान', '३९७', False), ('घनत्व', 'प्रति १०० वर्ग कि.मी. १.५६', False), ('तथ्यांक वर्ष', '२०१५ देखि २०२४', False), ('विधि', 'क्यामेरा ट्र्याप, मलको डीएनए', False), ('भारत (२०२४)', '७१८', False), ('आइयुसीएन स्थिति', 'संवेदनशील', False)],
      ('हिउँचितुवा', 'Hiunchituwa', 'हिउँचितुवा'), SL_NE_BODY, SL_NE_FAQ, REL_SL_NE, 'हिउँचितुवा हिमाली निकुञ्ज र संरक्षण क्षेत्रमा बस्छ।')),
 _mk('nepal-wildlife-population', 'nepal_wildlife_counts_hero.webp', 'Wildlife of Nepal', 'https://en.wikipedia.org/wiki/Wildlife_of_Nepal',
  _en('Nepal Wildlife Count: 429 Tigers, 752 Rhinos, 397 Snow Leopards',
      'Latest official counts for Nepal tigers (429, 2026), rhinos (752, 2021) and snow leopards (397, 2025), with year, method and links.',
      'Wildlife Population of Nepal (2026)', 'Tigers 429, rhinos 752, snow leopards 397: the latest counts for Nepal wildlife, with year and method.',
      'Latest counts of Nepal wildlife: tigers 429 (2026), rhinos 752 (2021), snow leopards 397 (2025).', 'Wildlife Counts of Nepal',
      'Infographic: tigers 429, rhinos 752, snow leopards 397', 'Wildlife counts', 'Wildlife Population <em>of Nepal</em>',
      '<strong>Tigers 429 (2026), rhinos 752 (2021), snow leopards 397 (2025).</strong> The latest official counts for Nepal, with year and method.',
      ['Tigers 429', 'Rhinos 752', 'Snow leopards 397'],
      [('Tigers', '429 (2026)', False), ('Rhinos', '752 (2021)', False), ('Snow leopards', '397 (2025, estimate)', False), ('National animal', 'Cow (Constitution)', False)],
      ('वन्यजन्तु', 'Banyajantu', 'ban-ya-jan-tu'), WP_EN_BODY, WP_EN_FAQ, REL_WP, 'Wildlife counts sit alongside the official national symbols.'),
  _ne('नेपालका वन्यजन्तुको सङ्ख्या: बाघ ४२९, गैँडा ७५२, हिउँचितुवा ३९७',
      'नेपालका बाघ (४२९, २०२६), गैँडा (७५२, २०२१) र हिउँचितुवा (३९७, २०२५) को पछिल्लो आधिकारिक गणना, साल, विधि र लिङ्कसहित।',
      'नेपालका वन्यजन्तुको सङ्ख्या (२०२६)', 'बाघ ४२९, गैँडा ७५२, हिउँचितुवा ३९७: नेपालका वन्यजन्तुको पछिल्लो गणना, साल र विधिसहित।',
      'नेपालका वन्यजन्तुको पछिल्लो गणना: बाघ ४२९ (२०२६), गैँडा ७५२ (२०२१), हिउँचितुवा ३९७ (२०२५)।', 'वन्यजन्तुको सङ्ख्या',
      'बाघ ४२९, गैँडा ७५२, हिउँचितुवा ३९७ को इन्फोग्राफिक', 'वन्यजन्तु सङ्ख्या', 'नेपालका <em>वन्यजन्तुको सङ्ख्या</em>',
      '<strong>बाघ ४२९ (२०२६), गैँडा ७५२ (२०२१), हिउँचितुवा ३९७ (२०२५)।</strong> नेपालका वन्यजन्तुको पछिल्लो आधिकारिक गणना, साल र विधिसहित।',
      ['बाघ ४२९', 'गैँडा ७५२', 'हिउँचितुवा ३९७'],
      [('बाघ', '४२९ (२०२६)', False), ('गैँडा', '७५२ (२०२१)', False), ('हिउँचितुवा', '३९७ (२०२५, अनुमान)', False), ('राष्ट्रिय पशु', 'गाई (संविधान)', False)],
      ('वन्यजन्तु', 'Banyajantu', 'वन्यजन्तु'), WP_NE_BODY, WP_NE_FAQ, REL_WP_NE, 'वन्यजन्तुको सङ्ख्या आधिकारिक राष्ट्रिय चिन्हहरूसँगै पर्छ।')),
]
