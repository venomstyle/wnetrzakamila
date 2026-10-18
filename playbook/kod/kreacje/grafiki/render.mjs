import { createRequire } from 'module'; import fs from 'fs'; const require = createRequire(import.meta.url); const { chromium } = require(process.env.PW);
const [dir,out]=process.argv.slice(2); const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium', args:['--no-sandbox','--allow-file-access-from-files'] });
for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.html'))) {
  const html=fs.readFileSync(dir+'/'+f,'utf8'); const w=+html.match(/--w:(\d+)px/)[1], h=+html.match(/--h:(\d+)px/)[1];
  const p=await b.newPage({viewport:{width:w,height:h}}); await p.goto('file://'+dir+'/'+f); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(150);
  const over = await p.evaluate(()=>{const w=document.querySelector('.wrap');return w.scrollHeight>w.clientHeight+2});
  await p.screenshot({path:out+'/'+f.replace('.html','.png')}); console.log(f, over?'PRZEPEŁNIENIE':'ok'); await p.close(); }
await b.close();
