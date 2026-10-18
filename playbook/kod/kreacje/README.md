# Źródła kreacji

**Grafiki** (HTML → PNG):

```
python3 reklamy/zrodla/grafiki/gen.py /tmp/ads-html
PW=$(npm root -g)/playwright node reklamy/zrodla/grafiki/render.mjs /tmp/ads-html "$PWD/reklamy/grafiki"
```

**Filmy** (Remotion 4, React 18):
1. W osobnym katalogu: `npm i remotion@4 @remotion/cli@4 react@18 react-dom@18`.
2. Skopiuj tam `src/` oraz czcionki z `public/fonts` do `public/`.
3. Uruchom render:

```
npx remotion render src/index.ts szukanie film-szukanie.mp4 --browser-executable=<chrome-headless-shell>
```
