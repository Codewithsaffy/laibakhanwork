// // prototypes in js
// const student = {
//   name: "laiba",
//   marks: 99,
//   fullmarks: function () {
//     console.log("marks =", this.marks); //yaha pe this ka mutlub hai student
//   },
// };
// // console.log(student);
// student.fullmarks();

// //__proto__
// const employee = {
//   calctex() {
//     console.log("the salary is 10%");
//   },
// };
// const laiba = {
//   salary: 100000,
// };
// const laiba1 = {
//   salary: 100000,
// };
// const laiba2 = {
//   salary: 100000,
// };
// const laiba3 = {
//   salary: 100000,
// };

// laiba.__proto__ = employee;
// laiba1.__proto__ = employee;
// laiba2.__proto__ = employee;
// laiba3.__proto__ = employee;

// console.log(laiba);
// console.log(laiba1);
// console.log(laiba2);
// console.log(laiba3);

// // laiba.calctex();
// // laiba1.calctex();
// // laiba2.calctex();
// // laiba3.calctex();

// //if the object and prototypes have same method then object method is used
// const employee1 = {
//   calctex() {
//     console.log("the salary is 10%");
//   },
// };
// const laiba4 = {
//   salary: 100000,
//   calctex() {
//     console.log("the salary is 20%");
//   },
// };
// laiba4.__proto__ = employee1;
// console.log(laiba4);
// laiba4.calctex(); //to yaha pe sirf laiba4 wala calcultax print ho ga
// //q ke apne properties apne method zyada nazdek hote hai

// // class in js
// class Toyotacar {
//   constructor(brand, mileage) {
//     console.log("creating a new car");
//     this.brandName = brand;
//     this.mileage = mileage;
//   }
//   start() {
//     console.log("the car is started");
//   }
//   stop() {
//     console.log("the car is stoped");
//   }
//   // setbrand(brand){
//   //   this.brandName=brand;
//   // } is ko hum is tarah bhi likh sakte hai
// }
// let fortuner = new Toyotacar("fortuner", 10); //new hamare leye aik object create karta hai classes ke through // yaha pe constructor print ho ga
// console.log(fortuner);
// // fortuner.setbrand("fortuner");
// fortuner.start();
// fortuner.stop();
// console.log(fortuner.brandName);

// //inheritance in js
// class parent {
//   hello() {
//     console.log("hello");
//   }
// }
// class chiled extends parent {}
// let obj = new chiled();
// obj.hello();

// //one more example
// class person {
//   constructor() {
//     this.species = "home species";
//   }
//   eat() {
//     console.log("eating");
//   }
//   sleep() {
//     console.log("sleeping");
//   }
// }
// class engineer extends person {
//   work() {
//     console.log("solve problem , write code");
//   }
// }
// class doctor extends person {
//   work() {
//     console.log("treat people");
//   }
// }
// let obj1 = new engineer();
// let obj2 = new doctor();
// obj1.eat();
// obj1.sleep();
// obj1.work();
// obj2.eat();
// obj2.sleep();
// obj2.work();
// console.log(obj1);

//child class ko hum code deride khete hai
// class persons {
//   constructor() {
//     this.species = "home species";
//   }
//   eat() {
//     console.log("eating");
//   }
// }
// class engineers extends persons {
//   constructor(branch) {
//     super(); //to invoke parent class constructor
//     this.branch = branch;
//   }
//   work() {
//     console.log("solve problem , write code");
//   }
// }

// let obj4 = new engineers("chemical engineer");
// console.log(obj4);

class person {
  constructor(name) {
    this.species = "home species";
    this.name = name;
  }
  eat (){
    console.log("eating");
  }
}
class engineers extends person {
  constructor(name) {
    super(name); //to invoke parent class constructor
  }
  work(){
    super.eat();
  }
}

let obj4 = new engineers("laiba");
console.log(obj4);
obj4.work();
