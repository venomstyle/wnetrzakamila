/* Zamienia cytaty zaczynające się od [!uwaga], [!praktyka], [!wzor], [!liczba]
   na ramki: <aside class="ramka ramka--typ"> z etykietą. Bez zależności.
   Wygląd ramek daje marka (CSS), etykiety można zmienić tutaj. */
const LABELS = { uwaga: 'Uwaga', praktyka: 'Z praktyki', wzor: 'Gotowy wzór', liczba: '' };

function walk(node, fn) {
  if (!node.children) return;
  node.children.forEach((child) => { fn(child); walk(child, fn); });
}

export default function remarkRamki() {
  return (tree) => {
    walk(tree, (node) => {
      if (node.type !== 'blockquote') return;
      const p = node.children?.[0];
      const t = p?.type === 'paragraph' ? p.children?.[0] : null;
      if (!t || t.type !== 'text') return;
      const m = t.value.match(/^\[!(uwaga|praktyka|wzor|liczba)\][ \t]*([^\n]*)\n?/);
      if (!m) return;
      const [, type, title] = m;
      t.value = t.value.slice(m[0].length);
      if (!t.value) p.children.shift();
      if (!p.children.length) node.children.shift();
      const label = type === 'liczba' ? title : (title || LABELS[type]);
      node.data = { hName: 'aside', hProperties: { className: ['ramka', `ramka--${type}`] } };
      node.children.unshift({
        type: 'paragraph',
        data: { hName: 'p', hProperties: { className: [type === 'liczba' ? 'ramka-liczba' : 'ramka-et'] } },
        children: [{ type: 'text', value: label }],
      });
    });
  };
}
