# -*- coding: utf-8 -*-
# /quiz/ and /ne/quiz/: 20-question bank, 12 drawn at random per run, explanation after each answer.
# All answers come from facts on our own pages (see official-vs-unofficial for constitutional articles).
import re as _re, json as _json
_hub = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
_css = []
for _l in _hub.split('\n'):
    if _re.match(r'^(\.quiz-|\.certificate|\.qr-|/\* quiz results)', _l): _css.append(_l)
    if 'max-width:600px){.quiz-choices' in _l: _css.append(_l)
QUIZ_CSS = '<style>\n' + '\n'.join(_css) + '\n.quiz-section{margin:8px 0 36px;overflow:clip;}\n.quiz-why{margin-top:14px;font-size:.88rem;color:rgba(251,243,230,.88);background:rgba(251,243,230,.08);border-left:3px solid var(--marigold);padding:10px 14px;border-radius:6px;display:none;}.quiz-why.show{display:block;}\n.quiz-section .quiz-head{margin-bottom:18px}.quiz-hub-links{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 26px}.quiz-hub-links a{font-size:.9rem;font-weight:600}\n</style>\n'
# (question, [choices], answer_index, why)
QEN = [
 ("What is the national animal of Nepal?", ["Yak", "Cow", "Elephant", "Tiger"], 1, "The cow is named as the national animal in Article 9(3) of the Constitution."),
 ("Which bird is Nepal's national bird?", ["Peacock", "Eagle", "Himalayan Monal (Danphe)", "Parrot"], 2, "The Lophophorus, the Danphe or Himalayan Monal, is named in Article 9(3)."),
 ("What is Nepal's national flower?", ["Lotus", "Rhododendron (Lali Gurans)", "Marigold", "Orchid"], 1, "Article 9(3) names the Rhododendron arboreum as the national flower."),
 ("What is Nepal's national colour?", ["Crimson", "Saffron", "Green", "Blue"], 0, "Article 9(3) says crimson is the national colour, the same crimson as the flag."),
 ("What is unusual about the shape of Nepal's flag?", ["It is a perfect square", "It has two stacked pennants and is not a rectangle", "It is round", "It has no colours"], 1, "Nepal's flag is the world's only non-quadrilateral national flag."),
 ("Which article of the Constitution names the national flower, colour, animal and bird?", ["Article 3", "Article 6", "Article 9(3)", "Article 289"], 2, "Article 9(3) lists them together. Article 8 covers the flag; Articles 6 and 7 cover language."),
 ("Which sport did the Government of Nepal declare the national sport in 2017?", ["Cricket", "Football", "Kabaddi", "Volleyball"], 3, "Volleyball was declared on 22 May 2017. Dandi Biyo and kabaddi are traditional games."),
 ("What is Nepal's official calendar called?", ["Gregorian", "Bikram Sambat", "Hijri", "Chinese lunar"], 1, "Bikram Sambat runs about 56.7 years ahead of the Gregorian calendar."),
 ("When does Nepali New Year 2084 begin?", ["1 January 2027", "13 October 2026", "14 April 2027", "1 July 2027"], 2, "Baisakh 1, 2084 BS falls on Wednesday, 14 April 2027."),
 ("Under Article 7, which language is the language of official business?", ["Hindi", "Nepali in Devanagari", "Maithili", "English"], 1, "Article 6 makes all mother tongues national languages; Article 7 names Nepali in Devanagari for official business."),
 ("What is the title of Nepal's national anthem?", ["Jana Gana Mana", "Resham Firiri", "Sayaun Thunga Phulka", "Lakhau Hamro"], 2, "Sayaun Thunga Phulka was adopted in 2007."),
 ("Which Kathmandu tower collapsed in the 2015 earthquake and was rebuilt?", ["Dharahara", "Boudhanath", "Swayambhunath", "Patan Durbar"], 0, "Dharahara is widely regarded as a national monument and was rebuilt afterwards."),
 ("Which fruit did the Council of Ministers recognise as the national fruit on 12 April 2024?", ["Mango", "Banana", "Orange", "Apple"], 2, "News reports say the cabinet recognised the orange; the exact species named in the decision text is not confirmed."),
 ("Is there a confirmed official national tree of Nepal?", ["Yes, the peepal, in Article 9", "Yes, the sal", "Yes, the rhododendron", "No, none is confirmed"], 3, "The peepal is the best-known sacred tree, but no official national tree is confirmed."),
 ("Which blade is most often called Nepal's national weapon?", ["Khukuri", "Katana", "Talwar", "Kris"], 0, "No official declaration is confirmed for the khukuri, so it is a customary symbol."),
 ("What is Nepal's official name for Mount Everest?", ["Chomolungma", "Annapurna", "Kanchenjunga", "Sagarmatha"], 3, "Sagarmatha is the official Nepali name; its height is 8,848.86 m."),
 ("Which institution issues Nepal's currency?", ["Nepal Rastra Bank", "Rastriya Banijya Bank", "Himalayan Bank", "Nepal Stock Exchange"], 0, "The rupee is issued by Nepal Rastra Bank."),
 ("Which flower forms the garland on Nepal's national emblem?", ["Lotus", "Rhododendron", "Marigold", "Jasmine"], 1, "The emblem shows Everest, hills, the Terai, joined hands and a rhododendron garland."),
 ("Which of these is NOT named in the Constitution as a national symbol?", ["The cow", "The Danphe", "Rhododendron", "The peepal tree"], 3, "The peepal is a customary symbol; the cow, Danphe and rhododendron are in Article 9(3)."),
 ("What colour are the borders of Nepal's flag?", ["White", "Green", "Deep blue", "Black"], 2, "Article 8(1) describes a crimson base with deep blue borders."),
]
QNE = [
 ("नेपालको राष्ट्रिय पशु कुन हो?", ["चौँरी", "गाई", "हात्ती", "बाघ"], 1, "संविधानको धारा ९(३) ले गाईलाई राष्ट्रिय पशु भनेको छ।"),
 ("नेपालको राष्ट्रिय पन्छी कुन हो?", ["मयूर", "चील", "डाँफे", "सुगा"], 2, "धारा ९(३) मा डाँफे (हिमालयन मोनाल) राष्ट्रिय पन्छी उल्लेख छ।"),
 ("नेपालको राष्ट्रिय फूल कुन हो?", ["कमल", "लालीगुराँस", "सयपत्री", "सुनाखरी"], 1, "धारा ९(३) ले लालीगुराँसलाई राष्ट्रिय फूल भनेको छ।"),
 ("नेपालको राष्ट्रिय रङ कुन हो?", ["गाढा रातो", "केसरी", "हरियो", "नीलो"], 0, "धारा ९(३) अनुसार गाढा रातो राष्ट्रिय रङ हो, झण्डाको रातो रङ जस्तै।"),
 ("नेपालको झण्डाको आकारमा के विशेषता छ?", ["यो पूरै वर्गाकार छ", "दुई पत्ताका रूपमा माथिनिर छन्, आयताकार होइन", "गोलो छ", "कुनै रङ छैन"], 1, "नेपालको झण्डा विश्वको एकमात्र चतुर्भुज नभएको राष्ट्रिय झण्डा हो।"),
 ("राष्ट्रिय फूल, रङ, पशु र पन्छी संविधानको कुन धारामा छन्?", ["धारा ३", "धारा ६", "धारा ९(३)", "धारा २८९"], 2, "धारा ९(३) ले यी सबै एकैठाउँ राखेको छ। धारा ८ झण्डा र धारा ६–७ भाषासँग सम्बन्धित छन्।"),
 ("२०१७ मा नेपाल सरकारले कुन खेललाई राष्ट्रिय खेल घोषणा गर्‍यो?", ["क्रिकेट", "फुटबल", "कबड्डी", "भलिबल"], 3, "भलिबल २०१७ मे २२ मा घोषणा भएको हो। दण्डीबियो र कबड्डी परम्परागत खेल हुन्।"),
 ("नेपालको आधिकारिक पात्रो कुन हो?", ["ग्रेगोरियन", "बिक्रम सम्वत्", "हिजरी", "चिनियाँ चन्द्र पात्रो"], 1, "बिक्रम सम्वत् ग्रेगोरियन पात्रोभन्दा करिब ५६.७ वर्ष अगाडि छ।"),
 ("नेपाली नयाँ वर्ष २०८४ कहिले सुरु हुन्छ?", ["२०२७ जनवरी १", "२०२६ अक्टोबर १३", "२०२७ अप्रिल १४", "२०२७ जुलाई १"], 2, "बैशाख १, २०८४ बुधबार, २०२७ अप्रिल १४ मा पर्छ।"),
 ("धारा ७ अनुसार सरकारी कामकाजको भाषा कुन हो?", ["हिन्दी", "देवनागरी लिपिमा लेखिने नेपाली", "मैथिली", "अङ्ग्रेजी"], 1, "धारा ६ ले सबै मातृभाषालाई राष्ट्रभाषा बनाएको छ; धारा ७ ले सरकारी कामकाजका लागि नेपाली तोकेको छ।"),
 ("नेपालको राष्ट्रगानको शीर्षक के हो?", ["जन गण मन", "रेशम फिरीरी", "सयौँ थुँगा फूलका", "लाखौँ हाम्रो"], 2, "‘सयौँ थुँगा फूलका’ सन् २००७ मा अपनाइएको हो।"),
 ("२०१५ को भूकम्पमा ढलेर पुनर्निर्माण गरिएको काठमाडौँको टावर कुन हो?", ["धरहरा", "बौद्धनाथ", "स्वयम्भू", "पाटन दरबार"], 0, "धरहरालाई व्यापक रूपमा राष्ट्रिय स्मारक मानिन्छ र पछि पुनर्निर्माण गरियो।"),
 ("२०२४ अप्रिल १२ मा मन्त्रिपरिषद्ले कुन फललाई राष्ट्रिय फलका रूपमा मान्यता दियो?", ["आँप", "केरा", "सुन्तला", "स्याउ"], 2, "समाचार अनुसार मन्त्रिपरिषद्ले सुन्तलालाई मान्यता दियो; निर्णयको पाठमा ठ्याक्कै कुन प्रजाति छ भन्ने पुष्टि भएको छैन।"),
 ("नेपालको आधिकारिक राष्ट्रिय रूख पुष्टि भएको छ?", ["छ, धारा ९ को पीपल", "छ, साल", "छ, लालीगुराँस", "छैन, कुनै पुष्टि भएको छैन"], 3, "पीपल सबैभन्दा चर्चित पवित्र रूख हो, तर आधिकारिक राष्ट्रिय रूख पुष्टि भएको छैन।"),
 ("नेपालको राष्ट्रिय हतियार भनेर प्रायः कुन हतियारलाई भनिन्छ?", ["खुकुरी", "कटाना", "तरवार", "क्रिस"], 0, "खुकुरीको आधिकारिक घोषणा पुष्टि भएको छैन, त्यसैले यो परम्परागत चिन्ह हो।"),
 ("सगरमाथाको नेपाली आधिकारिक नाम के हो?", ["चोमोलुङ्मा", "अन्नपूर्ण", "कञ्चनजङ्घा", "सगरमाथा"], 3, "सगरमाथा आधिकारिक नेपाली नाम हो; उचाइ ८,८४८.८६ मिटर।"),
 ("नेपालको मुद्रा कुन संस्थाले जारी गर्छ?", ["नेपाल राष्ट्र बैंक", "राष्ट्रिय वाणिज्य बैंक", "हिमालयन बैंक", "नेपाल स्टक एक्सचेन्ज"], 0, "रुपैयाँ नेपाल राष्ट्र बैंकले जारी गर्छ।"),
 ("नेपालको राष्ट्रिय प्रतीक चिन्हमा कुन फूलको माला छ?", ["कमल", "लालीगुराँस", "सयपत्री", "चमेली"], 1, "प्रतीक चिन्हमा सगरमाथा, पहाड, तराई, मिलेका हात र लालीगुराँसको माला छ।"),
 ("तलका मध्ये कुन संविधानमा राष्ट्रिय चिन्हका रूपमा उल्लेख छैन?", ["गाई", "डाँफे", "लालीगुराँस", "पीपलको रूख"], 3, "पीपल परम्परागत चिन्ह हो; गाई, डाँफे र लालीगुराँस धारा ९(३) मा छन्।"),
 ("नेपालको झण्डाको किनाराको रङ कुन हो?", ["सेतो", "हरियो", "गाढा नीलो", "कालो"], 2, "धारा ८(१) मा गाढा रातो आधार र गाढा नीलो किनारा वर्णित छ।"),
]
def _quiz_body(lang):
    en = lang == 'en'
    Q = QEN if en else QNE
    data = _json.dumps([dict(q=a, c=b, a=c, w=d) for a, b, c, d in Q], ensure_ascii=False)
    T = (dict(q='Question', of='/', score='Score', next='Next Question', res='See Results', retry='Retry Quiz', share='Share Result', copied='Copied! ✓', ph='Your name for the certificate', cert='Certificate of Achievement', title='Nepal National Symbols Quiz', name='Nepal Symbols Explorer', scored='scored', outof='out of', start='Start Quiz', intro='12 random questions from a bank of 20. Instant feedback with the reason, then a score and a certificate.',
              m100='Perfect score — a true Nepal symbols expert!', m80="Excellent! You know Nepal's symbols very well.", m50="Good effort — a solid grasp of Nepal's national symbols.", m0='Nice try — read the guides and take the quiz again.', url='https://symbols.thenepal.io/quiz/', sharetxt='on the Nepal National Symbols Quiz! Try it:')
         if en else
         dict(q='प्रश्न', of='/', score='अङ्क', next='अर्को प्रश्न', res='नतिजा हेर्नुहोस्', retry='फेरि प्रयास गर्नुहोस्', share='नतिजा सेयर गर्नुहोस्', copied='कपी भयो ✓', ph='प्रमाणपत्रका लागि तपाईंको नाम', cert='उपलब्धिको प्रमाणपत्र', title='नेपालका राष्ट्रिय चिन्ह क्विज', name='नेपाल चिन्ह अन्वेषक', scored='ले', outof='मध्ये', start='क्विज सुरु गर्नुहोस्', intro='२० प्रश्नको बैङ्कबाट अनियमित १२ प्रश्न। तुरुन्त कारणसहितको प्रतिक्रिया, त्यसपछि अङ्क र प्रमाणपत्र।',
              m100='पूर्ण अङ्क — साँच्चै नेपाली चिन्हका विज्ञ!', m80='उत्कृष्ट! तपाईंलाई नेपालका चिन्ह राम्ररी थाहा छ।', m50='राम्रो प्रयास — नेपालका राष्ट्रिय चिन्हको राम्रो ज्ञान।', m0='राम्रो प्रयास — गाइडहरू पढेर फेरि प्रयास गर्नुहोस्।', url='https://symbols.thenepal.io/ne/quiz/', sharetxt='ले नेपालका राष्ट्रिय चिन्ह क्विजमा अङ्क ल्याए! तपाईं पनि प्रयास गर्नुहोस्:'))
    hub = ('/', 'All 23 national symbols', '/official-vs-unofficial/', 'Which symbols are official?') if en else ('/ne/', 'सबै २३ राष्ट्रिय चिन्ह', '/ne/official-vs-unofficial/', 'कुन चिन्ह आधिकारिक छन्?')
    js = r'''
(function(){
  var BANK = __DATA__, T = __T__, N = 12;
  var body = document.getElementById('quiz-body'), startBtn = document.getElementById('quiz-start-btn');
  var Q = [], qi = 0, score = 0, answered = false;
  function pick(){ var a = BANK.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a.slice(0, N); }
  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
  function ask(){
    answered = false; var it = Q[qi], L = ['A','B','C','D'], pct = Math.round(qi / Q.length * 100);
    body.innerHTML = '<div class="quiz-card"><div class="quiz-progress-row"><span>'+T.q+' '+(qi+1)+' '+T.of+' '+Q.length+'</span><div class="quiz-bar"><div class="quiz-bar-fill" style="width:'+pct+'%"></div></div><span class="quiz-score-pill">'+T.score+': '+score+'</span></div>'
      + '<div class="quiz-question">'+esc(it.q)+'</div><div class="quiz-choices">'+it.c.map(function(c,i){return '<button type="button" class="quiz-choice" data-i="'+i+'"><span class="qc-letter">'+L[i]+'</span><span>'+esc(c)+'</span></button>';}).join('')+'</div>'
      + '<div class="quiz-why" id="quiz-why">'+esc(it.w)+'</div><div class="quiz-next-row"><button type="button" class="quiz-next-btn" id="quiz-next-btn">'+(qi===Q.length-1?T.res:T.next)+' <span aria-hidden="true">→</span></button></div></div>';
    var bs = body.querySelectorAll('.quiz-choice');
    bs.forEach(function(b){ b.addEventListener('click', function(){
      if (answered) return; answered = true; bs.forEach(function(x){x.disabled = true;});
      var i = parseInt(b.dataset.i, 10);
      if (i === it.a) { b.classList.add('correct'); score++; } else { b.classList.add('wrong'); bs[it.a].classList.add('correct'); }
      document.getElementById('quiz-why').classList.add('show'); document.getElementById('quiz-next-btn').classList.add('show');
    }); });
    document.getElementById('quiz-next-btn').addEventListener('click', function(){ qi++; if (qi >= Q.length) results(); else ask(); });
  }
  function msg(p){ return p === 100 ? T.m100 : p >= 80 ? T.m80 : p >= 50 ? T.m50 : T.m0; }
  function results(){
    var pct = Math.round(score / Q.length * 100);
    body.innerHTML = '<div class="quiz-result"><div class="qr-score">'+score+' / '+Q.length+'</div><div class="qr-sub">'+msg(pct)+'</div>'
      + '<div class="qr-name-row"><input type="text" class="qr-name-input" id="qr-name-input" placeholder="'+T.ph+'" maxlength="40" aria-label="'+T.ph+'"></div>'
      + '<div class="certificate"><div class="cert-eyebrow">'+T.cert+'</div><h3>'+T.title+'</h3><div class="cert-name" id="cert-name">'+T.name+'</div><div class="cert-detail">'+score+' '+T.outof+' '+Q.length+' ('+pct+'%)</div><div class="cert-detail">symbols.thenepal.io</div><div class="cert-seal">🏅</div></div>'
      + '<div class="quiz-result-actions"><button type="button" class="qr-share" id="qr-share">'+T.share+' <span aria-hidden="true">↗</span></button><button type="button" class="qr-retry" id="qr-retry">'+T.retry+'</button></div></div>';
    var inp = document.getElementById('qr-name-input'), cn = document.getElementById('cert-name');
    inp.addEventListener('input', function(){ cn.textContent = inp.value.trim() || T.name; });
    document.getElementById('qr-retry').addEventListener('click', start);
    document.getElementById('qr-share').addEventListener('click', function(){
      var text = (inp.value.trim() || T.name) + ' ' + score + '/' + Q.length + ' (' + pct + '%) ' + T.sharetxt + ' ' + T.url, btn = document.getElementById('qr-share');
      if (navigator.share) { navigator.share({title: T.title, text: text, url: T.url}).catch(function(){}); }
      else if (navigator.clipboard) { navigator.clipboard.writeText(text).then(function(){ var o = btn.innerHTML; btn.innerHTML = T.copied; setTimeout(function(){ btn.innerHTML = o; }, 1800); }).catch(function(){}); }
    });
  }
  function start(){ Q = pick(); qi = 0; score = 0; ask(); }
  startBtn.addEventListener('click', function(){ start(); body.scrollIntoView({behavior:'smooth', block:'center'}); });
})();
'''.replace('__DATA__', data).replace('__T__', _json.dumps(T, ensure_ascii=False))
    return QUIZ_CSS + '''    <section>
      <p class="lede">%s</p>
      <p class="quiz-hub-links"><a href="%s">%s →</a><a href="%s">%s →</a></p>
    </section>
    <div class="quiz-section">
      <div class="quiz-head"><div><span class="eyebrow">%s</span><h2>%s</h2></div><button class="quiz-start-btn" id="quiz-start-btn" type="button">%s <span aria-hidden="true">→</span></button></div>
      <div class="quiz-body" id="quiz-body"><div class="quiz-intro"><div class="quiz-big-emoji">🏆</div><p style="color:rgba(251,243,230,.8);font-size:.9rem;">%s</p></div></div>
    </div>
    <script>%s</script>
''' % (('Test what you know about Nepal\'s flag, anthem, emblem, animals, calendar and more. Every answer comes with the reason, so you learn as you go — useful for students and for Lok Sewa (PSC) general-knowledge practice.' if en else 'नेपालको झण्डा, राष्ट्रगान, प्रतीक चिन्ह, पशुपन्छी, पात्रो र अरूबारे आफ्नो ज्ञान जाँच्नुहोस्। हरेक उत्तरसँगै कारण दिइएको छ, त्यसैले खेल्दै सिक्न सकिन्छ — विद्यार्थी र लोकसेवा सामान्य ज्ञान अभ्यासका लागि उपयोगी।'),
        hub[0], hub[1], hub[2], hub[3], ('Test Yourself' if en else 'आफूलाई जाँच्नुहोस्'), T['title'], T['start'], T['intro'], js)
