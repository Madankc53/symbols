# -*- coding: utf-8 -*-
S = 'https://symbols.thenepal.io'
def rel(lang, items):
    pre = S + ('/ne' if lang == 'ne' else '')
    return [(pre + '/' + s + '/', n) for s, n in items]

# ---------------------------------------------------------------- FRUIT
FRUIT_EN_BODY = '''    <section>
      <p class="lede">Every autumn, the terraced hills of Nepal turn gold with citrus. On 12 April 2024 (30 Chaitra 2080 BS) the Council of Ministers recognised the orange as Nepal's national fruit, with the orange most people picture first being the sweet-sour <em>suntala</em>, or mandarin. This page explains what was decided, what is still unclear, and why this fruit fits the country so well.</p>
    </section>

    <section id="status">
      <h2>What Was Officially Decided</h2>
      <div class="status">
        <b>Confirmed.</b> Rising Nepal reported on 12 April 2024 that the Council of Ministers "decided to recognize orange as the national fruit," announced by Government Spokesperson and Communications Minister Rekha Sharma. The Ministry of Agriculture and Livestock Development brought the proposal, which followed a submission from the National Agriculture Genetic Resources Center (Genebank).
      </div>
      <div class="status warn">
        <b>Not confirmed.</b> The news report says only "orange". We have not seen the cabinet decision text, so we cannot say which species it names. The fruit is widely discussed as the mandarin orange (<em>suntala</em>, <em>Citrus reticulata</em>); see the naming note below.
      </div>
      <ol class="tl">
        <li><b>2023</b>Genebank submits its research on orange to the Ministry of Agriculture and Livestock Development.</li>
        <li><b>12 April 2024 (30 Chaitra 2080)</b>Council of Ministers recognises orange as the national fruit.</li>
        <li><b>Announced the same day</b>Minister Rekha Sharma shares the decision at the press briefing after the cabinet meeting.</li>
      </ol>
      <p class="source">Source: Rising Nepal, "Orange declared as national fruit" (12 April 2024). The 2023 submission date comes from a secondary blog source and is not independently confirmed.</p>
    </section>

    <section id="naming">
      <h2>A Note on Naming: Suntala vs. Junar</h2>
      <div class="callout">
        <strong>Two different oranges.</strong> In Nepali usage, <em>suntala</em> (सुन्तला) normally means the mandarin orange (<em>Citrus reticulata</em>), a loose-skinned, easy-to-peel fruit, while <em>junar</em> (जुनार) is the sweet orange (<em>Citrus sinensis</em>). Sindhuli district is best known for junar; the eastern hills, including Dhankuta, are known for mandarin. Because news reports say only "orange", this guide treats the suntala as the main subject while noting that junar belongs to the same citrus family and is often mentioned alongside it.
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Nepali name</th><th>English</th><th>Scientific name</th></tr></thead>
          <tbody>
            <tr><td>सुन्तला (Suntala)</td><td>Mandarin orange</td><td>Citrus reticulata</td></tr>
            <tr><td>जुनार (Junar)</td><td>Sweet orange</td><td>Citrus sinensis</td></tr>
            <tr><td>कागती (Kagati)</td><td>Lime</td><td>Citrus aurantiifolia</td></tr>
            <tr><td>भोगटे (Bhogate)</td><td>Pomelo</td><td>Citrus maxima</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: Nepal Horticulture Society, "Development and Outlook of Citrus Industry in Nepal" (which calls suntala an indigenous fruit of Nepal); Kathmandu Post and Nepal Horticulture Society reports on Sindhuli sweet orange</p>
    </section>

    <section id="where">
      <h2>Where It Grows</h2>
      <p>Citrus is a fruit of Nepal's mid-hills, where steep south-facing slopes, mild winters and good drainage suit the trees. Orchards are small family plots more often than large estates, which is why the harvest matters so much to rural households.</p>
      <div class="chips"><span>Eastern hills (Dhankuta and neighbours)</span><span>Sindhuli (sweet orange)</span><span>Other mid-hill districts</span></div>
      <p>For exact area and production by province and district, use the latest Ministry of Agriculture and Livestock Development statistics. We do not repeat figures here because published numbers differ by year and source.</p>
    </section>

    <section id="season">
      <h2>Season and Everyday Use</h2>
      <p>Mandarins ripen from autumn into winter, so the harvest arrives around Dashain and Tihar, when fruit is part of offerings and festival tables. Exact timing depends on altitude and variety. Oranges are eaten fresh or pressed for juice,.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>As far as we could confirm, Nepal had no officially recognised national fruit before April 2024.</li>
          <li>The Nepal Horticulture Society describes the suntala as an indigenous fruit of Nepal.</li>
          <li>Citrus fruits are a well-known source of vitamin C, one reason oranges are popular in the cold season.</li>
        </ul>
      </div>
    </section>

    <section id="why">
      <h2>Why the Orange Fits</h2>
      <p><b>Geography.</b> It thrives in the same mid-hill belt where most Nepalis live and farm. <b>Livelihood.</b> Citrus is a cash crop for many hill families. <b>Culture.</b> Its season matches the festival calendar. <b>Identity.</b> Unlike many imports, it is a fruit people associate directly with Nepali hill orchards.</p>
      <p class="source">Source: explanatory summary; the official reasons were not published in the sources we reviewed</p>
    </section>
'''

