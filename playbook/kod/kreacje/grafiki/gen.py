import json,sys,os
R='/home/user/niechcieznajda'; OUT=sys.argv[1]
F=f'file://{R}/public/fonts'
LOGO=open(f'{R}/src/components/Logo.astro').read().split('<svg',1)[1].split('</svg>')[0]
LOGO='<svg'+LOGO+'</svg>'
CSS=f"""
@font-face{{font-family:Archivo;src:url('{F}/Archivo-Variable-latin-ext.woff2');font-weight:100 900;font-stretch:62% 125%;unicode-range:U+0100-02AF}}
@font-face{{font-family:Archivo;src:url('{F}/Archivo-Variable-latin.woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:Inter;src:url('{F}/Inter-Variable-latin-ext.woff2');font-weight:100 900;unicode-range:U+0100-02AF}}
@font-face{{font-family:Inter;src:url('{F}/Inter-Variable-latin.woff2');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:var(--w);height:var(--h);background:#0f1214;color:#f1efe8;font-family:Archivo;overflow:hidden;position:relative;
 background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 1px,transparent 1px 36px)}}
.wrap{{position:absolute;inset:0;padding:var(--top) var(--pad) var(--bot);display:flex;flex-direction:column}}
.logo{{display:flex;align-items:center;gap:16px;font-stretch:118%;font-weight:850;font-size:calc(var(--u)*1.1);letter-spacing:-.01em}}
.logo svg{{width:calc(var(--u)*2.6);height:calc(var(--u)*2.6)}} .logo b{{color:#ffd23f;font-weight:850}}
.kick{{margin-top:calc(var(--u)*2.2);font-size:calc(var(--u)*.95);font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#ffd23f}}
h1{{margin-top:calc(var(--u)*.8);font-stretch:112%;font-weight:850;font-size:calc(var(--u)*var(--h1,3.4));line-height:1.02;letter-spacing:-.02em;text-wrap:balance}}
h1 em{{font-style:normal;color:#ffd23f}}
.tape{{position:relative;margin:calc(var(--u)*2) calc(var(--pad)*-1) 0;padding:calc(var(--u)*2.4) var(--pad) calc(var(--u)*1.1);transform:rotate(-3deg);color:#111316;
 background:repeating-linear-gradient(90deg,rgba(17,19,22,.85) 0 3px,transparent 3px 22px) left top/100% calc(var(--u)*.9) no-repeat,
 repeating-linear-gradient(90deg,rgba(17,19,22,.85) 0 4px,transparent 4px 110px) left top/100% calc(var(--u)*1.6) no-repeat,#ffd23f;box-shadow:0 30px 60px rgba(0,0,0,.5)}}
.tape::before{{content:"";position:absolute;left:calc(var(--pad)*.45);top:-14px;bottom:-14px;width:calc(var(--u)*1.1);background:#c9ced3;border-radius:4px}}
.tape strong{{display:block;font-stretch:125%;font-weight:900;font-size:calc(var(--u)*var(--big,6.6));line-height:.95;letter-spacing:-.04em;padding-left:calc(var(--u)*1.4)}}
.tape span{{display:block;padding-left:calc(var(--u)*1.4);margin-top:calc(var(--u)*.5);font-family:Inter;font-weight:650;font-size:calc(var(--u)*1.05);line-height:1.3;max-width:24em}}
.sub{{margin-top:calc(var(--u)*2.2);font-family:Inter;font-size:calc(var(--u)*1.2);line-height:1.45;color:#d6d3cb;max-width:26em}}
.sub b{{color:#f1efe8}}
.bottom{{margin-top:auto;display:flex;flex-direction:column;gap:calc(var(--u)*.9)}}
.cta{{align-self:flex-start;display:inline-flex;align-items:center;gap:14px;padding:calc(var(--u)*.85) calc(var(--u)*1.4);background:#ffd23f;color:#111316;border-radius:10px;font-weight:850;font-size:calc(var(--u)*1.2)}}
.cta i{{font-style:normal;font-size:1.2em}}
.trust{{display:flex;flex-wrap:wrap;gap:8px 10px;font-family:Inter;font-weight:700;font-size:calc(var(--u)*.8);color:#f1efe8}}
.trust span{{padding:6px 12px;border:1.5px solid #2a3137;border-radius:999px;background:#171b1f}}
.trust span::before{{content:"✓ ";color:#ffd23f}}
.fine{{font-family:Inter;font-size:calc(var(--u)*.72);color:#9aa1a7;line-height:1.4}}
.search{{margin-top:calc(var(--u)*2);display:flex;align-items:center;gap:16px;padding:calc(var(--u)*.9) calc(var(--u)*1.2);background:#f1efe8;color:#111316;border-radius:999px;font-family:Inter;font-weight:600;font-size:calc(var(--u)*1.35);box-shadow:0 20px 40px rgba(0,0,0,.45)}}
.search svg{{width:1.1em;height:1.1em;flex:none}}
.cards{{margin-top:calc(var(--u)*1.1);display:flex;flex-direction:column;gap:calc(var(--u)*.6)}}
.card{{display:flex;justify-content:space-between;align-items:center;padding:calc(var(--u)*.75) calc(var(--u)*1.1);background:#171b1f;border:1px solid #2a3137;border-radius:12px;font-family:Inter;font-size:calc(var(--u)*1)}}
.card b{{font-weight:700}} .card small{{color:#9aa1a7;font-size:.85em}} .card .st{{color:#ffd23f;font-weight:700}}
.card.ty{{border:2px dashed #ffd23f;background:transparent;color:#ffd23f;font-weight:700;justify-content:center}}
.list{{margin-top:calc(var(--u)*2);display:flex;flex-direction:column;gap:calc(var(--u)*.8);font-family:Inter;font-size:calc(var(--u)*1.25);font-weight:600}}
.list div{{display:flex;gap:14px;align-items:flex-start}} .list div::before{{content:"";flex:none;width:calc(var(--u)*.9);height:calc(var(--u)*.9);margin-top:.25em;background:#ffd23f;border-radius:3px}}
"""
SEARCH='<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7" fill="none" stroke="#111316" stroke-width="2.5"/><path d="m20 20-3.5-3.5" stroke="#111316" stroke-width="2.5" stroke-linecap="round"/></svg>'
CTA_AUDYT='<span class="cta">Darmowy audyt strony <i>→</i></span>'
ADS={
 'a-dane':dict(kick='Dane z Map Google',h1='Klient sprawdza Cię w&nbsp;Google, <em>zanim zadzwoni</em>.',
   mid='<div class="tape"><strong>30,3%</strong><span>fachowców w Mapach Google nie podaje w wizytówce żadnej strony</span></div>',
   sub='Sprawdzę, co widzi klient u Ciebie, i <b>nagram krótkie wideo z listą poprawek.</b>',
   fine='Dane własne: 702 wizytówki z Map Google, 8 branż, 6 miast, 13.10.2026.'),
 'b-polecenia':dict(kick='Masz klientów z polecenia?',h1='Polecił Cię sąsiad. <em>Klient i tak sprawdzi Cię w Google.</em>',
   mid=f'<div class="search">{SEARCH} Nowak hydraulik opinie</div><div class="cards"><div class="card ty">Co zobaczy, zanim zadzwoni?</div></div>',
   sub='Zdjęcia realizacji, opinie i numer telefonu w jednym miejscu. <b>Pokażę Ci, czego dziś brakuje.</b>',
   fine='Przykład poglądowy. Nazwa firmy jest zmyślona.'),
 'c-portal':dict(kick='Zlecenia bez pośrednika',h1='Bez punktów. <em>Bez licytacji z pięcioma firmami.</em>',
   mid='<div class="list"><div>Klient sam znajduje Cię w Google</div><div>Widzi zdjęcia Twoich realizacji</div><div>Dzwoni prosto do Ciebie</div></div>',
   sub='Strona dla fachowca: realizacje, opinie i przycisk „Zadzwoń”. <b>Strona jest Twoja.</b>',
   fine='Strony projektuję od 7 lat.'),
 'd-wideo':dict(kick='Darmowy audyt',h1='Nagram Ci wideo <em>o Twojej stronie</em>. Za darmo.',
   mid='<div class="list"><div>Sprawdzę stronę i wizytówkę Google oczami klienta</div><div>Porównam Cię z firmami z Twojego miasta</div><div>Wideo na maila w 3 dni robocze, obejrzysz wieczorem</div></div>',
   sub='Wystarczy nazwa firmy i miasto. <b>Zajmie Ci 2 minuty.</b>',
   fine='Projektuję strony i aplikacje od 7 lat.'),
}
ZAUFANIE='<div class="trust"><span>Nie dzwonię</span><span>Nie jestem z Google</span><span>Bez haseł i kodów</span><span>Bez zobowiązań</span></div>'
FORMATY={'kwadrat':(1080,1080,26,72),'pion':(1080,1920,35,84),'poziom':(1200,628,15,48)}
os.makedirs(OUT,exist_ok=True)
for k,a in ADS.items():
  for f,(w,h,u,pad) in FORMATY.items():
    if f=='poziom' and k not in ('a-dane','d-wideo'): continue
    big = {'kwadrat':'4.4','pion':'5.2','poziom':'4.4'}[f]
    h1s = {'kwadrat':'2.5','pion':'2.9','poziom':'2.6'}[f]
    hide_sub = f=='poziom' or (f=='kwadrat' and k=='a-dane')
    html=f"""<!doctype html><html lang=pl><meta charset=utf-8><style>:root{{--w:{w}px;--h:{h}px;--u:{u}px;--pad:{pad}px;--top:{'220px' if f=='pion' else 'var(--pad)'};--bot:{'330px' if f=='pion' else 'var(--pad)'};--h1:{h1s};--big:{big}}}{CSS}</style><body><div class=wrap>
<div class=logo>{LOGO}<span>niech cię <b>znajdą</b></span></div>
<p class=kick>{a['kick']}</p><h1>{a['h1']}</h1>{a['mid']}
{'' if hide_sub else f"<p class=sub>{a['sub']}</p>"}
<div class=bottom>{ZAUFANIE if f!='poziom' else ''}{CTA_AUDYT}<p class=fine>{a['fine']}</p></div></div></body></html>"""
    open(f'{OUT}/{k}-{f}.html','w').write(html)
print('ok')
