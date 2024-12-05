// // // for loop
// // for (let i=1;i<=10;i++){
// //   console.log("my name is laiba");
// // }

// // let sum=0;
// // for (let i=1;i<=10;i++){
// //   sum=sum+i;
// // }
// // console.log(sum);

// // // while loop
// // let i=1;
// // while(i<=10){
// //   console.log(i);
// //   i++;
// // }

// // do while loop
// let j=20;
// do{
//   console.log("apna collage");
//   j++;
// }while(j<=10);// do while loop mestatement correc tho ya na ho aik bar lazmi chale ga

// //for of loop
// let str="laiba";
// for (let char of str){//iteration bhi khete hai
//   console.log(char);
// }// for of loop me alag alag kar ke print hota hai

// //for in loop
// let student={
//   name:"laiba",
//   age:17,
//   marks:99.9
// }
// for (let key in student){
//   console.log(key , student[key]);
// }

// tempelate literal  important
let name=`laiba`;
console.log(name); // question a sakta hai jab hamare pass single or double code tha to bactic istamal karne ke kya arorat thi
console.log(`my name is ${name}`);//is ko hum direct bactic code laga kar print kare ge aur double code ko bar bar lagana parta hai ${name} is ko hum string interpolaion khete hai

//escape sequence
//\n new line
console.log("my name is \n laiba");

// \t tab space
console.log("my name is \t laiba");

//\t length meaik single character ki tarah count hote hai

//str.touppercase
let str="apna collage";
console.log(str.toUpperCase());

//lowercase
let str1="apna collage";
console.log(str1.toLowerCase());

//  important string are immutable in javascript 

//trim method starting and ending ke space ko khatam kar deta hai
let str2="    apna collage    ";
console.log(str2.trim());

// slice
let str3="apna collage";
console.log(str3.slice(0,3));

// .concat
let a="laiba";
let b="khan";
console.log(a.concat(b));//concat do string ko gorta hai

//.replace
let c= "hello";
console.log(c.replace("h","m"));//replace aik character ko dosre character se replace karta hai
// is ka mutlub agar aik chese do se ten bar hai to wo sirf aik ko replace kare ga

//.allreplace
let d= "hello";
console.log(d.replaceAll("l","p")) //is me l jitna bhi hai sub replace ho gai ga

//.carat
let e= "hello";
console.log(e.charAt(0));// ye batata hai ke konsa character kha hai




