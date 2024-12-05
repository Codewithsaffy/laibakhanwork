// // // function
// // //{}is ka mutlub hota hai block of code
// // //redundancy yani repeat hona 
// // //function ke andar jo input hota hai us ko parameter khete hai
// // function myfun(msg){
// //   console.log("my name is laiba");
// //   console.log(msg);
// // }
// // myfun("I LOVE JS");//is ko hum argument khete hai
// // // parameter aur arrgument same kam karta hai

// // function add(a,b){
// //   console.log(a+b);
// // }
// // add(10,20);

// // //return statement
// // function sum(x,y){
// //   let z=x+y;
// //   return z;
// // }
// // console.log(sum(10,20));
// // //aise bhi return ka istamal kar sakte hai
// // //hare function ke go parameter hota hai wo like local variables of function hote hai wo sirf block tak zinda hote hai

// // // function sum(a,b){
// // //   return a+b;
// // // }

// // // =>arrow function
// // //modern js
// // const ad=(a,b)=>{
// //   console.log(a+b);
// // }
// // ad(1,2);


// // const mul=(a,b)=>{
// //   console.log(a*b);
// // }
// // mul(1,2);
// // //is ko hum return se bhi likh sakte hai
// // const mult=(a,b)=>{
// //   return a*b;
// // }
// // console.log(mult(1,2));

// // const a=()=>{
// //   console.log("hello");
// // }
// // a();
// // //is ko hum is tarah bhi likh sakte hai
// // //per zyada acha hai ke hum phele wale ki tarah likhe
// // const b=()=> console.log("hello");
// // b();

// // //  for each loop in array
// // // ye aik method hai
// // // for each arrayke andar se value ko return karta hai
// // // arrow
// // let arr=[1,2,3,4,5];
// // arr.forEach((element)=>{
// //   console.log(element);
// // })
// // //or aise bhi likh sakte hai
// // let arr1=["laiba","khan","areeba","yousuf"];
// // arr1.forEach(function myfun(element){
// //   console.log(element);
// // })
// // //is ko is leye istamal karte hai ke hame sare array ko uppercase ye sab lagana hota hai to is leye istamal karte hai
// // //index bhi print karwana ho  to karwa sakte hai
// // //array ko bhi print karwa sakte hai
// // let arr2=["laiba","khan","areeba","yousuf"];
// // arr2.forEach(function myfun(element,index,arr){
// //   console.log(element.toUpperCase(),index,arr);
// // })

// // // important for each ko hum higher order function / higher order method bhi khete hai
// // //jis bhi function me hame call back hota hoa dikhe wo higher order fun/ higher order method hai


// // //for each or map dono aik hi kam karta hai lekin map aik naya array bana ke deta hai lekin for each aik naya array nahi bana ke deta hai
// // // map
// // let arr3=["laiba","khan","areeba","yousuf"];
// // arr3.map(function myfun(element,index,arr){
// //   console.log(element.toUpperCase(),index,arr);
// // })


// //.filter
// let ar=[1,2,3,4,5,6,7,8,9,10];
// let even=ar.filter((val)=>{
//   return val%2===0
// })
// console.log(even);
// //or agar not equal to likhe ge to sari ki sari odd no me mile gi
// let are=[1,2,3,4,5,6,7,8,9,10];
// let odd=are.filter((val)=>{
//   return val%2!==0
// })
// console.log(odd);
// //aise bhi ker sakte hai ke koi bhi value is no se bari ho
// let ars=[1,2,3,4,5,6,7,8,9,10];
// let greater=ars.filter((val)=>{
//   return val>3
// })
// console.log(greater);

// //.reduce
// let arra=[1,2,3,4,5];
// let sum=arra.reduce((res,cur)=>{
//   return res+cur
// })
// console.log(sum);

// let arras=[1831,20983,370914,443189,514798];
// let largest=arras.reduce((res,cur)=>{
//   return res>cur ? res : cur
// })
// console.log(largest);

// let n=prompt("Enter a number");
let n=5
let arr=[];
for (let i=1; i<n;i++){
  arr[i - 1]=i;
}
console.log(arr);
let sum= arr.reduce((res,cur)=>{
  return res+cur
})
console.log(sum);

let mul= arr.reduce((res,cur)=>{
  return res*cur
})
console.log(mul);// is ko hum factorial bhi khete hai