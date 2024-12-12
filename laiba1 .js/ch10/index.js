// // this is called synchronous program
// console.log("one");
// console.log("two");


// //this is called asynchronous program
// //settimeout ye batata hai hai ke kitne der bad code ko exicute hona hai
// function hello(){
//   console.log("hello");
// }
// setTimeout(hello,4000); //2s is equal to 2000ms
// //is ko hum is tarah bhi ker sakte hai
// setTimeout(()=>{
//   console.log("hello");
//   hello},4000); 
  
//   console.log("three");

//   // callabck function
//   // function sum(a,b){
//   //   console.log(a+b);
//   // }
//   // function calculator(a,b,sum1){
//   //   sum1(a,b);
//   // }
//   // calculator(10,20,sum);
//   function calculator(a,b,sum1){
//     sum1(a,b);
//   }
//   calculator(10,20,(a,b)=>{
//     console.log(a+b);
//   });



  //calllback hell
  //nesting
  //yani aik ke ander aik pher us ke under
  let age=0;
  if (age>=18){
    if (age>=25){
      console.log("you can drive");
    }
    else{
      console.log("you can not drive");
    }
  }
  else{
    console.log("you can not drive");
  }

  for(let i=0;i<10;i++){
    for(let j=0;j<10;j++){
      console.log(i,j);
    }
  }