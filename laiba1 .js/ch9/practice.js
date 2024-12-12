let DATA ="My data";
class user{
  constructor(name,email){
    this.name=name;
    this.email=email;
  }
  viewData(){
    console.log(DATA);
  }
}
class admin extends user{
  constructor(name,email){
    super(name,email);
  }
  editData(){
    DATA="this is edited data";
  }
}
let student1 =new user("laiba","2dX4q@example.com");
let student2 =new user("Areeba","2738bxomsnadh.com");
student1.viewData();
student2.viewData();
console.log(student1,student2);

let admin1 =new admin("laiba","2dX4q@example.com");
console.log(admin1);
admin1.editData();
admin1.viewData();



//error handling
let a=4;
let b= 5;
console.log("a:",a);
console.log("b:",b);
console.log("a+b:",a+b);
//agar hame lage ke kisi codee me error a sakta hai to try ka istmal kare ge
try{
  console.log("a-b:",a-c);
}
catch(err){
  console.log(err);
}
console.log("a-b:",a-b);
console.log("a*b:",a*b);
console.log("a/b:",a/b);