import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';
import { C, Koniec, Tasma, Tlo, useWejscie, zanik } from './wspolne';
const FRAZA = 'hydraulik Kraków opinie';
export const Szukanie: React.FC = () => {
  const f = useCurrentFrame();
  const znaki = Math.floor(interpolate(f, [30, 75], [0, FRAZA.length], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  const s1 = useWejscie(0); const k1 = useWejscie(85); const k2 = useWejscie(95); const k3 = useWejscie(115); const t = useWejscie(150);
  const scena1 = zanik(f, 200); const scena2 = f >= 205 && f < 330 ? zanik(f, 318) : 0; const kursor = Math.floor(f / 15) % 2 ? 1 : 0;
  return (
    <Tlo>
      <AbsoluteFill style={{ padding: '260px 84px 360px', opacity: scena1, display: 'flex', flexDirection: 'column', gap: 44 }}>
        <div style={{ ...s1, fontStretch: '112%', fontWeight: 850, fontSize: 80, lineHeight: 1.05, letterSpacing: '-0.02em' }}>Polecił Cię sąsiad. Klient i tak sprawdzi Cię w Google.</div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 26, padding: '34px 44px', background: C.ink, color: C.on, borderRadius: 999, fontFamily: 'Inter', fontWeight: 600, fontSize: 54, boxShadow: '0 24px 48px rgba(0,0,0,.45)' }}>
          <svg viewBox="0 0 24 24" width="54" height="54"><circle cx="11" cy="11" r="7" fill="none" stroke="#111316" strokeWidth="2.5"/><path d="m20 20-3.5-3.5" stroke="#111316" strokeWidth="2.5" strokeLinecap="round"/></svg>
          <span>{FRAZA.slice(0, znaki)}<span style={{ opacity: znaki < FRAZA.length ? 1 : kursor }}>|</span></span>
        </div>
        {[['Firma A', 'strona, 214 opinii', '4,9'], ['Firma B', 'strona, 96 opinii', '4,8']].map(([n, o, r], i) => (
          <div key={n} style={{ ...(i ? k2 : k1), display: 'flex', justifyContent: 'space-between', padding: '34px 40px', background: C.paper, border: `2px solid ${C.line}`, borderRadius: 22, fontFamily: 'Inter', fontSize: 44 }}>
            <span><b>{n}</b> <span style={{ color: C.muted, fontSize: 36 }}>· {o}</span></span><span style={{ color: C.acc, fontWeight: 700 }}>{r} ★</span>
          </div>
        ))}
        <div style={{ ...k3, padding: '34px 40px', border: `4px dashed ${C.acc}`, borderRadius: 22, color: C.acc, fontFamily: 'Inter', fontWeight: 700, fontSize: 46, textAlign: 'center' }}>A gdzie jest Twoja firma?</div>
        <div style={{ ...t, fontFamily: 'Inter', fontSize: 40, color: C.ink2, lineHeight: 1.4 }}>Dzwoni do pierwszej firmy, której stronę i opinie zobaczy.</div>
        <div style={{ ...t, fontFamily: 'Inter', fontSize: 28, color: C.muted, marginTop: 'auto' }}>Przykład poglądowy. Firmy A i B są zmyślone.</div>
      </AbsoluteFill>
      <AbsoluteFill style={{ padding: '300px 84px 360px', opacity: scena2, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 70 }}>
        <div style={{ fontStretch: '112%', fontWeight: 850, fontSize: 80, lineHeight: 1.05 }}>W Mapach Google</div>
        <Tasma od={215} liczba="30,3%" opis="fachowców nie podaje w wizytówce żadnej strony" />
        <div style={{ fontFamily: 'Inter', fontSize: 30, color: C.muted }}>Dane własne: 702 wizytówki z Map Google, 8 branż, 6 miast, 13.10.2026.</div>
      </AbsoluteFill>
      {f >= 330 && <Koniec od={330} haslo={'Sprawdzę, co widzi klient u Ciebie.'} />}
    </Tlo>
  );
};
