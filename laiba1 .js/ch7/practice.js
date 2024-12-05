let newbut=document.createElement("button");
newbut.innerText="click me";
newbut.style.backgroundColor="red";
newbut.style.color="white";
console.log(newbut);
let body= document.querySelector("body");
body.prepend(newbut);

//classlict.add
let para = document.querySelector("p");
para.classList.add("newclass");

//classlist.remove
// let para = document.querySelector("p");
// para.classList.remove("newclass");
