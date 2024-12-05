let but1=document.querySelector("#but1");
// but1.onclick = (e)=>{
//   console.log(e);
//   console.log(e.type);
//   console.log(e.target);
//   console.log(e.clientX,e.clientY);
// }
//is ko hum is tarah bhi likh sakte hai e hum aik se zyada aik chese mai nahi laga sakte likin event listener ko hum aikk chese ke leye bar bar laga sakte hai
but1.addEventListener("click",()=>{
  console.log("clicked");
})
but1.addEventListener("click",(e)=>{
  console.log("clicked1");
  console.log(e);//event type ,target ,client sub kuch laga sakte hai
})
// Define the event listener function
const handleClick = () => {
  console.log("clicked3");
};

// Add the event listener
but1.addEventListener("click", handleClick);

// Remove the event listener
but1.removeEventListener("click", handleClick);

  

// but1.onclick = ()=>{
//   console.log("clicked");
//   let a=25
//   a++
//   console.log(a);
// }

let para= document.querySelector(".box");
para.onmouseover = (e)=>{
  console.log("mouse is over");
  console.log(e);
  console.log(e.type);
  console.log(e.target);
  console.log(e.clientX,e.clientY);
}