FRUIT_EN_FAQ = [
 ("What is the national fruit of Nepal?", "The Council of Ministers recognised the orange as Nepal's national fruit on 12 April 2024 (30 Chaitra 2080 BS). The fruit is widely discussed as the mandarin orange, the suntala."),
 ("When was the national fruit declared?", "On 12 April 2024, announced by Government Spokesperson and Communications Minister Rekha Sharma after a cabinet meeting."),
 ("Is the national fruit suntala or junar?", "News reports say only \"orange\". In Nepali usage suntala is the mandarin (Citrus reticulata) and junar is the sweet orange (Citrus sinensis). We have not seen the cabinet text, so we cannot say which species it names."),
 ("Did Nepal have a national fruit before 2024?", "We could not find an earlier official designation, so 2024 appears to be the first."),
 ("Who proposed the orange?", "The Ministry of Agriculture and Livestock Development presented the proposal, which followed research submitted by the National Agriculture Genetic Resources Center (Genebank)."),
 ("Where is orange grown in Nepal?", "Mainly in the mid-hills, with mandarin well known in the eastern hills and sweet orange (junar) associated with Sindhuli."),
 ("What is the scientific name of the suntala?", "Citrus reticulata, the mandarin orange, in the family Rutaceae."),
]

FRUIT_NE_BODY = '''    <section>
      <p class="lede">हरेक शरद ऋतुमा नेपालका पाखा सुन्तलाले सुनौलो बन्छन्। २०८० चैत ३० (सन् २०२४ अप्रिल १२) मा मन्त्रिपरिषद्ले सुन्तलालाई नेपालको राष्ट्रिय फल घोषणा गर्‍यो। यस पृष्ठले के निर्णय भयो, के अझै स्पष्ट छैन र यो फल देशसँग किन मिल्छ भन्ने कुरा बुझाउँछ।</p>
    </section>

    <section id="status">
      <h2>आधिकारिक रूपमा के निर्णय भयो</h2>
      <div class="status">
        <b>पुष्टि भएको।</b> राइजिङ नेपालले २०२४ अप्रिल १२ मा "मन्त्रिपरिषद्ले सुन्तलालाई राष्ट्रिय फलका रूपमा मान्यता दिने निर्णय गर्‍यो" भनी समाचार दियो। सरकारका प्रवक्ता तथा सञ्चारमन्त्री रेखा शर्माले निर्णय सार्वजनिक गरिन्। कृषि तथा पशुपन्छी विकास मन्त्रालयले प्रस्ताव ल्यायो, जुन राष्ट्रिय कृषि आनुवंशिक स्रोत केन्द्र (जीन बैंक) को सिफारिसपछि आएको थियो।
      </div>
      <div class="status warn">
        <b>पुष्टि नभएको।</b> समाचारमा "सुन्तला (orange)" मात्र उल्लेख छ। हामीले मन्त्रिपरिषद्को निर्णयको पाठ हेरेका छैनौं, त्यसैले कुन प्रजाति तोकिएको हो भन्न सक्दैनौं। यो फललाई सामान्यतया सुन्तला (<em>Citrus reticulata</em>) भनेर चर्चा गरिन्छ; तल नामको टिप्पणी हेर्नुहोस्।
      </div>
      <ol class="tl">
        <li><b>२०२३</b>जीन बैंकले सुन्तलासम्बन्धी अध्ययन कृषि तथा पशुपन्छी विकास मन्त्रालयमा पठायो।</li>
        <li><b>२०८० चैत ३० (२०२४ अप्रिल १२)</b>मन्त्रिपरिषद्ले सुन्तलालाई राष्ट्रिय फलका रूपमा मान्यता दियो।</li>
        <li><b>सोही दिन सार्वजनिक</b>मन्त्रिपरिषद् बैठकपछि मन्त्री रेखा शर्माले निर्णय जानकारी गराइन्।</li>
      </ol>
      <p class="source">स्रोत: राइजिङ नेपाल, "Orange declared as national fruit" (२०२४ अप्रिल १२)। २०२३ को प्रस्ताव मितिको कुरा एउटा अप्रत्यक्ष ब्लग स्रोतबाट लिइएको हो र स्वतन्त्र रूपमा पुष्टि भएको छैन।</p>
    </section>

    <section id="naming">
      <h2>नामसम्बन्धी टिप्पणी: सुन्तला बनाम जुनार</h2>
      <div class="callout">
        <strong>दुई फरक फल।</strong> नेपाली प्रयोगमा <em>सुन्तला</em> भनेको सजिलै बोक्रा निकाल्न मिल्ने मन्डारिन (<em>Citrus reticulata</em>) हो भने <em>जुनार</em> मिठो सुन्तला (<em>Citrus sinensis</em>) हो। सिन्धुली जुनारका लागि चर्चित छ; पूर्वी पहाड (धनकुटासहित) मा सुन्तला बढी चिनिन्छ। समाचारमा "orange" मात्र लेखिएकाले यो गाइडले सुन्तलालाई मुख्य विषय मानेको छ, र जुनार पनि सोही फल-परिवारको भएकाले साथमा उल्लेख गरेको छ।
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>नेपाली नाम</th><th>अङ्ग्रेजी</th><th>वैज्ञानिक नाम</th></tr></thead>
          <tbody>
            <tr><td>सुन्तला</td><td>Mandarin orange</td><td>Citrus reticulata</td></tr>
            <tr><td>जुनार</td><td>Sweet orange</td><td>Citrus sinensis</td></tr>
            <tr><td>कागती</td><td>Lime</td><td>Citrus aurantiifolia</td></tr>
            <tr><td>भोगटे</td><td>Pomelo</td><td>Citrus maxima</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: नेपाल हर्टिकल्चर सोसाइटी, "Development and Outlook of Citrus Industry in Nepal" (जसले सुन्तलालाई नेपालको आदिवासी फल भनेको छ); सिन्धुलीको जुनारबारे काठमाडौँ पोस्ट र नेपाल हर्टिकल्चर सोसाइटीका प्रतिवेदन</p>
    </section>

    <section id="where">
      <h2>कहाँ फल्छ</h2>
      <p>सुन्तला जातका फल नेपालको मध्य पहाडका फल हुन्, जहाँ घाम लाग्ने भिरालो पाखा, सौम्य जाडो र राम्रो निकास यिनका लागि उपयुक्त हुन्छन्। बगैँचा ठूला फार्मभन्दा साना पारिवारिक जग्गामा बढी हुन्छन्, त्यसैले ग्रामीण परिवारका लागि यसको बाली निकै महत्त्वपूर्ण छ।</p>
      <div class="chips"><span>पूर्वी पहाड (धनकुटा र आसपास)</span><span>सिन्धुली (जुनार)</span><span>अन्य मध्य पहाडी जिल्ला</span></div>
      <p>प्रदेश र जिल्लाअनुसार क्षेत्रफल तथा उत्पादनको ठ्याक्कै तथ्याङ्कका लागि कृषि तथा पशुपन्छी विकास मन्त्रालयको पछिल्लो तथ्याङ्क हेर्नुहोस्। प्रकाशित सङ्ख्या वर्ष र स्रोतअनुसार फरक पर्ने भएकाले हामीले यहाँ आँकडा दोहोर्‍याएका छैनौं।</p>
    </section>

    <section id="season">
      <h2>मौसम र दैनिक प्रयोग</h2>
      <p>सुन्तला शरद ऋतुदेखि जाडोसम्म पाक्छ, त्यसैले दशैं र तिहारताका फल पूजा र चाडपर्वका थालमा देखिन्छ। ठ्याक्कै समय उचाइ र जातअनुसार फरक पर्छ। सुन्तला ताजै खाइन्छ वा जुस बनाइन्छ।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाहा छ?</h3>
        <ul>
          <li>हामीले पुष्टि गर्न सकेसम्म, सन् २०२४ अप्रिलअघि नेपालको आधिकारिक रूपमा मान्यता पाएको राष्ट्रिय फल थिएन।</li>
          <li>नेपाल हर्टिकल्चर सोसाइटीले सुन्तलालाई नेपालको आदिवासी फल भनेको छ।</li>
          <li>सुन्तला जातका फल भिटामिन सीका राम्रा स्रोत मानिन्छन्, जाडोमा यिनको लोकप्रियताको एउटा कारण यही हो।</li>
        </ul>
      </div>
    </section>

    <section id="why">
      <h2>सुन्तला किन मिल्छ</h2>
      <p><b>भूगोल।</b> धेरैजसो नेपालीले बसोबास र खेती गर्ने मध्य पहाडी पेटीमै यो फल्छ। <b>जीविका।</b> धेरै पहाडी परिवारका लागि यो नगदे बाली हो। <b>संस्कृति।</b> यसको मौसम चाडपर्वको पात्रोसँग मिल्छ। <b>पहिचान।</b> आयातित फलभन्दा फरक, मानिसले यसलाई सिधै नेपाली पहाडी बगैँचासँग जोड्छन्।</p>
      <p class="source">स्रोत: व्याख्यात्मक सारांश; हामीले हेरेका स्रोतमा आधिकारिक कारणहरू प्रकाशित थिएनन्</p>
    </section>
'''

