use std::fmt;


fn main(){
    println!("Hello World!");//comments
    /*comments */
    /*
    In programming,variables act as containers that store values.
    These values can be anything, from numbers, to text or 
entire functions.
     */

    let _my_container = 21;//variable
    let _container1 = "Hello";//string
    let _container2 = true;//boolean
    let _container3 = 21.0;//float type

    /*If you know other programming languages, like C++, java, 
you need to declare variable types or data types. 

But in Rust, you must have noticed we do not need to 
declare any variable types. 

The Rust compiler can automatically detect the data type of 
the variable, based on the value assigned to it. 

Making it easy for the programmer, to store different types 
of values in variables without declaring the data types.


In Rust, by default, variables are immutable. 

In other words, the variable's value cannot be changed once 
a value is assigned to a variable name. 

Unlike other programming languages, this is a unique feature of Rust


*/

//exaple to print a variable value using Rust
let price = 150;

println!("The price is {}", price);
// price = 450;
// println!("The price changed is {}", price);
// error[E0384]: cannot assign twice to immutable variable `price`
//   --> rust.rs:42:1
//    |
// 39 | let price = 150;
//    |     -----
//    |     |
//    |     first assignment to `price`
//    |     help: consider making this binding mutable: `mut price`
// ...
// 42 | price = 450;
//    | ^^^^^^^^^^^ cannot assign twice to immutable variable
/*In Rust, Variables are immutable by default. 

To make a variable mutable, we use prefix, mut keyword 
before variable name. 

The value of a mutable variable can be changed. */

let mut price2 = 150;

println!("The price is {}", price2);

price2 = 450;

println!("The price changed is {}", price2);


//conditions

if 3 < 5{
    println!("Three is less than five");
}
else {
    println!("Three is not less than five");
}

let a = 10;

let b = 20;

if a > b {
    println!("a is greater than b");
}
else if a < b {
    println!("a is less than b");
}
else {
    println!("a is equal to b");
}

//Loops
let mut count =  0;

loop {

    count=count+1;

    println!("{} Hello World",count);

    if count == 10{

        break;

    }

}

count=3;

while count !=0{

    println!("{}!",count);

    count=count-1;

}

println!("BOOM!!!");

for x in 1..11{

    println!("x is {}",x);

}

let a =[10,20,30,40,50,60,70,80,90,100];

for element in a.iter() {

    println!("The value is:{}",element);

}

//Array is a collection of values of the same data type.
//In an array, element values can be updated or modified but cannot be deleted.

let mut arr = [24,12,4];
//24 is index 0
//12 is index 1
//4 is index 2

println!("array is {:?}",arr);

println!("The value of first index is {}",arr[0]);

println!("array size is {}",arr.len());

arr[1]=0;

println!("{:?}",arr);

let _arr2=[10,20,30,40,50,60,70,80,90,100];

for element in a.iter(){

    println!("The value is : {}",element);

}

//A tuple is a collection of values of dfferent types
//A tuple is a fixed size collection of values of different types

let tup = (20,25,30,35);

println!("tup is {:?}",tup);

let tup2 = (10,"Rust",3.4,false);

println!("tup2 is {:?}",tup2);

println!("The third index of tuple2 is {}",tup2.2);

//Vector is a resizable array
//vector allow you to store more than one value in a single data structure.
//Vector is a collection of values of the same data type
//Vector can be used to implement a stack
// const T:i32 = 10;

// let v: Vec<T> = Vec::new();

let mut v: Vec<i32> = Vec::new();
println!("v is {:?}",v);
v.push(20);
v.push(6);
v.push(35);
v.push(74);
let mut v2 = vec![1,2,3,4];

println!("new v is {:?}",v);
println!("v2 is {:?}",v2);
v2.extend([20, 6, 35, 74]);
println!("new v2 is {:?}",v2);
println!("The third index of vector is {}",v[2]);
v2.remove(3);
println!("new v2 is {:?}",v2);
println!("size of vector is : {}",v2.len());
// A string is a data type used in programming to store text, 
// they are written inside double quotes. 

// A “string” is a sequence of characters, consisting of a letter 
// or a number, or even a special character. Let us learn more 
// about strings in Rust.

//String Literal
//String Literal (&str) are used when the value of a string is known at compile time.
//String Literal are a set of characters, which are stored into a variable.

let we_are:&str = "Programming Hub";

println!("We are : {}",we_are);

//String Object

//The String Object type is provided in the Standard Library.

//Unlike string literal, The string object type is not a part of the core language.

// To create a String object, we can use any of the following 
// syntax: 

// String::new() 

// The above syntax creates an empty string.

// We can also use String::from() keyword to declare a string in 
// Rust 

// let hello = String::from("Hello, world!"); 

// This creates a string with some default value passed as a 
// parameter to the from() method. 

// Our string “Hello, World” is stored in a variable hello.

let hello = String::from("Hello, world!"); 

println!("{}",hello);

//Length of the string

let hello2 = String::from("Hello, Rusty!");

println!("length of the string is : {}",hello2.len());

//Append string

let mut hello3 = String::from("Hello, ");

println!("{}",hello3);

hello3.push('W');

println!("{}",hello3);

hello3.push_str("orld!");

println!("{}",hello3);

//Replace String

let name1 = "Hello Rusty ,Hello!".to_string();

println!("{}",name1);

let name2 = name1.replace("Hello","Hi"); //find and replace

println!("{}",name2);

//String Concatenation

let a = "Programming".to_string();

println!("{}",a);

let b = "Hub".to_string();

println!("{}",b);

let c = a +" "+ &b;

println!("{}",c);

//Ownership

// Ownership is Rust’s most unique feature, and it enables 
// Rust to make memory safety guarantees without needing a 
// garbage collector. 

// Therefore, it’s important to understand how ownership 
// works in Rust.

// First, let’s take a look at the ownership rules. Keep these 
// rules in mind as we work through the examples that 
// illustrate them: 

// 1. Each value in Rust has a variable that’s called its owner. 
//Every data stored in Rust will have an owner associated with it.

// 2. There can only be one owner at a time. 

// 3. When the owner goes out of scope, the value will be dropped.

// Two variables cannot point to the same memory location. 

// The variables will always be pointing to different memory 
// locations.

// The ownership of value can be transferred by: 

// ¢ Assigning value of one variable to another variable. 

// ¢ Passing value to a function. 

// ¢ Returning value from a function.

//Assigning value of one variable to another variable.

// The key selling point of Rust as a language is its memory 
// safety. 

// Memory safety is achieved by tight control on who can use 
// what and when restrictions.

// let v3 = vec![1,2,3];

// let v4 = v3;

// println!("{:?}",v4);

// The idea of ownership is that only one variable binds to 
// a resource, either v binds to resource or v2 binds to the 
// resource.

// The above example throws an error. 

// This is because the ownership of the resource is transferred 
// to v2. 

// It means the ownership is moved from v to v2 (v2=v) and v is 
// invalidated after the move.

// Passing value to a function. 

// let v3 = vec![1,2,3]; //vector v3 owns the object in heap

// let v4 = v3; //moves ownership to v4

// display(v2);//v4 is moved to display and v4 is invalidated

// println!("In main {:?}",v4); //v4 is No longer usable here

// fn display(v4){
//     println!("inside display {:?}",v4);
// }   

// Passing a variable to a function will move or copy, just as 
// assignment does. 

// If we tried to use v after the call to display, Rust would throw 
// a compile-time error.

// Returning value from a function.

// Taking ownership and then returning ownership with every 
// function is a bit tedious. 

// What if we want to let a function use a value but not take 
// ownership? 

// It’s quite annoying that anything we pass in also needs to 
// be passed back if we want to use it again, in addition to any 
// data resulting from the body of the function that we might 
// want to return as well.

// let v3 = vec![1,2,3]; //vector v3 owns the object in heap

// let v4 = v3; //moves ownership to v4

//let v4_return = display(v4);

// println!("{:?}",v4_return);

// fn display(v) -> Vec {
//     println!("inside display {:?}",v); //returning same vector

// }

// Ownership passed to the function will be invalidated as 
// function execution completes. 

// One work around for this is let the function return the owned 
// object back to the caller.

//Functions

//Functions are a set of instructions which perform a specific task and can be reused multiple times.

// Rust code uses snake case as the conventional style for 
// function and variable names. 

// Inthe snake case, all letters are lowercase and underscores 
// separate words. 

// For example if you want to name a function print hello we 
// will write it as: print_hello().
// Rust doesn’t care where you define your functions, only that 
// they’re defined somewhere.

print_hello();//call the function

print_values(10);//call the function

print_values2(10,20);//call the function

//Enumerations

// Enumerations serve the purpose of representing a group of 
// named constants in a programming language.

// For example the 4 suits in a deck of playing cards may be 
// 4 enumerators named Club, Diamond, Heart, and Spade, 
// belonging to an enumerated type named Suit. 

// Other examples include natural enumerated types (like the 
// planets, days of the week, colors, directions, etc.). 

// Enums allow you to define a type by enumerating its 
// possible variants.

// First, we'll define and use an enum to show how an enum 
// can encode meaning along with data. 

// Enums are a feature in many languages, but their 
// capabilities differ in each language. 

// Rust’s enums are most similar to algebraic data types in 
// functional languages, such as F#, OCaml, and Haskell.

// In Rust programming, when we have to select a value from a 
// list of possible variants we use enumeration data types. 

// An enumerated type is declared using the enum keyword. 
// Following is the syntax of enum: 

// enum enum_name { 
// variant1, 
// variant2, 
// variant3 

// Different variants are written inside the enum, separated 
// with commas (,).
println!("roses are {}",Color::Red);

println!("violets are {}",Color::Blue);

println!("leaves are {}",Color::Green);

//Match Statement and Enum

print_size(CarType::SUV);

print_size(CarType::Hatch);

print_size(CarType::Sedan);
}

enum CarType {
    Hatch,
    Sedan,
    SUV,
}

fn print_size(car:CarType){
    match car{

        CarType::SUV =>println!("Large sized car"),
    
        CarType::Hatch =>println!("Small sized car"),
    
        CarType::Sedan =>println!("Medium sized car"),

    }

}




enum Color {
    Red,
    Green,
    Blue
}

impl fmt::Display for Color {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            Color::Red => write!(f, "Red"),
            Color::Green => write!(f, "Green"),
            Color::Blue => write!(f, "Blue"),
        }
    }
}

fn print_hello(){

    println!("Hello, World!");
}

fn print_values(x:i32){

    println!("The value of x is: {}",x);
}

fn print_values2(x:i32,y:i32){

    println!("The value of x is: {}",x);

    println!("The value of y is: {}",y);
}