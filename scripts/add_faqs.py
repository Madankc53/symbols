#!/usr/bin/env python3
"""Append related-question FAQs (facts taken from each page's own fact box). Idempotent."""
import re
EN={
'anthem':[("How many submissions were received when Nepal chose its national anthem?","The current anthem was selected from 1,272 nationwide submissions and adopted on 3 August 2007."),
("What does the title Sayaun Thunga Phulka mean?","The Nepali title सयौं थुँगा फूलका means “Made of hundreds of flowers”.")],
'bird':[("What is the scientific name of the Himalayan Monal?","The Himalayan Monal, known in Nepal as the Danphe, is Lophophorus impejanus. It is also called the Impeyan Monal or Impeyan Pheasant and belongs to the pheasant family, Phasianidae."),
("Which law protects the Danphe in Nepal?","The Danphe is protected under Nepal's National Parks and Wildlife Conservation Act, 1973.")],
'butterfly':[("What is the scientific name of the Krishna Peacock?","The Krishna Peacock is Papilio krishna, a swallowtail in the family Papilionidae."),
("How big is the Krishna Peacock butterfly?","Its wingspan is roughly 120–130 mm.")],
'calendar':[("When did Bikram Sambat become official in Nepal?","Bikram Sambat was made official in 1901 CE (1958 B.S.) under the Rana rulers."),
("What type of calendar is Bikram Sambat?","Bikram Sambat is a lunisolar civil calendar with 12 months, running from Baisakh to Chaitra.")],
'cave':[("Where is Siddha Gufa located?","Siddha Gufa is at Bimalnagar, Bandipur, in Tanahun district."),
("How long is Siddha Gufa?","The surveyed length is about 758 m, with a surveyed vertical range of about 105 m.")],
'color':[("When was the flag carrying Nepal's national colour adopted?","The current national flag, whose field is crimson red, was adopted on 16 December 1962."),
("Which national symbols use crimson red?","Crimson red appears on the national flag and the national flower, and in the tika and sindoor.")],
'currency':[("How many paisa are in a Nepalese rupee?","One rupee is divided into 100 paisa."),
("What did the Nepalese rupee replace?","The rupee replaced the silver mohar in 1932.")],
'dance':[("Where does Deuda dance come from?","Deuda comes from the Karnali and Sudurpaschim provinces of far-western Nepal."),
("When is Maruni performed?","Maruni is performed mainly during Dashain and Tihar.")],
'dress':[("What is a Dhaka topi?","The Dhaka topi is the traditional men's headwear of Nepal, made from Dhaka cloth, a tradition that was originally handwoven. Topi Day is celebrated on 1 January."),
("What is a Majetro?","The Majetro is a women's shawl worn with the Gunyu Cholo, the traditional women's dress.")],
'everest':[("What is the Tibetan name of Mount Everest?","The Tibetan name is Chomolungma, meaning “Mother Goddess of the World”."),
("Is Mount Everest inside a national park?","Yes. It lies within Sagarmatha National Park, gazetted in 1976.")],
'fish':[("What is the scientific name of the Golden Mahseer?","The Golden Mahseer, also called the Himalayan Mahseer, is Tor putitora, a member of the carp family Cyprinidae."),
("What habitat does the Golden Mahseer need?","It lives in fast-flowing rivers and deep pools at roughly 200–2,000 m.")],
'flower':[("What is the scientific name of Nepal's national flower?","Lali Gurans is Rhododendron arboreum, in the heath family Ericaceae."),
("How many rhododendron species are found in Nepal?","About 31 rhododendron species have been recorded in Nepal.")],
'language':[("What are the older names of the Nepali language?","Nepali has historically been called Khaskura and Gorkhali."),
("How many mother tongues are recorded in Nepal?","The 2021 census recorded 124 mother tongues in Nepal.")],
'monument':[("Where is Dharahara located?","Dharahara is at Sundhara in Kathmandu."),
("What is another name for Dharahara?","Dharahara is also known as Bhimsen Tower, after Bhimsen Thapa, under whom it was built.")],
'museum':[("What was the National Museum of Nepal called earlier?","It was the Silkhana Museum (1926), then the Nepal Museum (1938), and became the National Museum in 1968."),
("Who runs the National Museum of Nepal?","It is run by the Government of Nepal through the Department of Archaeology.")],
'sport':[("How many players are on a volleyball team?","A volleyball side has 6 players."),
("What other sports are popular in Nepal?","Football, cricket and kabaddi are also popular.")],
'tree':[("What is the scientific name of the Peepal tree?","The Peepal is Ficus religiosa, in the family Moraceae. It is also called the Sacred Fig, Bodhi Tree or Ashwattha."),
("How tall does a Peepal tree grow?","A Peepal can reach up to 30 m with a wide spreading canopy, and grows from the lowlands to the mid-hills, about 10–1,520 m.")],
}
NE={
'anthem':[("राष्ट्रिय गान छनोट गर्दा कति रचना प्राप्त भएका थिए?","हालको राष्ट्रिय गान देशभरबाट प्राप्त १,२७२ रचनाहरूबाट छनोट गरिएको थियो र ३ अगस्ट २००७ मा अपनाइएको थियो।"),
("‘सयौं थुँगा फूलका’ शीर्षकको अर्थ के हो?","‘सयौं थुँगा फूलका’ को अर्थ अंग्रेजीमा “Made of hundreds of flowers” हो।")],
'bird':[("डाँफेको वैज्ञानिक नाम के हो?","डाँफेको वैज्ञानिक नाम Lophophorus impejanus हो। यसलाई Impeyan Monal वा Impeyan Pheasant पनि भनिन्छ र यो फेजेन्ट परिवार (Phasianidae) अन्तर्गत पर्छ।"),
("नेपालमा डाँफेलाई कुन कानुनले संरक्षण गरेको छ?","डाँफे राष्ट्रिय निकुञ्ज तथा वन्यजन्तु संरक्षण ऐन, १९७३ अन्तर्गत संरक्षित छ।")],
'butterfly':[("कृष्ण मयुर पुतलीको वैज्ञानिक नाम के हो?","यसको वैज्ञानिक नाम Papilio krishna हो र यो Papilionidae परिवारको पुतली हो।"),
("कृष्ण मयुर पुतली कति ठूलो हुन्छ?","यसको पखेटा फैलाउँदा लगभग १२०–१३० मिलिमिटर हुन्छ।")],
'calendar':[("बिक्रम संवत् नेपालमा कहिले आधिकारिक भयो?","बिक्रम संवत् राणा शासनकालमा सन् १९०१ (वि.सं. १९५८) मा आधिकारिक बनाइएको थियो।"),
("बिक्रम संवत् कस्तो पात्रो हो?","बिक्रम संवत् चन्द्र–सौर नागरिक पात्रो हो, जसमा वैशाखदेखि चैत्रसम्म १२ महिना हुन्छन्।")],
'cave':[("सिद्ध गुफा कहाँ छ?","सिद्ध गुफा तनहुँ जिल्लाको बन्दीपुर, विमलनगरमा अवस्थित छ।"),
("सिद्ध गुफा कति लामो छ?","सर्वेक्षण गरिएको लम्बाइ लगभग ७५८ मिटर र सर्वेक्षण गरिएको ठाडो दायरा लगभग १०५ मिटर हो।")],
'color':[("राष्ट्रिय रंग रहेको झण्डा कहिले अपनाइयो?","सिन्दुरे रातो रंगको मूल भाग भएको हालको राष्ट्रिय झण्डा १६ डिसेम्बर १९६२ मा अपनाइएको थियो।"),
("कुन राष्ट्रिय प्रतीकहरूमा सिन्दुरे रातो रंग देखिन्छ?","सिन्दुरे रातो रंग राष्ट्रिय झण्डा र राष्ट्रिय फूलमा तथा टिका र सिन्दुरमा देखिन्छ।")],
'currency':[("एक नेपाली रुपैयाँमा कति पैसा हुन्छ?","एक रुपैयाँ १०० पैसामा विभाजित हुन्छ।"),
("नेपाली रुपैयाँले केको स्थान लियो?","रुपैयाँले सन् १९३२ मा चाँदीको मोहरको स्थान लियो।")],
'dance':[("देउडा नृत्य कहाँको हो?","देउडा नृत्य सुदूरपश्चिम नेपालको कर्णाली र सुदूरपश्चिम प्रदेशको हो।"),
("मारुनी नृत्य कहिले प्रदर्शन गरिन्छ?","मारुनी नृत्य मुख्यतया दशैं र तिहारमा प्रदर्शन गरिन्छ।")],
'dress':[("ढाका टोपी भनेको के हो?","ढाका टोपी नेपाली पुरुषको परम्परागत टोपी हो, जुन ढाका कपडाबाट बनाइन्छ। ढाका कपडा मूलतः हातले बुनिन्थ्यो। टोपी दिवस १ जनवरीमा मनाइन्छ।"),
("मजेत्रो भनेको के हो?","मजेत्रो महिलाले गुन्यू चोलोसँग ओढ्ने शाल हो।")],
'everest':[("सगरमाथाको तिब्बती नाम के हो?","सगरमाथाको तिब्बती नाम चोमोलुङमा हो, जसको अर्थ “संसारकी देवी माता” हो।"),
("सगरमाथा कुनै राष्ट्रिय निकुञ्जभित्र पर्छ?","पर्छ। यो सन् १९७६ मा घोषित सगरमाथा राष्ट्रिय निकुञ्जभित्र पर्छ।")],
'fish':[("असला माछाको वैज्ञानिक नाम के हो?","गोल्डेन महासीर (हिमालयन महासीर) को वैज्ञानिक नाम Tor putitora हो र यो माछा सिप्रिनिडी (Cyprinidae) परिवारको हो।"),
("गोल्डेन महासीरलाई कस्तो बासस्थान चाहिन्छ?","यो माछा लगभग २००–२,००० मिटर उचाइका तीव्र बहाव भएका नदी र गहिरा कुण्डमा बस्छ।")],
'flower':[("राष्ट्रिय फूल लालीगुराँसको वैज्ञानिक नाम के हो?","लालीगुराँसको वैज्ञानिक नाम Rhododendron arboreum हो र यो Ericaceae परिवारमा पर्छ।"),
("नेपालमा गुराँसका कति प्रजाति पाइन्छन्?","नेपालमा गुराँसका लगभग ३१ प्रजाति अभिलेखित छन्।")],
'language':[("नेपाली भाषाका पुराना नाम के-के हुन्?","नेपाली भाषालाई ऐतिहासिक रूपमा खस कुरा र गोरखाली भनिन्थ्यो।"),
("नेपालमा कति मातृभाषा अभिलेखित छन्?","सन् २०२१ को जनगणनाले नेपालमा १२४ मातृभाषा अभिलेख गरेको छ।")],
'monument':[("धरहरा कहाँ अवस्थित छ?","धरहरा काठमाडौंको सुन्धारामा अवस्थित छ।"),
("धरहराको अर्को नाम के हो?","धरहरालाई भीमसेन स्तम्भ पनि भनिन्छ, जुन भीमसेन थापाको पालामा बनेको थियो।")],
'museum':[("राष्ट्रिय संग्रहालयको अघिल्ला नाम के थिए?","यो सिल्खाना संग्रहालय (सन् १९२६), त्यसपछि नेपाल संग्रहालय (सन् १९३८) र सन् १९६८ मा राष्ट्रिय संग्रहालय बनेको हो।"),
("राष्ट्रिय संग्रहालय कसले सञ्चालन गर्छ?","यो नेपाल सरकारको पुरातत्त्व विभागमार्फत सञ्चालित छ।")],
'sport':[("भलिबल टोलीमा कति खेलाडी हुन्छन्?","भलिबलको एक पक्षमा ६ जना खेलाडी हुन्छन्।"),
("नेपालमा अरू कुन खेलहरू लोकप्रिय छन्?","फुटबल, क्रिकेट र कबड्डी पनि लोकप्रिय छन्।")],
'tree':[("पीपल रुखको वैज्ञानिक नाम के हो?","पीपलको वैज्ञानिक नाम Ficus religiosa हो र यो Moraceae परिवारमा पर्छ। यसलाई Sacred Fig, बोधि वृक्ष वा अश्वत्थ पनि भनिन्छ।"),
("पीपलको रुख कति अग्लो हुन्छ?","पीपल ३० मिटरसम्म अग्लो र फैलिएको छहारी भएको हुन्छ, र तराईदेखि मध्य पहाडसम्म लगभग १०–१,५२० मिटरमा पाइन्छ।")],
}
import html
def add(f,items):
    s=open(f,encoding='utf-8').read()
    i=s.rfind('<details class="faq-item">')
    if i<0: print('no faq',f); return
    j=s.index('</details>',i)+len('</details>')
    new=''
    for q,a in items:
        if q in s: continue
        new+='\n      <details class="faq-item">\n        <summary>%s</summary>\n        <p>%s</p>\n      </details>'%(html.escape(q,quote=False),html.escape(a,quote=False))
    open(f,'w',encoding='utf-8').write(s[:j]+new+s[j:])
for k,v in EN.items(): add('national-%s/index.html'%k,v)
for k,v in NE.items(): add('ne/national-%s/index.html'%k,v)
