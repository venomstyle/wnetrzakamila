import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';
import { C, Koniec, Tlo, useWejscie, zanik } from './wspolne';
const KROKI = ['Sprawdzam stronę i wizytówkę Google oczami klienta', 'Porównuję Cię z firmami z Twojego miasta', 'Nagrywam wideo z listą poprawek'];
export const Audyt: React.FC = () => {
  const f = useCurrentFrame();
  const h = useWejscie(0); const p = useWejscie(40);
  const scena1 = zanik(f, 290);
  const miara = interpolate(f, [70, 250], [0, 100], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <Tlo>
      <AbsoluteFill style={{ padding: '260px 84px 360px', opacity: scena1, display: 'flex', flexDirection: 'column', gap: 56 }}>
        <div style={{ ...h, fontStretch: '112%', fontWeight: 850, fontSize: 104, lineHeight: 1.02, letterSpacing: '-0.02em' }}>Nagram Ci wideo <span style={{ color: C.acc }}>o Twojej stronie.</span></div>
        <div style={{ ...p, fontFamily: 'Inter', fontSize: 46, color: C.ink2 }}>Za darmo. Wystarczy nazwa firmy i miasto.</div>
        <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', gap: 40, paddingLeft: 70, marginTop: 20 }}>
          <div style={{ position: 'absolute', left: 10, top: 0, width: 30, height: `${miara}%`, background: `repeating-linear-gradient(180deg,${C.on} 0 3px,transparent 3px 24px),${C.acc}`, borderRadius: 4 }} />
          {KROKI.map((k, i) => { const s = useWejscie(80 + i * 55, 40); return (
            <div key={k} style={{ ...s, padding: '34px 40px', background: C.paper, border: `2px solid ${C.line}`, borderRadius: 22 }}>
              <div style={{ color: C.acc, fontWeight: 850, fontSize: 34, letterSpacing: '.1em' }}>KROK {i + 1}</div>
              <div style={{ fontFamily: 'Inter', fontWeight: 650, fontSize: 46, lineHeight: 1.3, marginTop: 8 }}>{k}</div>
            </div>); })}
        </div>
        <div style={{ ...useWejscie(250), fontWeight: 850, fontSize: 60, color: C.acc }}>Na maila w 3 dni robocze.</div>
      </AbsoluteFill>
      {f >= 300 && <Koniec od={300} haslo={'Projektuję strony od 7 lat. Zacznij od audytu.'} />}
    </Tlo>
  );
};
