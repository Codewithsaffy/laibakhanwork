//fetch API

let URL ="https://dummyjson.com/recipes";
// let promise=fetch(URL);
// console.log(promise);
let parafetch=document.querySelector("p");
let butn=document.querySelector("#btn");
//json
//Fetch API with async await
const getdata = async()=>{
  console.log("getting data...");
  let response= await fetch(URL);
  console.log(response);//JSON format me hai
  // console.log(response.status);
  let data=await response.json();
  parafetch.innerText=data.recipes[1].name;
  
}
butn.addEventListener("click",getdata); 
// getdata();