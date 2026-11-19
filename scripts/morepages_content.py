# -*- coding: utf-8 -*-
# Three extra pages: /national-poet/, /world-heritage-sites/, /is-yeti-national-symbol/ (EN + NE).
# Facts and sources:
#  - Madhav Prasad Ghimire: Kathmandu Post, "Madhav Prasad Ghimire, the Rastra Kavi, dies at 101" (19 Aug 2020): born 23 Sep 1919 Putsun, Lamjung;
#    died 18 Aug 2020 Lainchaur; title Rastra Kavi conferred by the government in 2003; works Gauri, Kinnar Kinnari, Charu Charcha, Shakuntala, Malati Mangale, Ritambhara.
#  - World Heritage: UNESCO list as summarised on Wikipedia "List of World Heritage Sites in Nepal": Sagarmatha NP 1979, Kathmandu Valley 1979, Chitwan NP 1984, Lumbini 1997;
#    Kathmandu Valley on the In Danger list 2003-2007.
#  - Yeti: Himalayan Times, 1 April 2024, "Yeti - Guardian of the Himalayas to feature on currency notes" carries an April Fool disclaimer.
def _mk(slug, photo, about_name, about_sameas, en, ne):
    return dict(slug=slug, photo=photo, noitemlist=True, about_name=about_name, about_sameas=about_sameas, en=en, ne=ne)

REL_MP = [('national-language', 'National Language'), ('national-day', 'National Day'), ('official-vs-unofficial', 'Official vs Unofficial Symbols'), ('sources', 'Sources & Methodology')]
REL_MP_NE = [('national-language', 'राष्ट्रिय भाषा'), ('national-day', 'राष्ट्रिय दिवस'), ('official-vs-unofficial', 'आधिकारिक कि परम्परागत'), ('sources', 'स्रोत र कार्यविधि')]
REL_WH = [('national-monument', 'National Monument'), ('national-everest', 'Mount Everest'), ('national-museum', 'National Museum'), ('official-vs-unofficial', 'Official vs Unofficial Symbols')]
REL_WH_NE = [('national-monument', 'राष्ट्रिय स्मारक'), ('national-everest', 'सगरमाथा'), ('national-museum', 'राष्ट्रिय संग्रहालय'), ('official-vs-unofficial', 'आधिकारिक कि परम्परागत')]
REL_YT = [('national-animal', 'National Animal'), ('national-everest', 'Mount Everest'), ('official-vs-unofficial', 'Official vs Unofficial Symbols'), ('sources', 'Sources & Methodology')]
REL_YT_NE = [('national-animal', 'राष्ट्रिय पशु'), ('national-everest', 'सगरमाथा'), ('official-vs-unofficial', 'आधिकारिक कि परम्परागत'), ('sources', 'स्रोत र कार्यविधि')]

