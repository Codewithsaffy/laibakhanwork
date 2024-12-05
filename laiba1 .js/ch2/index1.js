// //arthi metic operators
// let a= 10;
// let b= 3;
// console.log("a+b=",a+b);
// console.log("a-b=",a-b);
// console.log("a*b=",a*b);
// console.log("a/b=",a/b);
// // modules operator jo bhi reminder bachta hai devide karwa ke
// console.log("a%b=",a%b);
// //exponentiation operator power ke leye istamal hota hai
// console.log("a**b=",a**b);
// // uniary operator
// //post
// //increment operator one add ho gai ga a me
// a++;
// console.log(a);
// //decrement operator one kum ho gai ga a me
// b--;
// console.log(b);
// //pre
// console.log(a++);// e phele a ki value hi likhe ga ani 10
// console.log(a);//pher a print kare ge to 11 ho ga
// console.log(++a);// e phele a ki value change ho gi ani 11

// //assignment operator
// let c=10;
// let d=10;
// let e=10;
// let f=10;
// let g=10;
// let h=10;
// c += 5; // c=c+5
// d -= 5; // c=c-5
// e *= 5; // c=c*5
// f /= 5; // c=c/5
// g %= 5; // c=c%5
// g **= 5; // c=c**5
// console.log(c);
// console.log(d);
// console.log(e);
// console.log(f);
// console.log(g);
// console.log(h);

// //comparative operator
// let x=10;
// let y=20;
// console.log("x==y",x==y);
// console.log("x!=y",x!=y);
// console.log("x===y",x===y);// ye variable bhi dekhta hai ke string hai ya kya hai
// console.log("x!==y",x!==y);// ye variable bhi dekhta hai ke string hai ya kya hai
// console.log("x>y",x>y);
// console.log("x<y",x<y);
// console.log("x>=y",x>=y);
// console.log("x<=y",x<=y);

// //logical operator
// let m=10;
// let n=20;
// console.log("m>5 && n<30",m>5 && n<30);
// console.log("m>5 || n<30",m>5 || n<30);// pipe symbol
// console.log("!(m>5 && n<30)",!(m>5 && n<30));// logical not hamesha true ko false aur false ko true bana dega

// //conditional operator
// let mode="dark";
// let color;
// if(mode==="dark"){
//   color="black";
// }
// if(mode==="light"){
//   color="white";
// }
// console.log(color);

let mode="blue";
let color;
if(mode==="dark"){
  color="black";
}
else{
  color="white";
}
console.log(color);

//ternary operators
let age=20;
let result = age>18? "eligible":"not eligible";//?ye lagane ka mutlub agar age 18 se bara hai yani (true) hai to eligible hoga aur agar age 18 se chota hai yani (false) hai to not eligible hoga
console.log(result);
//or is tarike se bhi likh sakte hai
age>18? console.log ("eligible"):console.log("not eligible");