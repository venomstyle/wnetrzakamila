/* Dane marki używane przez szkielet. Wypełnij z plików projektu (prawdziwe fakty, bez wymyślania).
   Wygląd marki NIE jest tutaj: kolory i fonty są w src/styles/tokeny.css (z wybranego kierunku stylu). */
export const marka = {
  name: 'Nazwa marki',
  url: 'https://example.pl',           // = site w astro.config.mjs
  /* Firmowy adres do zgłoszeń zmian w poradnikach (ramka „Widzisz zmianę?” pod źródłami). */
  email: 'kontakt@example.pl',
  blog: { base: '/poradniki/', name: 'Poradniki', title: 'Poradniki', lead: 'Każdy tekst ma źródła i datę sprawdzenia.' },
  /* Autor: tylko prawdziwe fakty (patrz references/styl.md, „Uczciwość”). */
  autor: { name: 'Autor', bio: 'Jedno-dwa zdania prawdziwych faktów o autorze i o tym, jak sprawdza informacje.' },
  /* Domyślne CTA, gdy tekst nie ma własnego cta we frontmatterze. */
  cta: { title: 'Wezwanie do działania', text: 'Co czytelnik dostanie i ile mu to zajmie.', href: '/', button: 'Sprawdź' },
  /* Linki w nagłówku i w górnym pasie stopki. */
  nav: [{ label: 'Poradniki', href: '/poradniki/' }],
  stopka: { note: 'Jedno zdanie o marce.', links: [{ label: 'Polityka prywatności', href: '/polityka-prywatnosci/' }] },
};