FRUIT_NE_FAQ = [
 ("नेपालको राष्ट्रिय फल कुन हो?", "मन्त्रिपरिषद्ले २०८० चैत ३० (२०२४ अप्रिल १२) मा सुन्तला (orange) लाई नेपालको राष्ट्रिय फलका रूपमा मान्यता दियो। यो फललाई सामान्यतया सुन्तला (मन्डारिन) भनेर चर्चा गरिन्छ।"),
 ("राष्ट्रिय फल कहिले घोषणा भयो?", "२०२४ अप्रिल १२ (२०८० चैत ३०) मा मन्त्रिपरिषद् बैठकपछि सरकारी प्रवक्ता तथा सञ्चारमन्त्री रेखा शर्माले घोषणा गरिन्।"),
 ("राष्ट्रिय फल सुन्तला हो कि जुनार?", "समाचारमा \"orange\" मात्र लेखिएको छ। नेपाली प्रयोगमा सुन्तला भनेको मन्डारिन (Citrus reticulata) र जुनार भनेको मिठो सुन्तला (Citrus sinensis) हो। हामीले निर्णयको पाठ हेरेका छैनौं, त्यसैले कुन प्रजाति तोकिएको हो भन्न सक्दैनौं।"),
 ("२०२४ अघि नेपालको राष्ट्रिय फल थियो?", "हामीले यसअघिको आधिकारिक घोषणा फेला पारेनौं, त्यसैले २०२४ पहिलो जस्तो देखिन्छ।"),
 ("सुन्तलाको प्रस्ताव कसले ल्यायो?", "कृषि तथा पशुपन्छी विकास मन्त्रालयले प्रस्ताव प्रस्तुत गर्‍यो, जुन राष्ट्रिय कृषि आनुवंशिक स्रोत केन्द्र (जीन बैंक) ले पठाएको अध्ययनपछि आएको थियो।"),
 ("नेपालमा सुन्तला कहाँ फल्छ?", "मुख्यतया मध्य पहाडमा; पूर्वी पहाडमा सुन्तला र सिन्धुलीमा जुनार चर्चित छन्।"),
 ("सुन्तलाको वैज्ञानिक नाम के हो?", "Citrus reticulata, अर्थात् मन्डारिन सुन्तला, Rutaceae परिवारको।"),
]