# ---------------- National poet ----------------
MP_EN_BODY = '''    <section>
      <p class="lede">Nepal's <strong>national poet</strong> (<em>Rastra Kavi</em>, राष्ट्रकवि) is <strong>Madhav Prasad Ghimire</strong> (1919-2020). The government conferred the title on him in <strong>2003</strong>, according to the Kathmandu Post.</p>
    </section>

    <section id="who">
      <h2>Who Was Madhav Prasad Ghimire?</h2>
      <div class="table-wrap">
        <table>
          <tbody>
            <tr><th>Born</th><td>23 September 1919, Putsun, Lamjung</td></tr>
            <tr><th>Died</th><td>18 August 2020, Lainchaur, Kathmandu, aged 101</td></tr>
            <tr><th>Title</th><td>Rastra Kavi (national poet), conferred by the government in 2003</td></tr>
            <tr><th>Posts held</th><td>Editor of Gorkhapatra from 1946; chancellor of the Royal Nepal Academy (now Nepal Academy), 1988-1990</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: The Kathmandu Post, "Madhav Prasad Ghimire, the Rastra Kavi, dies at 101" (19 August 2020).</p>
    </section>

    <section id="works">
      <h2>His Best-Known Works</h2>
      <div class="chips"><span>Gauri</span><span>Kinnar Kinnari</span><span>Charu Charcha</span><span>Shakuntala</span><span>Malati Mangale</span><span>Ritambhara</span></div>
      <p><em>Gauri</em> is an epic written as an elegy for his first wife. <em>Malati Mangale</em> is a musical drama first staged in 1985. <em>Ritambhara</em>, his last epic, was unfinished when he died. Poems such as <em>Nepali Hami Rahaula Kaha</em> and <em>Himal Pari Himal Wari</em> are among those the Post lists as notable.</p>
      <p class="source">Source: The Kathmandu Post, 19 August 2020.</p>
    </section>

    <section id="status">
      <h2>Is "National Poet" an Official Symbol?</h2>
      <div class="status warn">
        <b>It is an honorary title, not a constitutional symbol.</b> The Constitution of Nepal fixes the flag, anthem, emblem, colour, flower, animal and bird. The Rastra Kavi title is a government honour given to a person. We have not seen the 2003 decision text, so the year rests on the Kathmandu Post report.
      </div>
      <p>Ghimire was cremated with state honours in August 2020.</p>
      <p class="source">Source: The Kathmandu Post photo story on his final rites (19 August 2020).</p>
    </section>

    <section id="dyk-sec">
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>Ghimire lived to 101 and edited the state daily Gorkhapatra from 1946.</li>
          <li>The national anthem's lyrics were not written by him. See our <a href="/national-anthem/">national anthem page</a> for its lyricist and history.</li>
        </ul>
      </div>
    </section>
'''
MP_EN_FAQ = [
 ("Who is the national poet of Nepal?", "Madhav Prasad Ghimire (1919-2020) is Nepal's national poet, known as Rastra Kavi. The government conferred the title in 2003, according to the Kathmandu Post."),
 ("What does Rastra Kavi mean?", "Rastra Kavi (राष्ट्रकवि) means national poet. It is an honorary title given by the government."),
 ("When did Madhav Prasad Ghimire die?", "He died on 18 August 2020 at his home in Lainchaur, Kathmandu, aged 101."),
 ("What is Madhav Prasad Ghimire famous for?", "He is known for epics and poems such as Gauri, Shakuntala and Ritambhara, the essay collection Charu Charcha and the musical drama Malati Mangale."),
 ("Is the national poet written in the Constitution of Nepal?", "No. It is an honorary government title, not one of the symbols set by the Constitution."),
]
MP_NE_BODY = '''    <section>
      <p class="lede">नेपालका <strong>राष्ट्रकवि</strong> <strong>माधवप्रसाद घिमिरे</strong> (१९१९-२०२०) हुन्। द काठमाडौं पोस्टका अनुसार सरकारले उनलाई सन् <strong>२००३</strong> मा यो उपाधि प्रदान गर्‍यो।</p>
    </section>

    <section id="who">
      <h2>माधवप्रसाद घिमिरे को हुन्?</h2>
      <div class="table-wrap">
        <table>
          <tbody>
            <tr><th>जन्म</th><td>२३ सेप्टेम्बर १९१९, पुटसुन, लमजुङ</td></tr>
            <tr><th>निधन</th><td>१८ अगस्ट २०२०, लैनचौर, काठमाडौं, १०१ वर्षको उमेरमा</td></tr>
            <tr><th>उपाधि</th><td>राष्ट्रकवि, सरकारद्वारा सन् २००३ मा प्रदान</td></tr>
            <tr><th>जिम्मेवारी</th><td>सन् १९४६ देखि गोरखापत्रका सम्पादक; शाही नेपाल प्रज्ञा प्रतिष्ठान (हालको नेपाल प्रज्ञा प्रतिष्ठान) का कुलपति, १९८८-१९९०</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: द काठमाडौं पोस्ट, "Madhav Prasad Ghimire, the Rastra Kavi, dies at 101" (१९ अगस्ट २०२०)।</p>
    </section>

    <section id="works">
      <h2>प्रमुख कृतिहरू</h2>
      <div class="chips"><span>गौरी</span><span>किन्नर किन्नरी</span><span>चारु चर्चा</span><span>शकुन्तला</span><span>मालती मंगले</span><span>ऋतम्भरा</span></div>
      <p><em>गौरी</em> उनकी पहिलो पत्नीको सम्झनामा लेखिएको महाकाव्य हो। <em>मालती मंगले</em> सन् १९८५ मा पहिलो पटक मञ्चन भएको गीतिनाटक हो। उनको अन्तिम महाकाव्य <em>ऋतम्भरा</em> निधन हुँदा अधुरो थियो। <em>नेपाली हामी रहौँला कहाँ</em> र <em>हिमाल परि हिमाल वारि</em> जस्ता कविता पोस्टले उल्लेखनीय भनेर सूचीबद्ध गरेको छ।</p>
      <p class="source">स्रोत: द काठमाडौं पोस्ट, १९ अगस्ट २०२०।</p>
    </section>

    <section id="status">
      <h2>के "राष्ट्रकवि" आधिकारिक चिन्ह हो?</h2>
      <div class="status warn">
        <b>यो मानार्थ उपाधि हो, संवैधानिक चिन्ह होइन।</b> नेपालको संविधानले झण्डा, राष्ट्रगान, प्रतीक चिन्ह, रङ, फूल, पशु र चरा तोकेको छ। राष्ट्रकवि सरकारले व्यक्तिलाई दिने सम्मान हो। २००३ को निर्णयको पाठ हामीले हेरेका छैनौं, त्यसैले वर्ष द काठमाडौं पोस्टको विवरणमा आधारित छ।
      </div>
      <p>सन् २०२० अगस्टमा घिमिरेको अन्त्येष्टि राजकीय सम्मानसहित गरियो।</p>
      <p class="source">स्रोत: द काठमाडौं पोस्टको अन्तिम संस्कारसम्बन्धी फोटो कथा (१९ अगस्ट २०२०)।</p>
    </section>

    <section id="dyk-sec">
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>घिमिरेले १०१ वर्षको आयु बाँचे र सन् १९४६ देखि सरकारी दैनिक गोरखापत्र सम्पादन गरे।</li>
          <li>राष्ट्रगानका शब्द उनले लेखेका होइनन्। गीतकार र इतिहासका लागि <a href="/ne/national-anthem/">राष्ट्रगान पृष्ठ</a> हेर्नुहोस्।</li>
        </ul>
      </div>
    </section>
'''
MP_NE_FAQ = [
 ("नेपालका राष्ट्रकवि को हुन्?", "माधवप्रसाद घिमिरे (१९१९-२०२०) नेपालका राष्ट्रकवि हुन्। द काठमाडौं पोस्टका अनुसार सरकारले सन् २००३ मा उनलाई यो उपाधि दियो।"),
 ("राष्ट्रकवि भनेको के हो?", "राष्ट्रकवि भनेको राष्ट्रिय कवि हो। यो सरकारले दिने मानार्थ उपाधि हो।"),
 ("माधवप्रसाद घिमिरेको निधन कहिले भयो?", "उनको निधन सन् २०२० अगस्ट १८ मा काठमाडौंस्थित निवासमा १०१ वर्षको उमेरमा भयो।"),
 ("माधवप्रसाद घिमिरे केका लागि प्रसिद्ध छन्?", "गौरी, शकुन्तला, ऋतम्भरा जस्ता महाकाव्य, चारु चर्चा निबन्ध संग्रह र मालती मंगले गीतिनाटकका लागि उनी चिनिन्छन्।"),
 ("के राष्ट्रकवि नेपालको संविधानमा लेखिएको छ?", "छैन। यो मानार्थ सरकारी उपाधि हो, संविधानले तोकेको चिन्ह होइन।"),
]

