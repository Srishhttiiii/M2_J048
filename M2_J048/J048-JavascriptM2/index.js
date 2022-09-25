//JavaScript is a dynamic lang
//Declaring a variable
//Always terminate lines in JS with a semicolon (;)
//Variables cannot start with a number, contain a space or a hyphen
//Variables are case-sensitive

let a = 'hahaha';
console.log(a);

//Constants
const interestRate= 1;
console.log(interestRate);

//Data Types -> Primitive (Value) Type includes String, Number, Boolean, Null, Undefined

let name = 'Srishti'; //string
let age = '19'; //number
let lol = true; //boolean
let lmao = undefined; //undefined
let zero = null; //null

//Reference Types ->  Objects, Arrays, Functions

//Objects

let person = {
    name: 'yes',
    age: 15
};

//Dot Notation 
person.name = 'Isa';

//Bracket Notation
person['name']= 'Anni';

console.log(person);


//Arrays

let selectedColours = ['red', 'green', 'blue'];
console.log(selectedColours[1]);


//Addition Function
// store input numbers
const num1 = parseInt(prompt('Enter the first number '));
const num2 = parseInt(prompt('Enter the second number '));

//add two numbers
const sum = num1 + num2;

// display the sum
console.log(`The sum of ${num1} and ${num2} is ${sum}`);
