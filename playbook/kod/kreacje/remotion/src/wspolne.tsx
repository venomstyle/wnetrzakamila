import React from 'react';
import { AbsoluteFill, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
export const C = { bg: '#0f1214', paper: '#171b1f', ink: '#f1efe8', ink2: '#d6d3cb', muted: '#9aa1a7', line: '#2a3137', acc: '#ffd23f', on: '#111316' };
export const Fonty: React.FC = () => (
  <style>{`
  @font-face{font-family:Archivo;src:url('${staticFile('Archivo-Variable-latin-ext.woff2')}');font-weight:100 900;font-stretch:62% 125%;unicode-range:U+0100-02AF}
  @font-face{font-family:Archivo;src:url('${staticFile('Archivo-Variable-latin.woff2')}');font-weight:100 900;font-stretch:62% 125%}
  @font-face{font-family:Inter;src:url('${staticFile('Inter-Variable-latin-ext.woff2')}');font-weight:100 900;unicode-range:U+0100-02AF}
  @font-face{font-family:Inter;src:url('${staticFile('Inter-Variable-latin.woff2')}');font-weight:100 900}`}</style>
);
export const Tlo: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <AbsoluteFill style={{ background: C.bg, color: C.ink, fontFamily: 'Archivo', backgroundImage: 'repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 1px,transparent 1px 36px)' }}>
    <Fonty />{children}
  </AbsoluteFill>
);
export const Logo: React.FC<{ size?: number }> = ({ size = 40 }) => (
  <div style={{ display: 'flex', alignItems: 'center', gap: size * 0.4, fontStretch: '118%', fontWeight: 850, fontSize: size }}>
    <svg viewBox="0 0 64 64" width={size * 2.3} height={size * 2.3}><rect x="10" y="12" width="52" height="40" rx="2" fill="#ffd23f"/>{[14,18,22,26,30,34,38,42,46,50,54,58].map((x, i) => <line key={x} x1={x} y1="12" x2={x} y2={i % 5 === 0 ? 22 : 17} stroke="#111316" strokeWidth="1.6"/>)}<rect x="4" y="9" width="8" height="46" rx="2" fill="#c9ced3"/><text x="15" y="47" fontFamily="Archivo" fontStretch="125%" fontWeight="900" fontSize="22" fill="#111316">nz</text></svg>
    <span>niech cię <span style={{ color: C.acc }}>znajdą</span></span>
  </div>
);
/* Wejście elementu: sprężyna od klatki `od`. */
export const useWejscie = (od: number, odleglosc = 60) => {
  const f = useCurrentFrame(); const { fps } = useVideoConfig();
  const s = spring({ frame: f - od, fps, config: { damping: 200 } });
  return { opacity: s, transform: `translateY(${(1 - s) * odleglosc}px)` };
};
export const Tasma: React.FC<{ od: number; liczba: string; opis: string }> = ({ od, liczba, opis }) => {
  const f = useCurrentFrame(); const { fps } = useVideoConfig();
  const s = spring({ frame: f - od, fps, config: { damping: 18, mass: 0.9 } });
  return (
    <div style={{ position: 'relative', margin: '0 -84px', padding: '96px 84px 44px 140px', transform: `rotate(-3deg) translateX(${(1 - s) * -1200}px)`, color: C.on,
      background: `repeating-linear-gradient(90deg,rgba(17,19,22,.85) 0 3px,transparent 3px 26px) left top/100% 34px no-repeat,repeating-linear-gradient(90deg,rgba(17,19,22,.85) 0 5px,transparent 5px 130px) left top/100% 62px no-repeat,${C.acc}`, boxShadow: '0 30px 60px rgba(0,0,0,.5)' }}>
      <div style={{ position: 'absolute', left: 40, top: -18, bottom: -18, width: 46, background: '#c9ced3', borderRadius: 6 }} />
      <div style={{ fontStretch: '125%', fontWeight: 900, fontSize: 210, lineHeight: 0.95, letterSpacing: '-0.04em' }}>{liczba}</div>
      <div style={{ fontFamily: 'Inter', fontWeight: 650, fontSize: 42, lineHeight: 1.3, marginTop: 18, maxWidth: 820 }}>{opis}</div>
    </div>
  );
};
export const Koniec: React.FC<{ od: number; haslo: string }> = ({ od, haslo }) => {
  const a = useWejscie(od); const b = useWejscie(od + 8); const c = useWejscie(od + 16);
  return (
    <AbsoluteFill style={{ padding: '260px 84px 360px', display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 56 }}>
      <div style={a}><Logo size={52} /></div>
      <div style={{ ...b, fontStretch: '112%', fontWeight: 850, fontSize: 104, lineHeight: 1.02, letterSpacing: '-0.02em' }}>{haslo}</div>
      <div style={{ ...c, display: 'flex', flexDirection: 'column', gap: 26 }}>
        <div style={{ alignSelf: 'flex-start', background: C.acc, color: C.on, borderRadius: 16, padding: '30px 44px', fontWeight: 850, fontSize: 52 }}>Darmowy audyt strony →</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14 }}>{['Nie dzwonię', 'Nie jestem z Google', 'Bez haseł i kodów', 'Bez zobowiązań'].map((t) => <span key={t} style={{ fontFamily: 'Inter', fontWeight: 700, fontSize: 34, padding: '10px 20px', border: `2px solid ${C.line}`, borderRadius: 999, background: C.paper }}><span style={{ color: C.acc }}>✓</span> {t}</span>)}</div>
        <div style={{ fontFamily: 'Inter', fontSize: 40, color: C.ink2 }}>niechcieznajda.pl</div>
      </div>
    </AbsoluteFill>
  );
};
export const zanik = (f: number, od: number, dl = 10) => interpolate(f, [od, od + dl], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