# ---------------------------------------------------------------- FOOD
FOOD_EN_BODY = '''    <section>
      <p class="lede">Ask almost anyone in Nepal what they ate today and the answer is probably dal bhat: rice, lentil soup and seasonal vegetables, usually with a pickle on the side. It is eaten in homes, trekking lodges and offices alike, which is why it is so often called Nepal's national dish, even though no government decision names it.</p>
    </section>

    <section id="status">
      <h2>Is There an Official National Food?</h2>
      <div class="status warn">
        <b>No official designation confirmed.</b> We could not find a Government of Nepal declaration of a national dish. Dal bhat is the staple meal eaten across the country and is the answer most often given. Dhindo, a millet or buckwheat porridge, is also called a national dish in some sources, especially in hill and mountain communities.
      </div>
      <p class="source">Source: Wikipedia, "Nepalese cuisine" and "Dal bhat" (which describe dal bhat as the standard meal of Nepal and dhindo as called the national dish); no government source found</p>
    </section>

    <section id="thali">
      <h2>Anatomy of a Dal Bhat Plate</h2>
      <p>A plate of dal bhat is a set of parts that work together. Exact items change with region, season and family.</p>
      <div class="thali">
        <div><span class="ic">🍚</span><b>Bhat (भात)</b><small>Steamed rice. In some areas another grain such as maize or millet is eaten instead.</small></div>
        <div><span class="ic">🥣</span><b>Dal (दाल)</b><small>Spiced lentil soup, often tempered with ghee or oil and spices. Jimbu, a Himalayan herb, is a classic flavour.</small></div>
        <div><span class="ic">🥬</span><b>Tarkari (तरकारी)</b><small>Seasonal vegetable curry, from potato and cauliflower to greens.</small></div>
        <div><span class="ic">🌶️</span><b>Achar (अचार)</b><small>Pickle or fresh chutney, such as tomato or radish achar.</small></div>
        <div><span class="ic">🍋</span><b>Extras</b><small>Saag (greens), lime, green chilli, papad, curd, or meat and fish on special days.</small></div>
      </div>
      <p class="source">Source: Wikipedia, "Dal bhat" and "Nepalese cuisine"</p>
    </section>

    <section id="dhindo">
      <h2>Dhindo and Gundruk: The Hill Classic</h2>
      <p>Before rice became common in the hills, many families relied on grains such as millet, maize and buckwheat. Dhindo is a thick porridge stirred from flour and hot water and traditionally eaten with gundruk, a fermented dried-greens pickle, or with a lentil or vegetable side. Dhindo is still a favourite comfort food, especially in colder places.</p>
      <div class="dyk">
        <h3>✦ Did you know?</h3>
        <ul>
          <li>Dal bhat was not the main daily meal in Nepal's hilly and Himalayan regions historically; it spread with rice farming and trade.</li>
          <li>Dal bhat is traditionally eaten twice a day by the Khas people, and many households across Nepal follow the same rhythm.</li>
          <li>Trekkers repeat the saying "Dal Bhat Power 24 Hour" because a plate keeps them going on mountain trails.</li>
        </ul>
      </div>
    </section>

    <section id="regions">
      <h2>One Nation, Many Plates</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Region / community</th><th>Typical foods</th></tr></thead>
          <tbody>
            <tr><td>Himalayan</td><td>Millet or barley dough, potato curry, momo, thukpa, tongba</td></tr>
            <tr><td>Thakali</td><td>Buckwheat, barley and millet dishes; less vegetarian than most hill cooking</td></tr>
            <tr><td>Newar</td><td>Buffalo meat, many fermented dishes, elaborate festival food</td></tr>
            <tr><td>Madhesh / Tharu</td><td>Basmati rice with ghee, pigeon-pea dal, fish and goat curry</td></tr>
            <tr><td>Limbu</td><td>Kinema (fermented soybean), bamboo shoots, millet breads</td></tr>
            <tr><td>Khas</td><td>Dal bhat tarkari, chamre (rice fried in ghee)</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">Source: Wikipedia, "Nepalese cuisine"</p>
    </section>

    <section id="culture">
      <h2>Food, Festival and Hospitality</h2>
      <p>Food in Nepal is tied to the calendar and the family: feast days, rice-feeding ceremonies and weddings each have their own dishes. A guest is rarely sent away without a meal, and dal bhat is the dish that most often fills that role.</p>
    </section>
'''

FOOD_EN_FAQ = [
 ("What is the national food of Nepal?", "No official national food designation could be confirmed. Dal bhat (rice, lentil soup and vegetable curry) is the answer most often given because it is the standard meal across Nepal."),
 ("Is dal bhat the national dish of Nepal?", "It is widely called the national dish, but we found no government declaration. Some sources also call dhindo a national dish."),
 ("What is dal bhat made of?", "Bhat is steamed rice, dal is spiced lentil soup, and tarkari is a vegetable curry, usually with a pickle (achar) and sometimes saag, papad or meat."),
 ("What is dhindo?", "A thick porridge stirred from millet, buckwheat or maize flour and hot water, traditionally eaten with gundruk or lentil and vegetable dishes."),
 ("What does Dal Bhat Power 24 Hour mean?", "It is a popular phrase among trekkers, meaning a plate of dal bhat gives enough energy for a full day on the trail."),
 ("What is gundruk?", "A fermented, dried leafy-greens pickle, often made from mustard greens, used in achar and soups."),
 ("Is momo the national food of Nepal?", "Momo is hugely popular, but it is not officially designated. Dal bhat remains the everyday staple."),
]

