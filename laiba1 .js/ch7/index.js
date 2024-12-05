// let div= document.querySelector("div");
// console.log(div);
// let id= div.getAttribute("id");
// console.log(id);
// div.style.backgroundColor="purple";

// let para= document.querySelector("p");
// console.log(para.setAttribute("class","para"));

//.append
// let newbut=document.createElement("button");
// newbut.innerText="click me";
// console.log(newbut);
// let div= document.querySelector("div");
// div.append(newbut);

//.prepend
// let newbut=document.createElement("button");
// newbut.innerText="click me";
// console.log(newbut);
// let div= document.querySelector("div");
// div.prepend(newbut);
//.before
// let newbut=document.createElement("button");
// newbut.innerText="click me";
// console.log(newbut);
// let div= document.querySelector("div");
// div.before(newbut);
//.after
let newbut=document.createElement("button");
newbut.innerText="click me";
console.log(newbut);
let div= document.querySelector("div");
div.after(newbut);


let newheading=document.createElement("h1");
newheading.innerHTML="<i>hello</i>";
console.log(newheading);
document.querySelector("body").prepend(newheading);