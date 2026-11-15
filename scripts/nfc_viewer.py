# -*- coding: utf-8 -*-
# Markup and strings for the 3D flag-construction viewer (assets/nfc.css, assets/nfc.js). Geometry is computed in nfc.js from Schedule 1.
import json,re
EN_STEPS=['<strong>Base line.</strong> On crimson cloth, draw a line AB from left to right. Its length sets the scale, so AB = 1.', '<strong>Height and point D.</strong> Raise AC at right angles to AB, with AC = AB plus one third of AB. Mark D on AC so that AD = AB, then join B and D.', '<strong>Point E.</strong> On BD, mark E so that BE = AB.', '<strong>Line FG.</strong> Through E, draw FG parallel to AB, starting at F on AC, with FG = AB.', '<strong>Join C and G.</strong> The outline is now complete: two stacked pennants.', '<strong>Points H and I.</strong> Mark H on AB with AH = one quarter of AB. Draw HI parallel to AC, meeting CG at I.', '<strong>Bisect CF.</strong> Find the midpoint J of CF and draw JK parallel to AB, meeting CG at K.', '<strong>Point L.</strong> L is where JK and HI cross.', '<strong>Join J and G.</strong> Draw the line JG.', '<strong>Point M.</strong> M is where JG meets HI.', '<strong>Point N.</strong> With centre M and the shortest distance from M to BD as radius, mark N on HI below M.', '<strong>Line OM.</strong> Through M, draw a line parallel to AB, starting at O on AC.', '<strong>Arc PNQ.</strong> With centre L and radius LN, draw the lower semicircle. P and Q are where it meets line OM.', '<strong>Outer edge of the crescent.</strong> With centre M and radius MQ, draw the lower semicircle through P and Q.', '<strong>Points R, S and T.</strong> With centre N and radius NM, draw an arc meeting arc PNQ at R and S. Join RS; T is where RS meets HI.', '<strong>Outer boundary of the rays.</strong> With centre T and radius TS, draw the upper semicircle.', '<strong>Inner boundary of the rays.</strong> With centre T and radius TM, draw the upper arc.', '<strong>Eight moon rays.</strong> Make eight equal, similar triangles in the space between the two arcs.', '<strong>Points U and V.</strong> Bisect AF at U and draw UV parallel to AB, meeting BE at V.', '<strong>Inner circle of the sun.</strong> W is where UV meets HI. With centre W and radius MN, draw a circle.', '<strong>Outer circle of the sun.</strong> With centre W and radius LN, draw a second circle.', '<strong>Twelve sun rays.</strong> Make twelve equal, similar triangles in the ring between the circles, with two apexes touching HI.', '<strong>The border.</strong> The deep blue border is as wide as TN and runs along all sides. At the five angles of the flag, the outer angles equal the inner ones.', '<strong>Rope or pole.</strong> The border is made as described when the flag is hung from a rope. For a pole, the hole in the border alongside AC can be extended as needed.']
NE_STEPS=[
'<strong>आधार रेखा।</strong> गाढा रातो कपडामा बायाँबाट दायाँ रेखा AB तान्नुहोस्। यसको लम्बाइले मापन तोक्छ, त्यसैले AB = १।',
'<strong>उचाइ र बिन्दु D।</strong> AB सँग समकोण हुने गरी AC उठाउनुहोस्, जहाँ AC = AB र AB को एक तिहाइको जोड। AC मा D यसरी चिन्ह लगाउनुहोस् कि AD = AB, अनि B र D जोड्नुहोस्।',
'<strong>बिन्दु E।</strong> BD मा E यसरी चिन्ह लगाउनुहोस् कि BE = AB।',
'<strong>रेखा FG।</strong> E हुँदै AB सँग समानान्तर FG तान्नुहोस्, F AC मा पर्ने गरी र FG = AB।',
'<strong>C र G जोड्नुहोस्।</strong> बाहिरी आकार पूरा भयो: माथि-तल दुई पताका।',
'<strong>बिन्दु H र I।</strong> AB मा H यसरी चिन्ह लगाउनुहोस् कि AH = AB को एक चौथाइ। AC सँग समानान्तर HI तान्नुहोस्, जसले CG लाई I मा भेट्छ।',
'<strong>CF को मध्यबिन्दु।</strong> CF को मध्यबिन्दु J पत्ता लगाई AB सँग समानान्तर JK तान्नुहोस्, जसले CG लाई K मा भेट्छ।',
'<strong>बिन्दु L।</strong> JK र HI काटिने ठाउँ L हो।',
'<strong>J र G जोड्नुहोस्।</strong> रेखा JG तान्नुहोस्।',
'<strong>बिन्दु M।</strong> JG र HI काटिने ठाउँ M हो।',
'<strong>बिन्दु N।</strong> केन्द्र M र M बाट BD सम्मको सबैभन्दा छोटो दूरीलाई अर्धव्यास मानेर, M तल HI मा N चिन्ह लगाउनुहोस्।',
'<strong>रेखा OM।</strong> M हुँदै AB सँग समानान्तर रेखा तान्नुहोस्, O AC मा पर्ने गरी।',
'<strong>चाप PNQ।</strong> केन्द्र L र अर्धव्यास LN ले तल्लो अर्धवृत्त खिच्नुहोस्। P र Q त्यो चापले रेखा OM लाई भेट्ने बिन्दु हुन्।',
'<strong>अर्धचन्द्रको बाहिरी किनारा।</strong> केन्द्र M र अर्धव्यास MQ ले P र Q हुँदै तल्लो अर्धवृत्त खिच्नुहोस्।',
'<strong>बिन्दु R, S र T।</strong> केन्द्र N र अर्धव्यास NM ले चाप खिच्नुहोस्, जसले चाप PNQ लाई R र S मा भेट्छ। RS जोड्नुहोस्; RS ले HI लाई भेट्ने ठाउँ T हो।',
'<strong>किरणहरूको बाहिरी सीमा।</strong> केन्द्र T र अर्धव्यास TS ले माथिल्लो अर्धवृत्त खिच्नुहोस्।',
'<strong>किरणहरूको भित्री सीमा।</strong> केन्द्र T र अर्धव्यास TM ले माथिल्लो चाप खिच्नुहोस्।',
'<strong>चन्द्रमाका आठ किरण।</strong> दुई चापबीचको ठाउँमा आठ समान र एकैनासे त्रिभुज बनाउनुहोस्।',
'<strong>बिन्दु U र V।</strong> AF लाई U मा दुई बराबर भाग गरी AB सँग समानान्तर UV तान्नुहोस्, जसले BE लाई V मा भेट्छ।',
'<strong>सूर्यको भित्री वृत्त।</strong> UV र HI काटिने ठाउँ W हो। केन्द्र W र अर्धव्यास MN ले वृत्त खिच्नुहोस्।',
'<strong>सूर्यको बाहिरी वृत्त।</strong> केन्द्र W र अर्धव्यास LN ले दोस्रो वृत्त खिच्नुहोस्।',
'<strong>सूर्यका बाह्र किरण।</strong> दुई वृत्तबीचको घेरामा बाह्र समान र एकैनासे त्रिभुज बनाउनुहोस्, जसमध्ये दुईका टुप्पा HI मा छुन्छन्।',
'<strong>किनारा।</strong> गाढा नीलो किनारा TN जत्तिकै चौडा हुन्छ र सबै छेउमा जान्छ। झण्डाका पाँच कोणमा बाहिरी कोण भित्रीसँग बराबर हुन्छन्।',
'<strong>डोरी वा डण्डी।</strong> झण्डा डोरीमा टाँगिने भए किनारा माथि वर्णन गरिए जस्तै बनाइन्छ। डण्डीमा भए AC छेउको किनाराको प्वाल आवश्यकता अनुसार बढाउन सकिन्छ।',
]
CP='<a href="https://www.constituteproject.org/constitution/Nepal_2015" rel="noopener">Constitute Project</a>'
NL='<a href="https://nepallaws.com/?p=38031" rel="noopener">Nepal Laws</a>'
L={
'en':dict(lang='en',h2='Watch Nepal’s flag being built',p='Schedule 1 of the Constitution builds the flag in 24 steps. Here every point is calculated from those steps, drawn on a grid, filled with cloth, and then raised into a 3D flag. Drag to look around, or scrub the timeline.',
 aria='Interactive 3D animation of Nepal’s flag construction. Space plays or pauses, left and right arrows jump between sections, R replays, F toggles full screen.',
 canvas='Three-dimensional view of Nepal’s flag being constructed step by step',load='The 3D scene loads when you scroll here.',
 fbl='Nepal’s national flag, drawn to Schedule 1 geometry',fbm='The 3D view needs WebGL, which isn’t available here. This is the flag, drawn flat to the same geometry. The 24 steps are written out below.',
 jump='Jump to a section',chips=['Grid','Shape','Moon','Sun','Border and cloth','3D flag','Full view'],timeline='Timeline',
 pause='Pause',play='Play',replay='Replay',replayAria='Replay from the start',skip='Skip',skipAria='Skip to the finished flag',speedAria='Playback speed {n} times',orbit='Orbit',orbitAria='Drag to rotate and zoom',zout='Zoom out',zin='Zoom in',fs='Full screen',
 clause='Clause {n} of 24',preparing='Preparing the 3D scene…',libFail='The 3D library could not be loaded. This is the flag, drawn flat to the same geometry. The 24 steps are written out below.',
 summary='Read all 24 steps as text',steps=EN_STEPS,
 note='Geometry follows Schedule 1 (Article 8) of the Constitution of Nepal 2015: all points A to W are calculated from the clauses with AB = 1, and the animation’s proportions are checked against the flag’s published height-to-width ratio of about 1.219. Schedule 1 leaves the real-world size to the Government of Nepal, and on-screen size here is arbitrary. The Constitution says “crimson” and “deep blue” only; the on-screen colours are common digital approximations, not official values. Point letters follow the English text. Read the original on '+CP+' or '+NL+'.',
 noscript='This section needs JavaScript for the animation. The 24 steps are listed above as text.',
 pcap=[{'t':'Start with one unit','x':'Schedule 1 builds the flag from straight lines, arcs and circles. Every length comes from the base line AB.'},{'t':'The shape · clauses 1–5','x':'Two stacked pennants, drawn with a ruler and a compass.'},{'t':'The moon · clauses 6–18','x':'A crescent that cradles a fan of eight rays.'},{'t':'The sun · clauses 19–22','x':'A twelve-rayed sun, built from two circles.'},{'t':'Border and cloth · clauses 23–24','x':'Crimson cloth, then a deep blue border as wide as TN.'},{'t':'From pattern to cloth','x':'The finished pattern becomes a flag. Its outline is the two pennants you just drew.'},{'t':'The national flag of Nepal','x':'Drag to look around. Use Replay to watch it built again.'}]),
'ne':dict(lang='ne',h2='नेपालको झण्डा बन्दै गरेको हेर्नुहोस्',p='संविधानको अनुसूची १ ले झण्डा २४ चरणमा बनाउँछ। यहाँ ती चरणबाट हरेक बिन्दु गणना गरिएको छ, ग्रिडमा खिचिएको छ, कपडाले भरिएको छ र अनि 3D झण्डा बनेर उठ्छ। वरिपरि हेर्न तान्नुहोस्, वा टाइमलाइन चलाउनुहोस्।',
 aria='नेपालको झण्डा बनाउने विधिको अन्तरक्रियात्मक 3D एनिमेसन। स्पेसले चलाउँछ वा रोक्छ, बायाँ र दायाँ तीरले भाग सार्छ, R ले फेरि चलाउँछ, F ले पूरा स्क्रिन खोल्छ।',
 canvas='नेपालको झण्डा चरणबद्ध रूपमा बन्दै गरेको त्रिआयामिक दृश्य',load='यहाँसम्म स्क्रोल गर्दा 3D दृश्य खुल्छ।',
 fbl='अनुसूची १ को ज्यामितिअनुसार खिचिएको नेपालको राष्ट्रिय झण्डा',fbm='3D दृश्यलाई WebGL चाहिन्छ, जुन यहाँ उपलब्ध छैन। यो उही ज्यामितिमा समतल खिचिएको झण्डा हो। २४ चरण तल लेखिएका छन्।',
 jump='भागमा जानुहोस्',chips=['ग्रिड','आकार','चन्द्रमा','सूर्य','किनारा र कपडा','3D झण्डा','पूरा दृश्य'],timeline='टाइमलाइन',
 pause='रोक्नुहोस्',play='चलाउनुहोस्',replay='फेरि',replayAria='सुरुदेखि फेरि चलाउनुहोस्',skip='छिटो',skipAria='तयार झण्डामा जानुहोस्',speedAria='चल्ने गति {n} गुणा',orbit='घुमाउनुहोस्',orbitAria='घुमाउन र जुम गर्न तान्नुहोस्',zout='सानो गर्नुहोस्',zin='ठूलो गर्नुहोस्',fs='पूरा स्क्रिन',
 clause='२४ मध्ये चरण {n}',preparing='3D दृश्य तयार हुँदैछ…',libFail='3D लाइब्रेरी लोड हुन सकेन। यो उही ज्यामितिमा समतल खिचिएको झण्डा हो। २४ चरण तल लेखिएका छन्।',
 summary='२४ चरण पाठका रूपमा पढ्नुहोस्',steps=NE_STEPS,
 note='ज्यामिति नेपालको संविधान २०७२ को अनुसूची १ (धारा ८) अनुसार हो: A देखि W सम्मका सबै बिन्दु AB = १ मानेर चरणहरूबाट गणना गरिएका छन्, र एनिमेसनको अनुपात झण्डाको प्रकाशित उचाइ-चौडाइ अनुपात (करिब १.२१९) सँग जाँचिएको छ। वास्तविक आकार अनुसूची १ ले नेपाल सरकारलाई छाडेको छ, र यहाँ स्क्रिनमा देखिने आकार मनपरी हो। संविधानमा “गाढा रातो” र “गाढा नीलो” मात्र लेखिएको छ; स्क्रिनका रङ डिजिटल अनुमान हुन्, आधिकारिक मान होइनन्। बिन्दुका अक्षर अंग्रेजी पाठअनुसार हुन्। मूल पाठ '+CP+' वा '+NL+' मा पढ्नुहोस्।',
 noscript='एनिमेसनका लागि यो भागमा JavaScript चाहिन्छ। २४ चरण माथि पाठका रूपमा सूचीबद्ध छन्।',
 pcap=[{'t':'एक इकाइबाट सुरु','x':'अनुसूची १ ले सरल रेखा, चाप र वृत्तबाट झण्डा बनाउँछ। हरेक लम्बाइ आधार रेखा AB बाट आउँछ।'},{'t':'आकार · चरण १–५','x':'रुलर र कम्पासले खिचिएका माथि-तल दुई पताका।'},{'t':'चन्द्रमा · चरण ६–१८','x':'आठ किरणको पंखा बोकेको अर्धचन्द्र।'},{'t':'सूर्य · चरण १९–२२','x':'दुई वृत्तबाट बनेको बाह्र किरणे सूर्य।'},{'t':'किनारा र कपडा · चरण २३–२४','x':'गाढा रातो कपडा, त्यसपछि TN जत्तिकै चौडा गाढा नीलो किनारा।'},{'t':'नक्साबाट कपडासम्म','x':'तयार नक्सा झण्डा बन्छ। यसको आकार तपाईंले अहिले खिचेका दुई पताका नै हो।'},{'t':'नेपालको राष्ट्रिय झण्डा','x':'वरिपरि हेर्न तान्नुहोस्। फेरि बन्दै गरेको हेर्न “फेरि” थिच्नुहोस्।'}]),
}
ICO={'play':'<svg viewBox="0 0 24 24" aria-hidden="true"><path id="nfc-play-ic" d="M7 5v14M17 5v14"/></svg>'}
def html(lg):
    d=L[lg]; e=lambda s:s.replace('"','&quot;')
    chips=''.join('<button type="button" class="nfc-chip" data-i="%d">%s</button>'%(i,c) for i,c in enumerate(d['chips']))
    steps=''.join('<li>%s</li>'%s for s in d['steps'])
    i18n={k:d[k] for k in ('pause','play','replay','replayAria','speedAria','clause','preparing','libFail','pcap')}; i18n['ph']=d['chips']
    return ('''<link rel="stylesheet" href="/assets/nfc.css?v=1">
<section class="nfc" id="nfc" lang="%(lang)s" data-i18n="%(i18n)s" aria-labelledby="nfc-title">
<header class="nfc-head"><h2 id="nfc-title">%(h2)s</h2><p>%(p)s</p></header>
<div class="nfc-stage" id="nfc-stage" tabindex="0" role="group" aria-label="%(aria)s">
  <canvas class="nfc-canvas" id="nfc-canvas" role="img" aria-label="%(canvas)s"></canvas>
  <div class="nfc-load" id="nfc-load">%(load)s</div>
  <div class="nfc-fallback" id="nfc-fallback"><canvas id="nfc-fbc" width="480" height="586" role="img" aria-label="%(fbl)s"></canvas><p id="nfc-fbmsg">%(fbm)s</p></div>
  <div class="nfc-top" role="group" aria-label="%(jump)s">%(chips)s</div>
  <div class="nfc-caption" id="nfc-caption" aria-hidden="true"><span class="nfc-clause" id="nfc-clause"></span><span class="nfc-ctitle" id="nfc-ctitle"></span><p class="nfc-ctext" id="nfc-ctext"></p></div>
  <div class="nfc-bar">
    <input class="nfc-scrub" id="nfc-scrub" type="range" min="0" max="48" step="0.01" value="0" aria-label="%(timeline)s">
    <div class="nfc-btns">
      <button type="button" class="nfc-btn" id="nfc-play" aria-label="%(pause)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path id="nfc-play-ic" d="M7 5v14M17 5v14"/></svg><span class="nfc-lbl" id="nfc-play-t">%(pause)s</span></button>
      <button type="button" class="nfc-btn" id="nfc-replay" aria-label="%(replayAria)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7M3 4v5h5"/></svg><span class="nfc-lbl">%(replay)s</span></button>
      <button type="button" class="nfc-btn" id="nfc-end" aria-label="%(skipAria)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l9 7-9 7zM18 5v14"/></svg><span class="nfc-lbl">%(skip)s</span></button>
      <button type="button" class="nfc-btn" id="nfc-speed" aria-label="%(speedAria1)s">1×</button>
      <span class="nfc-sp"></span>
      <button type="button" class="nfc-btn" id="nfc-orbit" aria-pressed="true" aria-label="%(orbitAria)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a9 4 0 1 0 0 0M12 3v18M3 12a9 4 0 0 0 18 0"/></svg><span class="nfc-lbl">%(orbit)s</span></button>
      <button type="button" class="nfc-btn" id="nfc-zout" aria-label="%(zout)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14"/></svg></button>
      <button type="button" class="nfc-btn" id="nfc-zin" aria-label="%(zin)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M12 5v14"/></svg></button>
      <button type="button" class="nfc-btn" id="nfc-fs" aria-label="%(fs)s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg></button>
    </div>
  </div>
  <p class="nfc-sr" id="nfc-sr" aria-live="polite"></p>
</div>
<details class="nfc-steps" id="nfc-steps"><summary>%(summary)s</summary><ol>%(steps)s</ol></details>
<p class="nfc-note">%(note)s</p>
<noscript><p class="nfc-note">%(noscript)s</p></noscript>
<script defer src="/assets/nfc.js?v=1"></script>
</section>''' % dict(d, chips=chips, steps=steps, i18n=__import__('html').escape(json.dumps(i18n,ensure_ascii=False),quote=True), speedAria1=d['speedAria'].replace('{n}','1'))).replace('<link','<link')