FOOD_NE_BODY = '''    <section>
      <p class="lede">नेपालमा जोसँग पनि आज के खायौ भनेर सोध्नुहोस्, उत्तर प्रायः दालभात नै हुन्छ: भात, दाल र मौसमी तरकारी, साथमा अचार। घर, ट्रेकिङ लज र कार्यालय सबैतिर यही खाइन्छ, त्यसैले सरकारी निर्णयले नतोकेको भए पनि यसलाई प्रायः नेपालको राष्ट्रिय परिकार भनिन्छ।</p>
    </section>

    <section id="status">
      <h2>के आधिकारिक राष्ट्रिय खाना छ?</h2>
      <div class="status warn">
        <b>आधिकारिक तोकिएको पुष्टि भएको छैन।</b> राष्ट्रिय परिकार तोकेको नेपाल सरकारको घोषणा हामीले फेला पारेनौं। दालभात देशभर खाइने मुख्य खाना हो र प्रायः यही उत्तर दिइन्छ। कोदो वा फापरको ढिँडोलाई पनि केही स्रोतले राष्ट्रिय परिकार भनेका छन्, विशेषगरी पहाडी र हिमाली समुदायमा।
      </div>
      <p class="source">स्रोत: Wikipedia, "Nepalese cuisine" र "Dal bhat" (जसले दालभातलाई नेपालको सामान्य खाना र ढिँडोलाई राष्ट्रिय परिकार भनिएको बताउँछ); सरकारी स्रोत फेला परेन</p>
    </section>

    <section id="thali">
      <h2>दालभात थालको बनावट</h2>
      <p>दालभातको थाल सँगै मिलेर काम गर्ने भागहरूको समूह हो। ठ्याक्कै परिकारहरू क्षेत्र, मौसम र परिवारअनुसार फरक पर्छन्।</p>
      <div class="thali">
        <div><span class="ic">🍚</span><b>भात</b><small>पकाएको चामल। केही ठाउँमा मकै वा कोदोजस्ता अन्य अन्न खाइन्छ।</small></div>
        <div><span class="ic">🥣</span><b>दाल</b><small>मसला हालेको दाल, प्रायः घ्यू वा तेलमा तारेर बनाइन्छ। जिम्बु हिमाली स्वाद दिने परम्परागत मसला हो।</small></div>
        <div><span class="ic">🥬</span><b>तरकारी</b><small>मौसमी तरकारी, आलु र काउलीदेखि साग सम्म।</small></div>
        <div><span class="ic">🌶️</span><b>अचार</b><small>गोलभेँडा वा मूलाको अचार जस्ता अचार वा ताजा चटनी।</small></div>
        <div><span class="ic">🍋</span><b>थप परिकार</b><small>साग, कागती, हरियो खुर्सानी, पापड, दही, र विशेष दिनमा मासु वा माछा।</small></div>
      </div>
      <p class="source">स्रोत: Wikipedia, "Dal bhat" र "Nepalese cuisine"</p>
    </section>

    <section id="dhindo">
      <h2>ढिँडो र गुन्द्रुक: पहाडको परम्परागत खाना</h2>
      <p>पहाडमा भात सामान्य बन्नुअघि धेरै परिवार कोदो, मकै र फापरजस्ता अन्नमा निर्भर थिए। ढिँडो पिठो र तातो पानी मिलाएर पकाइने बाक्लो परिकार हो, जुन परम्परागत रूपमा गुन्द्रुक (सुकाएर किण्वन गरिएको साग) को अचार वा दाल-तरकारीसँग खाइन्छ। चिसो ठाउँमा ढिँडो अझै मन पराइने खाना हो।</p>
      <div class="dyk">
        <h3>✦ के तपाईंलाई थाहा छ?</h3>
        <ul>
          <li>ऐतिहासिक रूपमा नेपालका पहाडी र हिमाली क्षेत्रमा दालभात दैनिक मुख्य खाना थिएन; धान खेती र व्यापारसँगै यो फैलियो।</li>
          <li>परम्परागत रूपमा खस समुदायमा दालभात दिनमा दुई पटक खाइन्छ, र देशभरका धेरै घरमा यही लय चल्छ।</li>
          <li>ट्रेकरहरू "Dal Bhat Power 24 Hour" भन्ने भनाइ दोहोर्‍याउँछन्, किनभने एक थालले पहाडी बाटोमा दिनभर ऊर्जा दिन्छ।</li>
        </ul>
      </div>
    </section>

    <section id="regions">
      <h2>एउटै देश, थुप्रै थाल</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>क्षेत्र / समुदाय</th><th>सामान्य परिकार</th></tr></thead>
          <tbody>
            <tr><td>हिमाली</td><td>कोदो वा जौको ढिँडो, आलुको तरकारी, मःमः, थुक्पा, तोङ्बा</td></tr>
            <tr><td>थकाली</td><td>फापर, जौ र कोदोका परिकार; सामान्य पहाडी खानाभन्दा कम शाकाहारी</td></tr>
            <tr><td>नेवार</td><td>भैँसीको मासु, धेरै किण्वित परिकार, भव्य चाडपर्वका खाना</td></tr>
            <tr><td>मधेश / थारु</td><td>घ्यूसहित बासमती चामल, रहरको दाल, माछा र खसीको तरकारी</td></tr>
            <tr><td>लिम्बु</td><td>किनेमा (किण्वित सोयाबिन), तामा (बाँसको मुन्टा), कोदोका रोटी</td></tr>
            <tr><td>खस</td><td>दालभात तरकारी, चम्रे (घ्यूमा भुटेको भात)</td></tr>
          </tbody>
        </table>
      </div>
      <p class="source">स्रोत: Wikipedia, "Nepalese cuisine"</p>
    </section>

    <section id="culture">
      <h2>खाना, चाडपर्व र आतिथ्य</h2>
      <p>नेपालमा खाना पात्रो र परिवारसँग जोडिएको छ: चाडपर्व, पासनी र विवाहका आ-आफ्नै परिकार हुन्छन्। पाहुनालाई खाना नखुवाई पठाउने चलन कमै छ, र त्यो भूमिका प्रायः दालभातले नै निभाउँछ।</p>
    </section>
'''

