let tag= document.querySelector("h2");
console.dir(tag.innerHTML);
tag.innerHTML+="from code with laiba";

let div= document.querySelectorAll(".box");
// console.dir(div);
// div[0].innerHTML="first 1";
// div[1].innerHTML="second 2";
// div[2].innerHTML="third 3";
// is ko hum for of loop se bhi ker sakte hai
index=1;
for (let i of div){
  i.innerText=`new unique value is ${index}`;
  index++;
}