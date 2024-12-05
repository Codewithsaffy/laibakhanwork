//arrays
// arrays javascript ke andar aik object hoti hai
//arrays ke andar key ki jaga index hota hai
//arrays wo hota hai ke hum chate to hai ke aik sath ho aur aik hi nam ho to hum array banane ko prefer karte hai
let marks=[1,2,3,4,5];
console.log(marks);
console.log(marks.length);//length array ke andar property hoti hai

let a=["laiba","khan","areeba","yousuf","yousuf"];
console.log(a);
//arrays ke andar hum value bhi change kar sakte hai
a[0]="laiba khan";
console.log(a);
// arrays mutable hoti hai important

//arrays for loop
let b=["laiba","khan","areeba","yousuf","yousuf"];
for (let i=0 ;i<b.length;i++){
  console.log(b[i]);
}

//arrays for of loop
let c=["laiba","khan","areeba","yousuf","yousuf"];
for (let char of c){
  console.log(char.toUpperCase());
}

// /arrays method
// push method end me add karega
let food_items=["biryani","potato","chines","motton","chicken"]
food_items.push("chips","burger");
console.log(food_items);
//pop method end me pop karega
let food=["biryani","potato","chines","motton","chicken"]
let deleteditem=food.pop();
console.log(food);
console.log(deleteditem);
//to string method
// array kosting me convert karneka tareka
let item=["biryani","potato","chines","motton","chicken"]
console.log(item.toString());

//concat method
let item1=["biryani","potato","chines","motton","chicken"]
let item2=["biryani","potato","motton"]
let item3=["biryani","chines","motton","chicken"]
let item4=item1.concat(item2,item3);
console.log(item4);

//unshift method start me add karega
let item5=["biryani","potato","chines","motton","chicken"]
item5.unshift("chips","burger");
console.log(item5);
//shift method start me pop karega
let item6=["biryani","potato","chines","motton","chicken"]
item6.shift();
console.log(item6);

//slice method
let item7=["biryani","potato","chines","motton","chicken"]
let item8=item7.slice(1,4);
console.log(item8);

//splice method
//splice method phelehum batai ge ki konsa index pher waha se kitna delet karna hai pher kya add karna hai
let item9=["biryani","potato","chines","motton","chicken"]
item9.splice(1,2,"chips","burger");
console.log(item9);





