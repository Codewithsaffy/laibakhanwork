// // console.log ("Operators in js")
// // Arithmetic Operators
// let assignment = 1
// let a = 10;
// let b = 4;
// console.log ("a+b=",a+b)
// console.log ("a-b=",a-b)
// console.log ("a*b=",a*b)
// console.log ("a/b=",a/b)
// console.log ("a**b=",a**b)
// console.log ("a%b=",a%b)
// console.log ("++a=",++a)
// console.log ("a++=",a++)
// console.log ("--a=",--a)
// console.log ("a--=",a--)
// // Assignment Operators
// // assignment  += 8 
// // or
// assignment= assignment + 5 
// console.log (assignment)
// assignment -= 5
// console.log ("a is now =" ,a)
// assignment= assignment -5
// console.log ("a is now =" ,a)
// assignment *= 5
// console.log ("a is now =", a)

// // comparision operators
// let comp1= 2;
// let comp2=3;
// console.log ("comp1 == comp2 is",comp1==comp2)
// console.log ("comp1 != comp2 is",comp1!=comp2)
// console.log ("comp1 === comp2 is",comp1===comp2)
// console.log ("comp1 !== comp2 is",comp1!==comp2)
// console.log ("comp1 > comp2 is",comp1>comp2)
// console.log ("comp1 < comp2 is",comp1<comp2)
// // logicali operators
// let x = 5;
// let y= 6;
// console.log (x<y && x==5)
// console.log (x>y || x==6)
// console.log (!false)
// console.log (!true)

// conditional operators
// if(z>0){
//   alert ("this is valid age");
// }
// else{
//   alert ("this is not valid age");
// }
let z = prompt("Hey whats your age?");
z = Number.parseInt(z)//converting string to number
if(z<0){
  alert ("this is not valid age");
}
else if(z<9){
  alert ("you are kid");
}
else if(z<18 && z>=9){
  alert ("you are kid but you can drive");
}
else{
  alert ("you are drive above 18");
}
console.log ("Done")
console.log ("you can",(z<18)?"drive":"not drive")

const variable = prompt ('Enter a color');
switch (variable){
  case 'red':
    console.log ('red is red');
    break;
  case 'pink':
    case 'yellow':
    console.log ('pink and yellow are pink and yellow');
    break;
    default:
    console.log (' this color is not in our list');
}
