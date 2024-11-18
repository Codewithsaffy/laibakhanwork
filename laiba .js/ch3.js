// for(let i=0;i<15;i++ ){
//   console.log(i+1)
// }
// let n = prompt("Enter a number");
// Number.parseInt(n);
// let n = 2
// let sum = 0;
// for (let i = 0; i < n; i++) {
//   sum += i + 1;
// }
// console.log("sum " + n + " natural number is " + sum);
/*
let obj = {
  name: "laiba",
  age: 22,
  class: 11,
}
//for in loop
for(let key in obj){
  console.log("Value of " + key + " are " +obj[key])
}
//for of loop
for(let key of "age"){
  console.log("Value of " + key + " are " +obj[key])
}*/
//while loop
/*
let a = prompt("Enter a number");
Number.parseInt(a);
let i =0
while(a<i){
  console.log(i)
  i++;
}
*/
//do while loop
/*
let a = prompt("Enter number");
a = Number.parseInt(a);
let i =10
do {
  console.log(i)
  i++;
}while(i<a)
*/
const sum =(x,y)=>{
  return Math.round(1+(x-y)/2); 
}
function add(x,y){
  return Math.round(1+(x+y)/2);
}
const hellow =()=>{
  console.log("how are you");
  return ("hi");
}
let a = 1;
let b = 2;
let c = 3;
 let v =hellow();
 console.log(v);
console.log("one plus average of",sum(a,b));
console.log("one plus average of",add(a,b));
console.log("one plus average of",add(b,c));
console.log("one plus average of",add(c,a));