# ---------------- World Heritage ----------------
WH_EN_BODY = '''    <section>
      <p class="lede">Nepal has <strong>four UNESCO World Heritage Sites</strong>: two natural (<strong>Sagarmatha National Park</strong> and <strong>Chitwan National Park</strong>) and two cultural (the <strong>Kathmandu Valley</strong> and <strong>Lumbini</strong>, the birthplace of the Buddha).</p>
    </section>

    <section id="list">
      <h2>The 4 World Heritage Sites of Nepal</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Site</th><th>Type</th><th>Inscribed</th></tr></thead>
          <tbody>
            <tr><td>Sagarmatha National Park</td><td>Natural</td><td>1979</td></tr>
            <tr><td>Kathmandu Valley</td><td>Cultural</td><td>1979</td></tr>
            <tr><td>Chitwan National Park</td><td>Natural</td><td>1984</td></tr>
            <tr><td>Lumbini, the Birthplace of Lord Buddha</td><td>Cultural</td><td>1997</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: UNESCO World Heritage List, as summarised in "List of World Heritage Sites in Nepal" (Wikipedia).</p>
    </section>

    <section id="valley">
      <h2>What Is Inside the Kathmandu Valley Site?</h2>
      <p>The Kathmandu Valley listing covers seven monument zones: the Durbar Squares of Kathmandu (Hanuman Dhoka), Patan and Bhaktapur, the Buddhist stupas of Swayambhunath and Boudhanath, and the Hindu temples of Pashupatinath and Changu Narayan.</p>
      <div class="chips"><span>Kathmandu Durbar Square</span><span>Patan Durbar Square</span><span>Bhaktapur Durbar Square</span><span>Swayambhunath</span><span>Boudhanath</span><span>Pashupatinath</span><span>Changu Narayan</span></div>
      <div class="status warn">
        <b>It was once on the "in danger" list.</b> The Kathmandu Valley was on UNESCO's List of World Heritage in Danger from 2003 to 2007. We have not checked its current status, so see UNESCO for the latest.
      </div>
    </section>

    <section id="not">
      <h2>What Is Not on the List</h2>
      <p>Famous places such as the Dharahara tower are not separate World Heritage Sites. Pashupatinath is part of the Kathmandu Valley listing. Nepal also keeps a longer "tentative list" of places that may be proposed later.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>Sagarmatha National Park protects the area around Mount Everest. Read more on our <a href="/national-everest/">Mount Everest page</a>.</li>
          <li>Lumbini is where Siddhartha Gautama, the Buddha, was born.</li>
        </ul>
      </div>
    </section>
'''
WH_EN_FAQ = [
 ("How many UNESCO World Heritage Sites are in Nepal?", "Nepal has four: Sagarmatha National Park (1979), the Kathmandu Valley (1979), Chitwan National Park (1984) and Lumbini (1997)."),
 ("What are the World Heritage Sites of Nepal?", "Sagarmatha National Park, Kathmandu Valley, Chitwan National Park and Lumbini, the birthplace of Lord Buddha."),
 ("Which World Heritage Sites in Nepal are natural?", "Sagarmatha National Park and Chitwan National Park are natural sites. The Kathmandu Valley and Lumbini are cultural sites."),
 ("What does the Kathmandu Valley World Heritage Site include?", "Seven monument zones: the Durbar Squares of Kathmandu, Patan and Bhaktapur, Swayambhunath, Boudhanath, Pashupatinath and Changu Narayan."),
 ("When was Lumbini listed as a World Heritage Site?", "Lumbini was inscribed in 1997."),
 ("Was the Kathmandu Valley ever on the danger list?", "Yes, from 2003 to 2007."),
]
WH_NE_BODY = '''    <section>
      <p class="lede">नेपालमा <strong>युनेस्कोका चारवटा विश्व सम्पदा स्थल</strong> छन्: दुई प्राकृतिक (<strong>सगरमाथा राष्ट्रिय निकुञ्ज</strong> र <strong>चितवन राष्ट्रिय निकुञ्ज</strong>) र दुई सांस्कृतिक (<strong>काठमाडौं उपत्यका</strong> र बुद्धको जन्मस्थल <strong>लुम्बिनी</strong>)।</p>
    </section>

    <section id="list">
      <h2>नेपालका ४ विश्व सम्पदा स्थल</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>स्थल</th><th>प्रकार</th><th>सूचीकृत</th></tr></thead>
          <tbody>
            <tr><td>सगरमाथा राष्ट्रिय निकुञ्ज</td><td>प्राकृतिक</td><td>सन् १९७९</td></tr>
            <tr><td>काठमाडौं उपत्यका</td><td>सांस्कृतिक</td><td>सन् १९७९</td></tr>
            <tr><td>चितवन राष्ट्रिय निकुञ्ज</td><td>प्राकृतिक</td><td>सन् १९८४</td></tr>
            <tr><td>लुम्बिनी, भगवान् बुद्धको जन्मस्थल</td><td>सांस्कृतिक</td><td>सन् १९९७</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: युनेस्को विश्व सम्पदा सूची, "List of World Heritage Sites in Nepal" (Wikipedia) मा सारांशित।</p>
    </section>

    <section id="valley">
      <h2>काठमाडौं उपत्यका सम्पदामा के के पर्छन्?</h2>
      <p>काठमाडौं उपत्यकाको सूचीमा सात स्मारक क्षेत्र छन्: काठमाडौं (हनुमानढोका), पाटन र भक्तपुरका दरबार क्षेत्र, स्वयम्भू र बौद्ध स्तुप तथा पशुपतिनाथ र चाँगुनारायण मन्दिर।</p>
      <div class="chips"><span>काठमाडौं दरबार क्षेत्र</span><span>पाटन दरबार क्षेत्र</span><span>भक्तपुर दरबार क्षेत्र</span><span>स्वयम्भू</span><span>बौद्ध</span><span>पशुपतिनाथ</span><span>चाँगुनारायण</span></div>
      <div class="status warn">
        <b>एक पटक "खतरामा परेको" सूचीमा थियो।</b> काठमाडौं उपत्यका सन् २००३ देखि २००७ सम्म युनेस्कोको खतरामा परेको विश्व सम्पदा सूचीमा थियो। हालको अवस्था हामीले जाँचेका छैनौं, पछिल्लो जानकारीका लागि युनेस्को हेर्नुहोस्।
      </div>
    </section>

    <section id="not">
      <h2>सूचीमा नभएका ठाउँ</h2>
      <p>धरहरा जस्ता चर्चित स्थल छुट्टै विश्व सम्पदा स्थल होइनन्। पशुपतिनाथ काठमाडौं उपत्यका सम्पदाकै हिस्सा हो। नेपालसँग पछि प्रस्ताव गर्न सकिने ठाउँहरूको लामो "अस्थायी सूची" पनि छ।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>सगरमाथा राष्ट्रिय निकुञ्जले सगरमाथा वरपरको क्षेत्र जोगाउँछ। हाम्रो <a href="/ne/national-everest/">सगरमाथा पृष्ठ</a> हेर्नुहोस्।</li>
          <li>लुम्बिनी सिद्धार्थ गौतम बुद्धको जन्मस्थल हो।</li>
        </ul>
      </div>
    </section>
'''
WH_NE_FAQ = [
 ("नेपालमा युनेस्कोका कतिवटा विश्व सम्पदा स्थल छन्?", "नेपालमा चारवटा छन्: सगरमाथा राष्ट्रिय निकुञ्ज (१९७९), काठमाडौं उपत्यका (१९७९), चितवन राष्ट्रिय निकुञ्ज (१९८४) र लुम्बिनी (१९९७)।"),
 ("नेपालका विश्व सम्पदा स्थलहरू कुन कुन हुन्?", "सगरमाथा राष्ट्रिय निकुञ्ज, काठमाडौं उपत्यका, चितवन राष्ट्रिय निकुञ्ज र भगवान् बुद्धको जन्मस्थल लुम्बिनी।"),
 ("नेपालका कुन विश्व सम्पदा स्थल प्राकृतिक हुन्?", "सगरमाथा राष्ट्रिय निकुञ्ज र चितवन राष्ट्रिय निकुञ्ज प्राकृतिक हुन्। काठमाडौं उपत्यका र लुम्बिनी सांस्कृतिक हुन्।"),
 ("काठमाडौं उपत्यका विश्व सम्पदामा के के पर्छन्?", "सात स्मारक क्षेत्र: काठमाडौं, पाटन र भक्तपुरका दरबार क्षेत्र, स्वयम्भू, बौद्ध, पशुपतिनाथ र चाँगुनारायण।"),
 ("लुम्बिनी कहिले विश्व सम्पदामा सूचीकृत भयो?", "लुम्बिनी सन् १९९७ मा सूचीकृत भयो।"),
 ("के काठमाडौं उपत्यका कहिल्यै खतराको सूचीमा परेको थियो?", "थियो, सन् २००३ देखि २००७ सम्म।"),
]

