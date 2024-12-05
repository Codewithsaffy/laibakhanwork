function countvowels(str){
  let count=0;
  for (let char of str){
    if(char==="a" || char==="e" || char==="i" || char==="o" || char==="u" || char==="A" || char==="E" || char==="I" || char==="O" || char==="U"){
      count++;
    }
  }
  console.log(count);
}
countvowels("laiba ");
//arrow function se bhi kar sakte hai
countvowels=(str)=>{
  let count=0;
  for (let char of str){
    if(char==="a" || char==="e" || char==="i" || char==="o" || char==="u" || char==="A" || char==="E" || char==="I" || char==="O" || char==="U"){
      count++;
    }
  }
  console.log(count);
}
countvowels("laiba ");



Array =[2,4,3,21,34,7,5,9,8]
Array.forEach((element)=>{
  element**=2;//element*element bhi likh sakte hai
  console.log(element);
})
//or arrow for each bfunction ko hum is tarah bhi istamal kar sakte hai
Array1 =[2,4,3,21,34,7,5,9,8]
let b=((element)=>{
  element**=2;//element*element bhi likh sakte hai
  console.log(element);
})
Array1.forEach(b)


let arr=[78,98,93,94,99,45,76,92,43];
let largest=arr.filter((val)=>{
  return val>90;
})
console.log(largest);