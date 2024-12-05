let modebtn= document.querySelector("#mode");
let body=document.querySelector("body");
let currentmode="light";
modebtn.addEventListener("click",()=>{
  if (currentmode==="light") {
    currentmode="dark";
    body.classList.add("dark");
    body.classList.remove("light");
  }
  else{
    currentmode="light";
    body.classList.add("light");
    body.classList.remove("dark");
  }

  console.log(currentmode);
})



let h1=document.querySelector("h1");
h1.onmouseover=()=>{
  let random = Math.floor(Math.random() * 1000);
  let random2 = Math.floor(Math.random() * 1000);
  let random3 = Math.floor(Math.random() * 100);
  h1.style.color=`rgb(${random}, ${random2}, ${random3})`;
}
console.log(h1);