# ---------------- Yeti ----------------
YT_EN_BODY = '''    <section>
      <p class="lede"><strong>No. We found no Government of Nepal decision naming the Yeti a national symbol.</strong> A widely shared 2024 story saying so was an April Fool's joke by a Nepali newspaper.</p>
    </section>

    <section id="hoax">
      <h2>Where the Yeti Story Came From</h2>
      <p>On 1 April 2024 the Himalayan Times published "Yeti - Guardian of the Himalayas to feature on currency notes". It claimed the government had picked the Yeti as a national symbol and would print it on banknotes. The article itself says the newspaper chose the Yeti as the subject of its April Fool joke and the officials and committees it quotes are part of the joke.</p>
      <div class="status warn">
        <b>Treat the claims in that article as fiction.</b> Do not cite it as proof that the Yeti is official. Screenshots of it without the disclaimer keep circulating.
      </div>
      <p class="source">Source: The Himalayan Times, 1 April 2024 (carries an April Fool disclaimer).</p>
    </section>

    <section id="real">
      <h2>What the Official Symbols Actually Are</h2>
      <p>The Constitution of Nepal sets the national flag, anthem, emblem, colour, flower, animal (the cow) and bird (the danphe). The Yeti, a mountain legend, is not among them. See our <a href="/official-vs-unofficial/">official vs unofficial symbols</a> guide for how we separate constitutional symbols from popular ones.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>The Yeti is a legend with no confirmed animal behind it. It is part of Himalayan folklore, not a recognised species.</li>
          <li>Our <a href="/national-animal/">national animal page</a> explains the official animal and the claims around others.</li>
        </ul>
      </div>
    </section>
'''
YT_EN_FAQ = [
 ("Is the Yeti the national animal of Nepal?", "No. Nepal's national animal under the Constitution is the cow. We found no decision naming the Yeti a national symbol."),
 ("Is the Yeti a national symbol of Nepal?", "No official decision was found. A 1 April 2024 Himalayan Times story saying so was an April Fool's joke."),
 ("Will the Yeti appear on Nepal's currency?", "We found no official announcement. The story about Yeti on banknotes came from an April Fool's article."),
 ("What is the Yeti?", "The Yeti is a legendary creature of Himalayan folklore. There is no confirmed animal behind it."),
]
YT_NE_BODY = '''    <section>
      <p class="lede"><strong>होइन। येती नेपालको राष्ट्रिय चिन्ह तोकिएको नेपाल सरकारको कुनै निर्णय हामीले भेटेनौं।</strong> सन् २०२४ मा व्यापक रूपमा सेयर भएको यस्तो खबर नेपालकै एक पत्रिकाको अप्रिल फुल मजाक थियो।</p>
    </section>

    <section id="hoax">
      <h2>येतीको खबर कहाँबाट आयो?</h2>
      <p>सन् २०२४ अप्रिल १ मा हिमालयन टाइम्सले "Yeti - Guardian of the Himalayas to feature on currency notes" प्रकाशित गर्‍यो। सरकारले येतीलाई राष्ट्रिय चिन्ह चयन गरेको र नोटमा छाप्ने भनिएको थियो। लेखमै पत्रिकाले येतीलाई अप्रिल फुल मजाकको विषय बनाएको उल्लेख छ।</p>
      <div class="status warn">
        <b>त्यस लेखका दाबीलाई काल्पनिक ठान्नुहोस्।</b> येती आधिकारिक हो भन्ने प्रमाणका रूपमा यसलाई उद्धृत नगर्नुहोस्। सूचना (डिस्क्लेमर) बिना यसका स्क्रिनसट अझै घुमिरहन्छन्।
      </div>
      <p class="source">स्रोत: हिमालयन टाइम्स, १ अप्रिल २०२४ (अप्रिल फुल सूचनासहित)।</p>
    </section>

    <section id="real">
      <h2>आधिकारिक चिन्ह कुन कुन हुन्?</h2>
      <p>नेपालको संविधानले राष्ट्रिय झण्डा, राष्ट्रगान, प्रतीक चिन्ह, रङ, फूल, पशु (गाई) र चरा (डाँफे) तोकेको छ। हिमालको दन्त्यकथा येती तीमध्ये पर्दैन। संवैधानिक र लोकप्रिय चिन्ह कसरी छुट्याउँछौं भन्ने बुझ्न <a href="/ne/official-vs-unofficial/">आधिकारिक कि परम्परागत</a> पृष्ठ हेर्नुहोस्।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाह छ?</h3>
        <ul>
          <li>येती हिमाली लोककथाको पात्र हो, पुष्टि भएको कुनै जनावर होइन।</li>
          <li>आधिकारिक पशु र अरूबारेका दाबीका लागि <a href="/ne/national-animal/">राष्ट्रिय पशु पृष्ठ</a> हेर्नुहोस्।</li>
        </ul>
      </div>
    </section>
'''
YT_NE_FAQ = [
 ("के येती नेपालको राष्ट्रिय पशु हो?", "होइन। संविधानअनुसार नेपालको राष्ट्रिय पशु गाई हो। येतीलाई राष्ट्रिय चिन्ह तोकिएको कुनै निर्णय हामीले भेटेनौं।"),
 ("के येती नेपालको राष्ट्रिय चिन्ह हो?", "आधिकारिक निर्णय भेटिएन। सन् २०२४ अप्रिल १ को हिमालयन टाइम्सको यस्तो खबर अप्रिल फुल मजाक थियो।"),
 ("के नेपालको नोटमा येती छापिन्छ?", "कुनै आधिकारिक घोषणा भेटिएन। नोटमा येती छापिने खबर अप्रिल फुलको लेखबाट आएको हो।"),
 ("येती भनेको के हो?", "येती हिमाली लोककथाको दन्त्य प्राणी हो। यसको पछाडि पुष्टि भएको कुनै जनावर छैन।"),
]

