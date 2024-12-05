let num = prompt("Enter a number");
if (num % 5 ===0){
  console.log("The number is multiple of 5");
}
else{
  console.log("The number is not multiple of 5");
}

let grade = prompt("Enter your marks");
if (grade >= 90 && grade <= 100){
  console.log("Grade A");
}
else if (grade >= 80 && grade <= 89){
  console.log("Grade B");
}
else if (grade >= 60 && grade <= 79){
  console.log("Grade C");
}
else if (grade >= 50 && grade <= 59){
  console.log("Grade D");
}
else{
  console.log("Grade F");}