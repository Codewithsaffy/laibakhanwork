//callback hell
//simple example
// function getData(data){
//   console.log(data);
// }
// getData("hello world");

//settimeout
// function getData(data){
//   setTimeout(()=>{
//     console.log(data);
//   },2000);
// }
// getData("hello world");


// //call back
// function getData(data ,getNextData){
//   setTimeout(()=>{
//     console.log(data);
//     if(getNextData) {
//       getNextData();
//     }
//   },2000);
// }
// // getData("hello world",getData("next data"));
// //is ko hum is tarah nahi likhe ge

// //is ko hum call back hell khete hai
// //pyramid of doom
// getData(1,()=>{
//   console.log("geting data 2...");
//   getData(2,()=>{
//     console.log("geting data 3...");
//     getData(3,()=>{
//       console.log("geting data 4...");
//       getData(4)
//     });
//   });
// })


//promises
// let promises=new Promise((resolve,reject)=>{
//   console.log("I am a promise");
//   // resolve("promise resolved");
//   reject("promise rejected");
// });
// console.log(promises);

// function getData(data ,getNextData){
//   return promises =new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//       console.log(data);
//       resolve("data resolved");
//       if(getNextData) {
//         getNextData();
//       }
//     },5000);
//   });
// }
// let fulfill=getData(193);
// console.log(fulfill);


// //.then
// const getPromise=(()=>{
//   return new Promise((resolve,reject)=>{
//     console.log("promise pendoing");
//     resolve("promise resolved");
//   });
// });
// let fulfill=getPromise();
// fulfill.then ((res)=>{
//   console.log("promise fulfiled",res);
// })

// // .catch
// const getPromises=(()=>{
//   return new Promise((resolve,reject)=>{
//     console.log("promise pendoing");
//     reject("promise rejected");
//   });
// });
// let fulfilled=getPromises();
// fulfilled.catch ((err)=>{
//   console.log("promise regected",err);
// })


//promise chain
// function asyncFun1(){
//   return new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//       console.log("data 1");
//       resolve("data 1 resolved");
//     },2000);
//   });
// }
// function asyncFun2(){
//   return new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//       console.log("data 2");
//       resolve("data 2 resolved");
//     },2000);
//   });
// }
// console.log("feetching 1...");
// let p1=asyncFun1();
// p1.then((res)=>{
//   console.log(res);
//   console.log("feetching 2...");
//   let p2=asyncFun1();
//   p2.then((res)=>{
//     console.log(res);
//   });
// });


//is ko hum is tarah bhi likh sakte hai


// console.log("feetching 1...");
// asyncFun1().then((res)=>{
//   console.log("feetching 2...");
//   asyncFun2().then((res)=>{
//   });
// });



// //example
// function getData(dataID){
//   return new Promise ((resolve,reject)=>{
//     setTimeout(()=>{
//       console.log("data",dataID);
//       resolve("success");
//     },2000);
//   });
// }

// getData(1).then((res)=>{
//   console.log(res);
//   getData(2).then((res)=>{
//     console.log(res);
//     getData(3).then((res)=>{
//       console.log(res);
//     })
//   })
// }) is ko hum is tarike se bhi  likhne ka traika

// console.log("getting data 1...");
// getData(1)
// .then((res)=>{
//     console.log("getting data 2...");
//     return getData(2)
//   })
//   .then((res)=>{
//     console.log("getting data 3...");
//   return getData(3)
//   })
//   .then((res)=>{
//     console.log(res);
//   })

//async await


// function api(dataID){
//   return new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//       console.log("weather data",dataID);
//       resolve("success");
//     },2000);
//   });
// }
// async function getweatherdata(){
//   await api(1);
//   await api(2);
//   await api(3);
// }
// getweatherdata();



function api(dataID){
  return new Promise((resolve,reject)=>{
    setTimeout(()=>{
      console.log("weather data",dataID);
      resolve("success");
    },2000);
  });
}
async function getweatherdata(){
  console.log("getting data 1...");
  await api(1);
  console.log("getting data 2...");
  await api(2);
  console.log("getting data 3...");
  await api(3);
  console.log("getting data 4...");
  await api(4);
  console.log("getting data 5...");
  await api(5);
  console.log("getting data 6...");
  await api(6);
  console.log("getting data 7...");
  await api(7);
}
getweatherdata();
// very simple 

//iife
// sirf aik bar exicute hota hai

(async function(){
  console.log("getting data 1...");
})
( function(){
  console.log("getting data 1...");
})
(()=>{
  console.log("getting data 1...");
})
//3 tarika hota hai is ko likhne ka