(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{245:function(t,e,n){"use strict";var o=n(3),r=n(247).start;o({target:"String",proto:!0,forced:n(248)},{padStart:function(t){return r(this,t,arguments.length>1?arguments[1]:void 0)}})},246:function(t,e,n){"use strict";var o=n(249),r={"text/plain":"Text","text/html":"Url",default:"Text"};t.exports=function(text,t){var e,n,l,c,d,mark,f=!1;t||(t={}),e=t.debug||!1;try{if(l=o(),c=document.createRange(),d=document.getSelection(),(mark=document.createElement("span")).textContent=text,mark.style.all="unset",mark.style.position="fixed",mark.style.top=0,mark.style.clip="rect(0, 0, 0, 0)",mark.style.whiteSpace="pre",mark.style.webkitUserSelect="text",mark.style.MozUserSelect="text",mark.style.msUserSelect="text",mark.style.userSelect="text",mark.addEventListener("copy",(function(n){if(n.stopPropagation(),t.format)if(n.preventDefault(),void 0===n.clipboardData){e&&console.warn("unable to use e.clipboardData"),e&&console.warn("trying IE specific stuff"),window.clipboardData.clearData();var o=r[t.format]||r.default;window.clipboardData.setData(o,text)}else n.clipboardData.clearData(),n.clipboardData.setData(t.format,text);t.onCopy&&(n.preventDefault(),t.onCopy(n.clipboardData))})),document.body.appendChild(mark),c.selectNodeContents(mark),d.addRange(c),!document.execCommand("copy"))throw new Error("copy command was unsuccessful");f=!0}catch(o){e&&console.error("unable to copy using execCommand: ",o),e&&console.warn("trying IE specific stuff");try{window.clipboardData.setData(t.format||"text",text),t.onCopy&&t.onCopy(window.clipboardData),f=!0}catch(o){e&&console.error("unable to copy using clipboardData: ",o),e&&console.error("falling back to prompt"),n=function(t){var e=(/mac os x/i.test(navigator.userAgent)?"⌘":"Ctrl")+"+C";return t.replace(/#{\s*key\s*}/g,e)}("message"in t?t.message:"Copy to clipboard: #{key}, Enter"),window.prompt(n,text)}}finally{d&&("function"==typeof d.removeRange?d.removeRange(c):d.removeAllRanges()),mark&&document.body.removeChild(mark),l()}return f}},247:function(t,e,n){var o=n(4),r=n(46),l=n(11),c=n(179),d=n(22),f=o(c),m=o("".slice),h=Math.ceil,v=function(t){return function(e,n,o){var c,v,y=l(d(e)),w=r(n),x=y.length,C=void 0===o?" ":l(o);return w<=x||""==C?y:((v=f(C,h((c=w-x)/C.length))).length>c&&(v=m(v,0,c)),t?y+v:v+y)}};t.exports={start:v(!1),end:v(!0)}},248:function(t,e,n){var o=n(58);t.exports=/Version\/10(?:\.\d+){1,2}(?: [\w./]+)?(?: Mobile\/\w+)? Safari\//.test(o)},249:function(t,e){t.exports=function(){var t=document.getSelection();if(!t.rangeCount)return function(){};for(var e=document.activeElement,n=[],i=0;i<t.rangeCount;i++)n.push(t.getRangeAt(i));switch(e.tagName.toUpperCase()){case"INPUT":case"TEXTAREA":e.blur();break;default:e=null}return t.removeAllRanges(),function(){"Caret"===t.type&&t.removeAllRanges(),t.rangeCount||n.forEach((function(e){t.addRange(e)})),e&&e.focus()}}},276:function(t,e,n){"use strict";n.r(e);n(245),n(16),n(105),n(104),n(74),n(75),n(76);var o=n(246),r=n.n(o),l={props:{guesses:{type:Array,required:!0}},data:function(){return{secTillMidnight:0}},computed:{secTillMidnightString:function(){var t=Math.floor(this.secTillMidnight/3600).toString().padStart(2,"0"),e=(Math.floor(this.secTillMidnight/60)%60).toString().padStart(2,"0"),n=(Math.floor(this.secTillMidnight)%60).toString().padStart(2,"0");return"".concat(t,":").concat(e,":").concat(n)}},created:function(){var t=new Date,e=new Date(t.getFullYear(),t.getMonth(),t.getDate(),23,59,59,999);this.secTillMidnight=Math.ceil((e.getTime()-t.getTime())/1e3),this.secTillMidnightTimer()},methods:{copyResults:function(){var t=(new Date).toLocaleDateString("en-US",{year:"2-digit",month:"numeric",day:"numeric"}),text="www.paintle.art ".concat(t,"\n");text+="Revealed "+(this.guesses.length-1)+" / 16 tiles\n\n";for(var e=0;e<16;e++)this.guesses.includes(e)?text+="🟦":text+="⬜",e%4==3&&(text+="\n");r()(text)},secTillMidnightTimer:function(){var t=this;this.secTillMidnight>0&&setTimeout((function(){t.secTillMidnight-=1,t.secTillMidnightTimer()}),1e3)}}},c=n(44),component=Object(c.a)(l,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"mx-auto bg-white"},[t._m(0),t._v(" "),n("div",{staticClass:"text-lg sm:text-2xl text-gray-400"},[n("p",[t._v("\n      You successfully guessed today's Paintle with\n      "+t._s(t.guesses.length-1<3?"only":"")+"\n      "),n("span",{staticClass:"font-bold"},[t._v(t._s(t.guesses.length-1)+" tile(s)")]),t._v("\n      revealed!\n    ")]),t._v(" "),n("br"),t._v(" "),n("p",[t._v("Time until next Paintle: "+t._s(t.secTillMidnightString))])]),t._v(" "),n("button",{staticClass:"\n      mt-4\n      px-4\n      text-lg\n      sm:text-2xl\n      py-2\n      border border-transparent\n      rounded-md\n      shadow-sm\n      text-white\n      bg-limey-dark\n      hover:bg-limey\n    ",on:{click:t.copyResults}},[t._v("\n    Copy results\n  ")])])}),[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"text-2xl sm:text-5xl text-gray-500 mx-auto pb-4"},[n("p",[t._v("Quite the Aesthete!")])])}],!1,null,null,null);e.default=component.exports}}]);