FOOD_NE_FAQ = [
 ("नेपालको राष्ट्रिय खाना कुन हो?", "आधिकारिक राष्ट्रिय खाना तोकिएको पुष्टि भएको छैन। दालभात (भात, दाल र तरकारी) देशभर खाइने सामान्य खाना भएकाले प्रायः यही उत्तर दिइन्छ।"),
 ("दालभात नेपालको राष्ट्रिय परिकार हो?", "यसलाई व्यापक रूपमा राष्ट्रिय परिकार भनिन्छ, तर हामीले सरकारी घोषणा फेला पारेनौं। केही स्रोतले ढिँडोलाई पनि राष्ट्रिय परिकार भनेका छन्।"),
 ("दालभात केकेबाट बन्छ?", "भात पकाएको चामल हो, दाल मसला हालेको दाल हो, र तरकारी मौसमी तरकारी हो; साथमा प्रायः अचार र कहिलेकाहीँ साग, पापड वा मासु हुन्छ।"),
 ("ढिँडो भनेको के हो?", "कोदो, फापर वा मकैको पिठो र तातो पानीले हल्लाएर बनाइने बाक्लो परिकार, जुन परम्परागत रूपमा गुन्द्रुक वा दाल-तरकारीसँग खाइन्छ।"),
 ("Dal Bhat Power 24 Hour को अर्थ के हो?", "यो ट्रेकरहरूमा लोकप्रिय भनाइ हो, जसको अर्थ एक थाल दालभातले पदयात्रामा दिनभरिलाई पुग्ने ऊर्जा दिन्छ।"),
 ("गुन्द्रुक भनेको के हो?", "सुकाएर किण्वन गरिएको पातेसाग, प्रायः तोरीको सागबाट बनाइने, जुन अचार र सुपमा प्रयोग गरिन्छ।"),
 ("के मःमः नेपालको राष्ट्रिय खाना हो?", "मःमः निकै लोकप्रिय छ, तर आधिकारिक रूपमा तोकिएको छैन। दालभात नै दैनिक मुख्य खाना हो।"),
]

REL_FRUIT = [('national-flower', 'Rhododendron — National Flower'), ('national-tree', 'Peepal — National Tree'), ('national-animal', 'Cow — National Animal'), ('national-food', 'Dal Bhat — National Food')]
REL_FRUIT_NE = [('national-flower', 'लाली गुराँस — राष्ट्रिय फूल'), ('national-tree', 'पीपल — राष्ट्रिय रूख'), ('national-animal', 'गाई — राष्ट्रिय पशु'), ('national-food', 'दालभात — राष्ट्रिय खाना')]
REL_FOOD = [('national-fruit', 'Suntala — National Fruit'), ('national-dress', 'Daura Suruwal &amp; Gunyu Cholo — National Dress'), ('national-dance', 'Deuda &amp; Maruni — National Dance'), ('national-flag', 'National Flag')]
REL_FOOD_NE = [('national-fruit', 'सुन्तला — राष्ट्रिय फल'), ('national-dress', 'दौरा सुरुवाल र गुन्यू चोलो — राष्ट्रिय पोशाक'), ('national-dance', 'देउडा र मारुनी — राष्ट्रिय नृत्य'), ('national-flag', 'राष्ट्रिय झण्डा')]

