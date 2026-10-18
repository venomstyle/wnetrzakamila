/** Wspólny zapis zgody (statystyki Plausible i pomiar Google Ads). Po 12 miesiącach pytamy ponownie.
 *  Zmianę wyboru ogłaszamy zdarzeniem `ncz-zgoda` (detail: 'granted' | 'denied'). */
export const KEY = 'ncz-consent';
export const KEY_AT = 'ncz-consent-at';
const WAZNA_MS = 365 * 24 * 60 * 60 * 1000;
export type Choice = 'granted' | 'denied';

export function read(): Choice | null {
  try {
    const v = localStorage.getItem(KEY);
    const at = Number(localStorage.getItem(KEY_AT) || 0);
    if (!at || Date.now() - at > WAZNA_MS) return null;
    return v === 'granted' || v === 'denied' ? v : null;
  } catch { return null; }
}
