// The editable game stays in index.html; only dist is deployed.
const fs=require('node:fs/promises'),path=require('node:path'),vm=require('node:vm'),zlib=require('node:zlib');
const {minify}=require('terser');
async function build(){
 const root=path.resolve(__dirname,'..'),dest=path.join(root,'dist');
 if(path.dirname(dest)!==root||path.basename(dest)!=='dist')throw Error('Invalid output path');
 await fs.mkdir(dest,{recursive:true});
 const source=await fs.readFile(path.join(root,'index.html'),'utf8');
 let html='',at=0;
 for(const m of source.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)){
  html+=source.slice(at,m.index);
  if(!m[2].trim())html+=m[0];
  else{
   // No renaming or algebraic rewrites: remove only comments and unnecessary whitespace.
   const result=await minify(m[2],{compress:false,mangle:false,format:{comments:false,inline_script:true}});
   new vm.Script(result.code);
   html+='<script'+m[1]+'>'+result.code+'</script>';
  }
  at=m.index+m[0].length;
 }
 html+=source.slice(at);
 await fs.writeFile(path.join(dest,'index.html'),html);
 for(const dir of ['pictos','portraits','portraits14','produits'])await fs.cp(path.join(root,dir),path.join(dest,dir),{recursive:true});
 await fs.copyFile(path.join(root,'verifier.html'),path.join(dest,'verifier.html'));
 console.log(JSON.stringify({sourceBytes:Buffer.byteLength(source),deliveredBytes:Buffer.byteLength(html),sourceGzip:zlib.gzipSync(source).length,deliveredGzip:zlib.gzipSync(html).length}));
}
build().catch(e=>{console.error(e);process.exitCode=1;});