QUIZ_EN_FAQ = [
 ("How many questions are in the Nepal national symbols quiz?", "Each round has 12 questions drawn at random from a bank of 20, so every attempt is a little different."),
 ("Is this quiz useful for Lok Sewa (PSC) preparation?", "It covers general-knowledge facts on Nepal's symbols, with the constitutional articles where they apply. Always check the current syllabus and official sources for your exam."),
 ("Where do the answers come from?", "From the guides on this site, which cite the Constitution of Nepal (2015) and government announcements. See the Official vs Unofficial page for the legal basis of each symbol."),
 ("Can I download a certificate?", "At the end you can type your name to see it on the certificate and share your score. Taking a screenshot saves the certificate."),
]
QUIZ_NE_FAQ = [
 ("नेपालका राष्ट्रिय चिन्हको क्विजमा कति प्रश्न छन्?", "हरेक चरणमा २० प्रश्नको बैङ्कबाट अनियमित रूपमा १२ प्रश्न आउँछन्, त्यसैले हरेक प्रयास अलि फरक हुन्छ।"),
 ("यो क्विज लोकसेवा तयारीका लागि उपयोगी छ?", "यसले नेपालका चिन्हसम्बन्धी सामान्य ज्ञान र लागू हुँदा संवैधानिक धारासमेत समेट्छ। परीक्षाका लागि हालको पाठ्यक्रम र आधिकारिक स्रोत सधैँ जाँच्नुहोस्।"),
 ("उत्तरहरू कहाँबाट आएका हुन्?", "यस साइटका गाइडबाट, जसले नेपालको संविधान (२०७२) र सरकारी घोषणा उद्धृत गर्छन्। हरेक चिन्हको कानुनी आधारका लागि आधिकारिक कि परम्परागत पृष्ठ हेर्नुहोस्।"),
 ("के प्रमाणपत्र डाउनलोड गर्न सकिन्छ?", "अन्त्यमा आफ्नो नाम लेखेर प्रमाणपत्रमा हेर्न र अङ्क सेयर गर्न सकिन्छ। स्क्रिनसट लिएर प्रमाणपत्र सुरक्षित गर्न सकिन्छ।"),
]
REL_Q = [('official-vs-unofficial', 'Official vs Unofficial Symbols'), ('national-flag', 'National Flag'), ('national-emblem', 'National Emblem'), ('national-calendar', 'National Calendar')]
REL_Q_NE = [('official-vs-unofficial', 'आधिकारिक कि परम्परागत'), ('national-flag', 'राष्ट्रिय झण्डा'), ('national-emblem', 'राष्ट्रिय प्रतीक चिन्ह'), ('national-calendar', 'राष्ट्रिय पात्रो')]
EXTRA_PAGES = EXTRA_PAGES + [
 dict(slug='quiz', photo='nepal_symbols_quiz.webp', noitemlist=True, about_name='National symbols of Nepal', about_sameas='https://en.wikipedia.org/wiki/National_symbols_of_Nepal',
  en=dict(title='Nepal National Symbols Quiz — 12 Questions with Answers & Certificate',
    desc='Free Nepal general-knowledge quiz on national symbols: flag, anthem, emblem, animal, bird, flower, calendar and more. 12 random questions, instant reasons and a certificate.',
    og_title='Nepal National Symbols Quiz', og_desc='12 random questions from a bank of 20, with the reason behind every answer and a shareable certificate.',
    ld_desc='An interactive quiz on the national symbols of Nepal with explanations for every answer.', itemlist_desc='', crumb='Quiz',
    img_alt='A gold trophy, a crimson pennant and question marks (illustration)', img_caption='Nepal symbols quiz — original illustration.',
    eyebrow='Free Quiz — General Knowledge', h1='Nepal National Symbols <em>Quiz</em>',
    hero='<strong>12 random questions, the reason behind every answer, and a certificate at the end.</strong> Covers the flag, anthem, emblem, animal, bird, flower, colour, calendar and more.',
    tags=['12 questions per round', '20-question bank', 'Reasons shown', 'Free'], caption='Original illustration — not a photograph.',
    facts=[('Questions', '12 per round', False), ('Bank size', '20 questions', False), ('Format', 'Multiple choice', False), ('Feedback', 'Reason after each answer', False), ('Result', 'Score and certificate', False), ('Cost', 'Free', False)],
    pron=('क्विज', 'Quiz', 'kwiz'), body=_quiz_body('en'), faq=QUIZ_EN_FAQ, related=rel('en', REL_Q) + [(S + '/', 'All national symbols of Nepal →')], related_p='Study the guides, then retake the quiz.'),
  ne=dict(title='नेपालका राष्ट्रिय चिन्ह क्विज — १२ प्रश्न, उत्तर र प्रमाणपत्र',
    desc='नेपालका राष्ट्रिय चिन्हबारे निःशुल्क सामान्य ज्ञान क्विज: झण्डा, राष्ट्रगान, प्रतीक चिन्ह, पशु, पन्छी, फूल, पात्रो र अरू। अनियमित १२ प्रश्न, कारणसहित उत्तर र प्रमाणपत्र।',
    og_title='नेपालका राष्ट्रिय चिन्ह क्विज', og_desc='२० प्रश्नको बैङ्कबाट अनियमित १२ प्रश्न, हरेक उत्तरको कारण र सेयर गर्न मिल्ने प्रमाणपत्र।',
    ld_desc='नेपालका राष्ट्रिय चिन्हबारे हरेक उत्तरको व्याख्यासहितको अन्तरक्रियात्मक क्विज।', itemlist_desc='', crumb='क्विज',
    img_alt='सुनौलो ट्रफी, गाढा रातो पताका र प्रश्नचिह्न (चित्रण)', img_caption='नेपाल चिन्ह क्विज — मौलिक चित्रण।',
    eyebrow='निःशुल्क क्विज — सामान्य ज्ञान', h1='नेपालका राष्ट्रिय चिन्ह <em>क्विज</em>',
    hero='<strong>अनियमित १२ प्रश्न, हरेक उत्तरको कारण, र अन्त्यमा प्रमाणपत्र।</strong> झण्डा, राष्ट्रगान, प्रतीक चिन्ह, पशु, पन्छी, फूल, रङ, पात्रो र अरू समेटिएको।',
    tags=['प्रत्येक चरणमा १२ प्रश्न', '२० प्रश्नको बैङ्क', 'कारणसहित', 'निःशुल्क'], caption='मौलिक चित्रण — तस्बिर होइन।',
    facts=[('प्रश्न', 'प्रत्येक चरणमा १२', False), ('बैङ्क', '२० प्रश्न', False), ('ढाँचा', 'बहुवैकल्पिक', False), ('प्रतिक्रिया', 'हरेक उत्तरपछि कारण', False), ('नतिजा', 'अङ्क र प्रमाणपत्र', False), ('शुल्क', 'निःशुल्क', False)],
    pron=('क्विज', 'Quiz', 'क्विज'), body=_quiz_body('ne'), faq=QUIZ_NE_FAQ, related=rel('ne', REL_Q_NE) + [(S + '/ne/', 'सबै राष्ट्रिय चिन्हहरू →')], related_p='गाइडहरू पढेर क्विज फेरि खेल्नुहोस्।'),
 ),
]
