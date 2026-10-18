/* Działy poradników: drugi poziom nad hubami (decyzja z 17.10.2026). Kolejność = droga fachowca do klienta.
   Nowy klaster: dopisz slug huba do działu. Hub spoza listy trafia do „Pozostałe”, więc nic nie znika.
   Kolor = kolor taśmy z okładek (src/okladki/szablon.html). */
export interface Dzial { id: string; nazwa: string; krotko: string; opis: string; huby: string[] }

export const dzialy: Dzial[] = [
  { id: 'widocznosc', nazwa: 'Bądź widoczny w Google', krotko: 'Widoczność w Google', opis: 'Wizytówka, opinie i mapy: to klient widzi, zanim zadzwoni.', huby: ['wizytowka-i-opinie', 'czy-google-widzi-twoja-strone', 'firma-w-innych-mapach', 'fachowcy-w-internecie'] },
  { id: 'strona', nazwa: 'Strona firmy', krotko: 'Strona firmy', opis: 'Ile kosztuje, co powinna mieć i jak sprawdzić obecną.', huby: ['strona-firmowa'] },
  { id: 'zlecenia', nazwa: 'Zdobywaj zlecenia', krotko: 'Zlecenia', opis: 'Portale, reklama i kody QR: skąd biorą się klienci i ile to kosztuje.', huby: ['zlecenia-i-klienci', 'reklama-dla-fachowca', 'kod-qr-dla-firmy'] },
  { id: 'obsluga', nazwa: 'Obsłuż klienta', krotko: 'Obsługa klienta', opis: 'Od pierwszego telefonu do zapłaty na miejscu.', huby: ['zapytania-od-klientow', 'telefon-w-firmie', 'platnosci-u-klienta'] },
  { id: 'firma', nazwa: 'Prowadzenie firmy', krotko: 'Firma', opis: 'Stawka, wycena, organizacja pracy i wizerunek firmy.', huby: ['stawka-i-wycena', 'organizacja-pracy-fachowca', 'wizerunek-firmy'] },
];

export const pozostale: Dzial = { id: 'inne', nazwa: 'Pozostałe tematy', krotko: 'Inne', opis: '', huby: [] };

export const kolorHuba: Record<string, string> = {
  'wizytowka-i-opinie': '#5ad1b8',
  'czy-google-widzi-twoja-strone': '#5cb8ff',
  'firma-w-innych-mapach': '#4dd9e8',
  'strona-firmowa': '#ffd23f',
  'zlecenia-i-klienci': '#ff8a3d',
  'reklama-dla-fachowca': '#ff6b6b',
  'kod-qr-dla-firmy': '#c9ced3',
  'zapytania-od-klientow': '#a8e05f',
  'telefon-w-firmie': '#ff86c8',
  'platnosci-u-klienta': '#3fd68f',
  'stawka-i-wycena': '#b9a3ff',
  'wizerunek-firmy': '#f1efe8',
  'organizacja-pracy-fachowca': '#ffc46b',
  'fachowcy-w-internecie': '#e05ad1',
};
export const KOLOR_DOMYSLNY = '#ffd23f';