PAGES = [
 dict(slug='national-fruit', photo='national_fruit_of_nepal.webp', about_name='Mandarin orange (Citrus reticulata)', about_sameas='https://en.wikipedia.org/wiki/Mandarin_orange',
  en=dict(title='National Fruit of Nepal — Suntala (Orange) Guide | symbols.thenepal.io',
    desc='The Council of Ministers recognised the orange as Nepal\'s national fruit on 12 April 2024. Read what was decided, suntala vs junar, where it grows and FAQs.',
    og_title='National Fruit of Nepal — Suntala (Orange)', og_desc='What was decided on 12 April 2024, the suntala vs junar naming, where oranges grow in Nepal and FAQs.',
    ld_desc='A guide to Nepal\'s national fruit, the orange (suntala), recognised by the Council of Ministers on 12 April 2024: decision, naming, growing regions and FAQs.',
    itemlist_desc='The full list of Nepal\'s 22 national symbols, of which the suntala (national fruit) is one.', crumb='National Fruit',
    img_alt='Suntala (mandarin orange) hanging on a branch above Nepal\'s mid-hills (illustration)', img_caption='Suntala (mandarin orange), Nepal\'s national fruit — original illustration.',
    eyebrow='National Fruit of Nepal — Recognised 12 April 2024', h1='Suntala — <em>The Orange</em>',
    hero='<strong>The Council of Ministers recognised the orange as Nepal\'s national fruit on 12 April 2024</strong> — widely discussed as the mandarin orange, the suntala (Citrus reticulata) — a fruit of the mid-hill orchards that ripens around Dashain and Tihar.',
    tags=['Nepali name: सुन्तला', 'Scientific name: Citrus reticulata', 'Recognised: 12 Apr 2024 (30 Chaitra 2080)', 'Grows in: mid-hills'],
    caption='Original illustration of a suntala branch — not a photograph.',
    facts=[('Nepali name', 'सुन्तला (Suntala)', True), ('English name', 'Orange / mandarin orange', False), ('Scientific name', 'Citrus reticulata (mandarin)', False), ('Family', 'Rutaceae', False),
           ('Recognised', '12 April 2024 (30 Chaitra 2080 BS)', False), ('Decided by', 'Council of Ministers', False), ('Announced by', 'Rekha Sharma, Government Spokesperson', False), ('Species named in decision', 'Not confirmed (reports say "orange")', False)],
    pron=('सुन्तला', 'Suntala', 'SUN-ta-la'), body=FRUIT_EN_BODY, faq=FRUIT_EN_FAQ,
    related=rel('en', REL_FRUIT) + [(S + '/', 'All national symbols of Nepal →')], related_p='The suntala is one of 22 national symbols of Nepal. Explore the rest of the hub, from the flag to the national flower.'),
  ne=dict(title='नेपालको राष्ट्रिय फल — सुन्तला गाइड | symbols.thenepal.io',
    desc='मन्त्रिपरिषद्ले २०८० चैत ३० (२०२४ अप्रिल १२) मा सुन्तलालाई नेपालको राष्ट्रिय फल घोषणा गर्‍यो। निर्णय, सुन्तला र जुनारको भिन्नता, कहाँ फल्छ र प्रश्नोत्तर पढ्नुहोस्।',
    og_title='नेपालको राष्ट्रिय फल — सुन्तला', og_desc='२०८० चैत ३० को निर्णय, सुन्तला र जुनारको भिन्नता, नेपालमा सुन्तला कहाँ फल्छ र प्रश्नोत्तर।',
    ld_desc='मन्त्रिपरिषद्ले २०८० चैत ३० मा मान्यता दिएको नेपालको राष्ट्रिय फल सुन्तलाको गाइड: निर्णय, नाम, फल्ने क्षेत्र र प्रश्नोत्तर।',
    itemlist_desc='नेपालका २२ राष्ट्रिय चिन्हहरूको पूर्ण सूची, जसमध्ये सुन्तला (राष्ट्रिय फल) एक हो।', crumb='राष्ट्रिय फल',
    img_alt='नेपालको मध्य पहाडमाथि हाँगामा झुन्डिएका सुन्तला (चित्रण)', img_caption='सुन्तला, नेपालको राष्ट्रिय फल — मौलिक चित्रण।',
    eyebrow='नेपालको राष्ट्रिय फल — २०८० चैत ३० मा मान्यता', h1='सुन्तला — <em>नेपालको राष्ट्रिय फल</em>',
    hero='<strong>मन्त्रिपरिषद्ले २०८० चैत ३० (२०२४ अप्रिल १२) मा सुन्तलालाई नेपालको राष्ट्रिय फलका रूपमा मान्यता दियो</strong> — यसलाई व्यापक रूपमा मन्डारिन सुन्तला (Citrus reticulata) भनेर चर्चा गरिन्छ — मध्य पहाडी बगैँचाको फल, जुन दशैं र तिहारताका पाक्छ।',
    tags=['नेपाली नाम: सुन्तला', 'वैज्ञानिक नाम: Citrus reticulata', 'मान्यता: २०८० चैत ३०', 'फल्ने ठाउँ: मध्य पहाड'],
    caption='सुन्तलाको हाँगाको मौलिक चित्रण — तस्बिर होइन।',
    facts=[('नेपाली नाम', 'सुन्तला', False), ('अङ्ग्रेजी नाम', 'Orange / Mandarin orange', False), ('वैज्ञानिक नाम', 'Citrus reticulata (मन्डारिन)', False), ('परिवार', 'Rutaceae', False),
           ('मान्यता', '२०८० चैत ३० (२०२४ अप्रिल १२)', False), ('निर्णयकर्ता', 'मन्त्रिपरिषद्', False), ('घोषणा गर्ने', 'रेखा शर्मा, सरकारी प्रवक्ता', False), ('निर्णयमा तोकिएको प्रजाति', 'पुष्टि भएको छैन (समाचारमा "orange")', False)],
    pron=('सुन्तला', 'Suntala', 'सुन्-त-ला'), body=FRUIT_NE_BODY, faq=FRUIT_NE_FAQ,
    related=rel('ne', REL_FRUIT_NE) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p='सुन्तला नेपालका २२ राष्ट्रिय चिन्हमध्ये एक हो। झण्डादेखि राष्ट्रिय फूलसम्म बाँकी चिन्हहरू हेर्नुहोस्।')),
 dict(slug='national-food', photo='national_dish_of_nepal.webp', about_name='Dal bhat', about_sameas='https://en.wikipedia.org/wiki/Dal_bhat',
  en=dict(title='National Food of Nepal — Dal Bhat (and Dhindo) Guide | symbols.thenepal.io',
    desc='Nepal has no officially designated national food that we could confirm; dal bhat is the staple most often named, and dhindo is also called a national dish. Plate, regions and FAQs.',
    og_title='National Food of Nepal — Dal Bhat', og_desc='Dal bhat, dhindo and gundruk: what Nepal eats, the status of "national dish", regional plates and FAQs.',
    ld_desc='A guide to Nepal\'s most-cited national food, dal bhat, with dhindo and gundruk: components, regional variations, status and FAQs.',
    itemlist_desc='The full list of Nepal\'s 22 national symbols, of which dal bhat (national food) is one.', crumb='National Food',
    img_alt='A Nepali dal bhat plate with rice, dal, vegetable curry and pickles (illustration)', img_caption='Dal bhat, Nepal\'s most-cited national food — original illustration.',
    eyebrow='National Food of Nepal — No Official Designation', h1='Dal Bhat — <em>The Everyday Plate</em>',
    hero='<strong>Dal bhat is the food most often called Nepal\'s national dish — though no official designation is confirmed</strong> — steamed rice with lentil soup and vegetable curry, eaten across the country, with dhindo as the classic hill alternative.',
    tags=['Nepali name: दालभात', 'Parts: bhat, dal, tarkari, achar', 'Also named: Dhindo', 'Status: not officially declared'],
    caption='Original illustration of a dal bhat plate — not a photograph.',
    facts=[('Nepali name', 'दालभात तरकारी', True), ('Main parts', 'Rice, lentil soup, vegetable curry, pickle', False), ('Eaten', 'Across Nepal; traditionally twice a day among the Khas', False), ('Hill alternative', 'Dhindo with gundruk', False),
           ('Official status', 'No declaration confirmed', False), ('Trekker slogan', 'Dal Bhat Power 24 Hour', False)],
    pron=('दालभात', 'Dal Bhat', 'DAAL BHAAT'), body=FOOD_EN_BODY, faq=FOOD_EN_FAQ,
    related=rel('en', REL_FOOD) + [(S + '/', 'All national symbols of Nepal →')], related_p='Dal bhat is one of 22 national symbols of Nepal. See the national fruit, dress, dance and more.'),
  ne=dict(title='नेपालको राष्ट्रिय खाना — दालभात (र ढिँडो) गाइड | symbols.thenepal.io',
    desc='नेपालको आधिकारिक राष्ट्रिय खाना तोकिएको पुष्टि भएको छैन; दालभात सबैभन्दा बढी भनिने मुख्य खाना हो र ढिँडोलाई पनि राष्ट्रिय परिकार भनिन्छ। थाल, क्षेत्रीय परिकार र प्रश्नोत्तर।',
    og_title='नेपालको राष्ट्रिय खाना — दालभात', og_desc='दालभात, ढिँडो र गुन्द्रुक: नेपालीले के खान्छन्, राष्ट्रिय परिकारको हैसियत, क्षेत्रीय थाल र प्रश्नोत्तर।',
    ld_desc='नेपालको सबैभन्दा बढी भनिने राष्ट्रिय खाना दालभातको गाइड: अवयव, क्षेत्रीय भिन्नता, हैसियत र प्रश्नोत्तर।',
    itemlist_desc='नेपालका २२ राष्ट्रिय चिन्हहरूको पूर्ण सूची, जसमध्ये दालभात (राष्ट्रिय खाना) एक हो।', crumb='राष्ट्रिय खाना',
    img_alt='भात, दाल, तरकारी र अचारसहितको नेपाली दालभात थाल (चित्रण)', img_caption='दालभात, नेपालको सबैभन्दा बढी भनिने राष्ट्रिय खाना — मौलिक चित्रण।',
    eyebrow='नेपालको राष्ट्रिय खाना — आधिकारिक तोकिएको छैन', h1='दालभात — <em>दैनिक थाल</em>',
    hero='<strong>दालभातलाई नेपालको राष्ट्रिय परिकार भनेर सबैभन्दा बढी चिनिन्छ — यद्यपि आधिकारिक रूपमा तोकिएको पुष्टि भएको छैन</strong> — भात, दाल र तरकारी देशभर खाइन्छ; पहाडको परम्परागत विकल्प ढिँडो हो।',
    tags=['नेपाली नाम: दालभात', 'भाग: भात, दाल, तरकारी, अचार', 'अर्को नाम: ढिँडो', 'हैसियत: आधिकारिक घोषणा छैन'],
    caption='दालभात थालको मौलिक चित्रण — तस्बिर होइन।',
    facts=[('नेपाली नाम', 'दालभात तरकारी', False), ('मुख्य भाग', 'भात, दाल, तरकारी, अचार', False), ('कहाँ खाइन्छ', 'देशभर; खस समुदायमा परम्परागत रूपमा दिनमा दुई पटक', False), ('पहाडी विकल्प', 'गुन्द्रुकसहित ढिँडो', False),
           ('आधिकारिक हैसियत', 'घोषणा पुष्टि भएको छैन', False), ('ट्रेकरको नारा', 'Dal Bhat Power 24 Hour', False)],
    pron=('दालभात', 'Dal Bhat', 'दाल-भात'), body=FOOD_NE_BODY, faq=FOOD_NE_FAQ,
    related=rel('ne', REL_FOOD_NE) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p='दालभात नेपालका २२ राष्ट्रिय चिन्हमध्ये एक हो। राष्ट्रिय फल, पोशाक, नृत्य र अन्य चिन्हहरू हेर्नुहोस्।')),
]
