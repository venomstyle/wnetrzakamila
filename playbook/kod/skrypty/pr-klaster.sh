#!/bin/bash
# UWAGA: ścieżki S= i M= są z sesji niechcieznajda. Ustaw je na swoje przed użyciem.
# użycie: pr-klaster.sh <galaz> "slug=data slug=data ..."
set -e
S=/tmp/claude-0/-home-user-niechcieznajda/296d62a7-89f9-5ca7-8b2b-7eaec8d91278/scratchpad; export PATH=$S/bin:$PATH
B=$1; PAIRS=$2; M=/home/user/niechcieznajda; W=$S/wt-$B
cd $M && git fetch -q origin main && git worktree add -q -b $B $W origin/main && cd $W
cp $M/src/okladki/szablon.html src/okladki/szablon.html
rm -rf $S/okl-$B && mkdir -p $S/okl-$B
for p in $PAIRS; do s=${p%%=*}; d=${p##*=}; f=src/content/poradniki/$s.md
  cp $M/$f $f
  python3 - "$f" "$d" <<'PY'
import re,sys
p,d=sys.argv[1:]; t=open(p).read()
for k in ('publishedAt','updatedAt'): t=re.sub(rf'^{k}: .*$',f'{k}: {d}',t,count=1,flags=re.M)
t=re.sub(r'^draft: true$','draft: false',t,count=1,flags=re.M); open(p,'w').write(t)
PY
  cp $f $S/okl-$B/; done
python3 .claude/skills/klaster-tresci/scripts/okladka.py --template src/okladki/szablon.html --from-dir $S/okl-$B --brand "niech cię znajdą" --out public/okladki --keep-html >/dev/null 2>&1 || true
PW=$(npm root -g)/playwright node $S/render.mjs $PWD/src/okladki $PWD/public/okladki >/dev/null; rm -f src/okladki/.okladka-*.html
python3 .claude/skills/klaster-tresci/scripts/arkusz.py $(for p in $PAIRS; do echo public/okladki/${p%%=*}-og.png; done) --cols 4 --cell 400 --out $S/arkusz-$B.png >/dev/null
echo "== QA"; python3 .claude/skills/klaster-tresci/scripts/sprawdz.py src/content/poradniki 2>&1 | grep -E "BŁĄD|UWAGA" | grep -v -i "przyszło" | sort | uniq -c
rm -rf .claude/skills/klaster-tresci/scripts/__pycache__
npm ci --silent >/dev/null 2>&1
for d in $(for p in $PAIRS; do echo ${p##*=}; done | sort -u); do echo "$d: $(PUBLIKUJ_NA=$d npx astro build 2>&1 | grep -oE '[0-9]+ page\(s\) built')"; done
