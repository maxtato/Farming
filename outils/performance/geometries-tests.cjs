const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
class Attribute{
 constructor(array,itemSize){this.array=array;this.itemSize=itemSize;this.count=array.length/itemSize;}
 getX(i){return this.array[i*this.itemSize];}
}
class FloatAttribute extends Attribute{constructor(a,n){super(new Float32Array(a),n);}}
class Geometry{
 constructor(){this.attributes={};this.index=null;this.disposed=false;}
 setAttribute(k,v){this.attributes[k]=v;return this;}
 setIndex(a){this.index=Array.isArray(a)?new Attribute(new (a.some(i=>i>65535)?Uint32Array:Uint16Array)(a),1):a;return this;}
 clone(){const g=new Geometry();for(const k in this.attributes){const a=this.attributes[k];g.setAttribute(k,new Attribute(a.array.slice(),a.itemSize));}if(this.index)g.setIndex(Array.from(this.index.array));return g;}
 applyMatrix4(m){const a=this.attributes.position.array;for(let i=0;i<a.length;i+=3){a[i]=a[i]*m.s+m.x;a[i+1]=a[i+1]*m.s+m.y;a[i+2]=a[i+2]*m.s+m.z;}return this;}
 dispose(){this.disposed=true;}
}
class Color{set(c){this.r=(c>>16&255)/255;this.g=(c>>8&255)/255;this.b=(c&255)/255;}}
const ctx=vm.createContext({THREE:{Color,BufferGeometry:Geometry,Float32BufferAttribute:FloatAttribute}});
const a=source.indexOf('function mergeParts(');vm.runInContext(source.slice(a,source.indexOf('\n}',a)+2),ctx);
const geo=(p,indices,normals=p.map((_,i)=>i%3===1?1:0))=>{const g=new Geometry().setAttribute('position',new FloatAttribute(p,3)).setAttribute('normal',new FloatAttribute(normals,3));if(indices)g.setIndex(indices);return g;};
function expected(parts){const result={position:[],normal:[],color:[]};for(const p of parts){const g=p.g.clone();if(p.m)g.applyMatrix4(p.m);const c=new Color();c.set(p.c);for(const i of g.index?g.index.array:Array.from({length:g.attributes.position.count},(_,i)=>i)){for(const k of ['position','normal'])result[k].push(...g.attributes[k].array.slice(i*3,i*3+3));result.color.push(c.r,c.g,c.b);}}for(const k in result)result[k]=new Float32Array(result[k]);return result;}
function check(parts){const result=ctx.mergeParts(parts),want=expected(parts);for(const k in want){const data=result.attributes[k].array,expanded=result.index?new Float32Array(Array.from(result.index.array).flatMap(i=>Array.from(data.slice(i*3,i*3+3)))):data;assert.deepEqual(expanded,want[k],k);}for(const p of parts)assert.equal(p.g.disposed,false);return result;}
let passed=0;const test=(name,f)=>{f();passed++;console.log('PASS',name);};
test('Indexed quads retain every triangle, winding, normal and colour with fewer vertices',()=>{
 const g=geo([0,0,0,1,0,0,1,1,0,0,1,0],[0,1,2,0,2,3]),r=check([{g,c:0x83bc56}]);assert.equal(r.attributes.position.count,4);assert.equal(r.index.count,6);
});
test('Mixed indexed and unindexed parts keep offsets and transformed float values',()=>{
 const q=geo([0,0,0,1,0,0,1,1,0,0,1,0],[0,1,2,0,2,3]),t=geo([0,0,0,.5,1,0,1,0,0]);
 check([{g:q,c:0x8643be,m:{s:1.38,x:23.1,y:-.77,z:.125}},{g:t,c:0x32bcff},{g:q,c:0x124851}]);
});
test('Sparse and reordered indices survive even when there are more vertices than indices',()=>{
 check([{g:geo([0,0,0,1,0,0,1,1,0,0,1,0,3,4,5],[3,2,1]),c:0xffffff}]);
});
test('Large merged models retain indices beyond the 16-bit limit',()=>{
 const vertices=Array.from({length:66000*3},(_,i)=>i*.001),g=geo(vertices,[65997,65998,65999]);const r=check([{g,c:0x335577}]);assert(r.index.array instanceof Uint32Array);assert.equal(r.index.getX(2),65999);
});
test('Unindexed shapes and empty models retain their original representation',()=>{
 const g=geo([0,0,0,1,0,0,0,1,0]);assert.equal(check([{g,c:0xabcdef}]).index,null);assert.equal(check([]).attributes.position.count,0);
});
console.log(`${passed} geometry tests passed.`);