def _en(title, desc, ogt, ogd, ld, crumb, alt, eyebrow, h1, hero, tags, facts, pron, body, faq, rel_, relp):
    return dict(title=title, desc=desc, og_title=ogt, og_desc=ogd, ld_desc=ld, itemlist_desc='', crumb=crumb, img_alt=alt, img_caption=alt,
                eyebrow=eyebrow, h1=h1, hero=hero, tags=tags, caption=alt, facts=facts, pron=pron, body=body, faq=faq,
                related=rel('en', rel_) + [(S + '/', 'All national symbols of Nepal →')], related_p=relp)
def _ne(title, desc, ogt, ogd, ld, crumb, alt, eyebrow, h1, hero, tags, facts, pron, body, faq, rel_, relp):
    return dict(title=title, desc=desc, og_title=ogt, og_desc=ogd, ld_desc=ld, itemlist_desc='', crumb=crumb, img_alt=alt, img_caption=alt,
                eyebrow=eyebrow, h1=h1, hero=hero, tags=tags, caption=alt, facts=facts, pron=pron, body=body, faq=faq,
                related=rel('ne', rel_) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p=relp)

EXTRA_PAGES = EXTRA_PAGES + [
 _mk('national-poet', 'national_language_of_nepal.webp', 'Madhav Prasad Ghimire', 'https://en.wikipedia.org/wiki/Madhav_Prasad_Ghimire',
  _en('National Poet of Nepal: Madhav Prasad Ghimire (Rastra Kavi)',
      "Nepal's national poet (Rastra Kavi) is Madhav Prasad Ghimire (1919-2020). Who he was, his best-known works and why the title is honorary, not constitutional.",
      'National Poet of Nepal: Madhav Prasad Ghimire', 'Madhav Prasad Ghimire is the Rastra Kavi (national poet) of Nepal. Life, works and the status of the title.',
      "Nepal's national poet Madhav Prasad Ghimire (Rastra Kavi): life, works and the honorary status of the title.", 'National Poet',
      'Nepali literature and the Nepali language', 'National Poet', 'National Poet <em>of Nepal</em>',
      "<strong>Nepal's national poet (Rastra Kavi) is Madhav Prasad Ghimire (1919-2020).</strong> The title is an honour from the government, not a constitutional symbol.",
      ['Rastra Kavi', '1919-2020', 'Honorary title'],
      [('Poet', 'Madhav Prasad Ghimire', False), ('Title', 'Rastra Kavi (राष्ट्रकवि)', False), ('Conferred', '2003 (per Kathmandu Post)', False), ('Born', '23 Sep 1919, Lamjung', False), ('Died', '18 Aug 2020, aged 101', False), ('Status', 'Honorary, not constitutional', False)],
      ('राष्ट्रकवि', 'Rastra Kavi', 'raash-tra ka-vi'), MP_EN_BODY, MP_EN_FAQ, REL_MP, 'The national poet is an honour, separate from the official symbols.'),
  _ne('नेपालका राष्ट्रकवि: माधवप्रसाद घिमिरे को हुन्?',
      'नेपालका राष्ट्रकवि माधवप्रसाद घिमिरे (१९१९-२०२०) हुन्। उनको परिचय, प्रमुख कृति र किन यो मानार्थ उपाधि हो, संवैधानिक होइन।',
      'नेपालका राष्ट्रकवि: माधवप्रसाद घिमिरे', 'माधवप्रसाद घिमिरे नेपालका राष्ट्रकवि हुन्। जीवन, कृति र उपाधिको स्थिति।',
      'नेपालका राष्ट्रकवि माधवप्रसाद घिमिरे: जीवन, कृति र उपाधिको मानार्थ स्थिति।', 'राष्ट्रकवि',
      'नेपाली साहित्य र नेपाली भाषा', 'राष्ट्रकवि', 'नेपालका <em>राष्ट्रकवि</em>',
      '<strong>नेपालका राष्ट्रकवि माधवप्रसाद घिमिरे (१९१९-२०२०) हुन्।</strong> यो सरकारले दिने सम्मान हो, संवैधानिक चिन्ह होइन।',
      ['राष्ट्रकवि', '१९१९-२०२०', 'मानार्थ उपाधि'],
      [('कवि', 'माधवप्रसाद घिमिरे', False), ('उपाधि', 'राष्ट्रकवि', False), ('प्रदान', '२००३ (काठमाडौं पोस्टअनुसार)', False), ('जन्म', '२३ सेप्टेम्बर १९१९, लमजुङ', False), ('निधन', '१८ अगस्ट २०२०, १०१ वर्षमा', False), ('स्थिति', 'मानार्थ, संवैधानिक होइन', False)],
      ('राष्ट्रकवि', 'Rastra Kavi', 'राष्ट्रकवि'), MP_NE_BODY, MP_NE_FAQ, REL_MP_NE, 'राष्ट्रकवि आधिकारिक चिन्हहरूभन्दा फरक सम्मान हो।')),
 _mk('world-heritage-sites', 'national_everest_of_nepal.webp', 'World Heritage Sites of Nepal', 'https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Nepal',
  _en('World Heritage Sites of Nepal: All 4 UNESCO Sites and Years',
      'Nepal has 4 UNESCO World Heritage Sites: Sagarmatha National Park, Kathmandu Valley, Chitwan National Park and Lumbini. Types, years inscribed and what each includes.',
      'World Heritage Sites of Nepal: All 4 UNESCO Sites', 'The 4 UNESCO World Heritage Sites of Nepal with type, year inscribed and what the Kathmandu Valley listing includes.',
      'The four UNESCO World Heritage Sites of Nepal: Sagarmatha, Kathmandu Valley, Chitwan and Lumbini.', 'World Heritage Sites',
      'Mount Everest and the Himalaya in Sagarmatha National Park', 'World Heritage', 'World Heritage Sites <em>of Nepal</em>',
      '<strong>Nepal has four UNESCO World Heritage Sites: Sagarmatha National Park, Kathmandu Valley, Chitwan National Park and Lumbini.</strong>',
      ['4 sites', '2 natural', '2 cultural'],
      [('Total', '4 UNESCO sites', False), ('Natural', 'Sagarmatha NP (1979), Chitwan NP (1984)', False), ('Cultural', 'Kathmandu Valley (1979), Lumbini (1997)', False), ('Valley zones', '7 monument zones', False), ('Danger list', 'Kathmandu Valley, 2003-2007', False)],
      ('विश्व सम्पदा स्थल', 'Biswa Sampada Sthal', 'bish-wa sam-pa-da sthal'), WH_EN_BODY, WH_EN_FAQ, REL_WH, 'World Heritage listing is by UNESCO, separate from the official national symbols.'),
  _ne('नेपालका विश्व सम्पदा स्थल: युनेस्कोका सबै ४ स्थल र साल',
      'नेपालमा युनेस्कोका ४ विश्व सम्पदा स्थल छन्: सगरमाथा राष्ट्रिय निकुञ्ज, काठमाडौं उपत्यका, चितवन राष्ट्रिय निकुञ्ज र लुम्बिनी। प्रकार, साल र के के पर्छन्।',
      'नेपालका विश्व सम्पदा स्थल: युनेस्कोका सबै ४', 'नेपालका ४ युनेस्को विश्व सम्पदा स्थल, प्रकार, सूचीकृत साल र काठमाडौं उपत्यकामा के के पर्छन्।',
      'नेपालका चार युनेस्को विश्व सम्पदा स्थल: सगरमाथा, काठमाडौं उपत्यका, चितवन र लुम्बिनी।', 'विश्व सम्पदा स्थल',
      'सगरमाथा राष्ट्रिय निकुञ्जमा सगरमाथा र हिमालय', 'विश्व सम्पदा', 'नेपालका <em>विश्व सम्पदा स्थल</em>',
      '<strong>नेपालमा युनेस्कोका चारवटा विश्व सम्पदा स्थल छन्: सगरमाथा राष्ट्रिय निकुञ्ज, काठमाडौं उपत्यका, चितवन राष्ट्रिय निकुञ्ज र लुम्बिनी।</strong>',
      ['४ स्थल', '२ प्राकृतिक', '२ सांस्कृतिक'],
      [('जम्मा', '४ युनेस्को स्थल', False), ('प्राकृतिक', 'सगरमाथा निकुञ्ज (१९७९), चितवन निकुञ्ज (१९८४)', False), ('सांस्कृतिक', 'काठमाडौं उपत्यका (१९७९), लुम्बिनी (१९९७)', False), ('उपत्यकाका क्षेत्र', '७ स्मारक क्षेत्र', False), ('खतराको सूची', 'काठमाडौं उपत्यका, २००३-२००७', False)],
      ('विश्व सम्पदा स्थल', 'Biswa Sampada Sthal', 'विश्व सम्पदा स्थल'), WH_NE_BODY, WH_NE_FAQ, REL_WH_NE, 'विश्व सम्पदा सूचीकरण युनेस्कोले गर्छ, आधिकारिक राष्ट्रिय चिन्हभन्दा फरक हो।')),
 _mk('is-yeti-national-symbol', 'national_everest_of_nepal.webp', 'Yeti', 'https://en.wikipedia.org/wiki/Yeti',
  _en('Is the Yeti a National Symbol of Nepal? No: The 2024 Hoax Explained',
      'Is the Yeti a national symbol or national animal of Nepal? No official decision exists. The 2024 story about Yeti on banknotes was an April Fool joke.',
      'Is the Yeti a National Symbol of Nepal?', 'No. The 2024 story naming the Yeti a national symbol was an April Fool joke. What the official symbols are.',
      'Why the Yeti is not a national symbol of Nepal: the 1 April 2024 hoax and the real official symbols.', 'Is the Yeti a National Symbol?',
      'Himalayan peaks where the Yeti legend is set', 'Myth check', 'Is the Yeti <em>a National Symbol?</em>',
      '<strong>No. The Yeti is not a national symbol or national animal of Nepal.</strong> The 2024 story saying so was an April Fool joke.',
      ['Not official', 'April Fool 2024', 'Folklore'],
      [('Official?', 'No decision found', False), ('Origin of claim', 'Himalayan Times, 1 Apr 2024', False), ('Article status', 'April Fool joke', False), ('National animal', 'Cow (Constitution)', False), ('National bird', 'Danphe (Constitution)', False)],
      ('येती', 'Yeti', 'ye-ti'), YT_EN_BODY, YT_EN_FAQ, REL_YT, 'The Yeti is folklore. The official symbols are set by the Constitution.'),
  _ne('के येती नेपालको राष्ट्रिय चिन्ह हो? होइन: २०२४ को अप्रिल फुल',
      'येती नेपालको राष्ट्रिय चिन्ह वा राष्ट्रिय पशु हो? आधिकारिक निर्णय छैन। नोटमा येती छापिने २०२४ को खबर अप्रिल फुल मजाक थियो।',
      'के येती नेपालको राष्ट्रिय चिन्ह हो?', 'होइन। येतीलाई राष्ट्रिय चिन्ह बनाइएको भन्ने २०२४ को खबर अप्रिल फुल मजाक थियो। आधिकारिक चिन्ह कुन कुन हुन्?',
      'येती किन नेपालको राष्ट्रिय चिन्ह होइन: १ अप्रिल २०२४ को मजाक र वास्तविक आधिकारिक चिन्ह।', 'के येती राष्ट्रिय चिन्ह हो?',
      'येतीको दन्त्यकथा जोडिएका हिमाली शिखरहरू', 'तथ्य जाँच', 'के येती <em>राष्ट्रिय चिन्ह हो?</em>',
      '<strong>होइन। येती नेपालको राष्ट्रिय चिन्ह वा राष्ट्रिय पशु होइन।</strong> त्यस्तो भन्ने २०२४ को खबर अप्रिल फुल मजाक थियो।',
      ['आधिकारिक होइन', 'अप्रिल फुल २०२४', 'लोककथा'],
      [('आधिकारिक?', 'निर्णय भेटिएन', False), ('दाबीको स्रोत', 'हिमालयन टाइम्स, १ अप्रिल २०२४', False), ('लेखको स्थिति', 'अप्रिल फुल मजाक', False), ('राष्ट्रिय पशु', 'गाई (संविधान)', False), ('राष्ट्रिय चरा', 'डाँफे (संविधान)', False)],
      ('येती', 'Yeti', 'येती'), YT_NE_BODY, YT_NE_FAQ, REL_YT_NE, 'येती लोककथा हो। आधिकारिक चिन्ह संविधानले तोकेको हो।')),
]
