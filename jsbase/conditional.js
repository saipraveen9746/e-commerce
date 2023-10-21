
// let age = 22
// let aggeee;
// if (age < 18) {
//     aggeee = "Minor";
//   } else {
//     aggeee = "Adult";
//   }

// console.log(aggeee);

// let x = 20;
// let y = 30;

// if (x>y){
//     console.log("x is greater than y");
// }
// else{
//     console.log("y is greater than x");
// }


// let z = prompt("enter the z value");
// let z1 = prompt("enter the z1 value");

// if (z>z1){
//     console.log("z is greater than z1");
// }
// else{
//     console.log("z1 is greater than z")
// };

// switch (new Date().getDay()){
//     case 0:
//         day = "Sunday";
//         break;
//     case 1:
//         day = "Monday";
//         break;
//     case 2:
//         day = "Tuesday";
//         break;
//     case 3:
//         day = "Wednesday";
//         break;
//     case 4:
//         day = "Tuesday";
//         break;
//     case 5:
//         day = "Friday";
//         break;
//     case 6:
//         day = "Saturday";
//         break;


// }
// console.log("Today is "+day);



// let Mark1 = prompt("Enter the mark");


// if (Mark1>=70 && Mark1<=80){
//     console.log("A+");
// }
// else if(Mark1>=60 && Mark1<=69){
//     console.log("B+");
// }
// else if (Mark1>=50 && Mark1 <=59){
//     console.log("C+");
// }
// else if (Mark1>=40 && Mark1 <=49){
//     console.log("D+");
// }
// else{
//     console.log("Fail");
// }

// let Mathsmark = prompt("Enter the mathsmark");
// let PhyMark = prompt ("Enter the physicsmark");

// if (Mathsmark>=80 || PhyMark>=80){
//     console.log("Pass");

// }
// else {
//     console.log("Fail");
// }




 


let num = prompt("enter the string");

let re = num.split('').reverse().join('');

if (re==num){
    console.log("Palindrome");
}
else{
    console.log("Not palindrome");
}





// let num = prompt("Enter the number");
// let rev = parseInt(num.toString().split('').reverse().join(''));

// if (rev==num){
//     console.log("Palindrome");
// }
// else {
//     console.log("not palindrome");
// }





let n = prompt("enter the num"); 
  
function factorial(n) { 
    let ans = 1; 
      
    if(n === 0)
        return 1;
    for (let i = 2; i <= n; i++) 
        ans = ans * i; 
    return ans; 
}
  
console.log(factorial(n));




