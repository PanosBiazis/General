use std::io::{self, Write}; // Import the io module and the Write trait
// use std::thread::sleep; // Import the sleep function
// use std::time::Duration; // Import the Duration struct

use crate::prime_program;


// use invalid_choice::print_invalid_choice_and_restart_math;

// use crate::invalid_choice;

// use invalid_choice::print_inv_choice_rest_go_menu;
// use invalid_choice::print_invalid_choice_and_restart_add;
// use invalid_choice::print_invalid_choice_and_restart_sub;
// use invalid_choice::print_invalid_choice_and_restart_mul;
// use invalid_choice::print_invalid_choice_and_restart_divq;
// use invalid_choice::print_invalid_choice_and_restart_divr;
// use crate::invalid_choice::print_invalid_choice_and_restart;
use crate::invalid_choice::print_invalid_choice_and_restart_math;
use crate::invalid_choice::print_inv_choice_rest_go_menu;
use crate::invalid_choice::print_invalid_choice_and_restart_add; 
use crate::invalid_choice::print_invalid_choice_and_restart_sub;
use crate::invalid_choice::print_invalid_choice_and_restart_mul;
use crate::invalid_choice::print_invalid_choice_and_restart_divq;
use crate::invalid_choice::print_invalid_choice_and_restart_divr;


fn exit_program() {
    println!("Exiting program...");
    std::process::exit(0);
}



pub fn math_op() {
    let mut input = String::new();

    println!("Select an operation:");
    println!("1. Add");
    println!("2. Subtract");
    println!("3. Multiply");
    println!("4. Divide with quotient");
    println!("5. Divide with remainder");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    match input {
        1 => add(),
        2 => subtract(),
        3 => multiply(),
        4 => divide_with_quotient(),
        5 => divide_with_remainder(),
        _ => print_invalid_choice_and_restart_math(),
    }
}



pub async fn go_menu_menu_or_exit(){

    let mut input2 = String::new();

    println!("1.Do you want to choose another math operation?");

    println!("2.Do you want to do something else?");
    
    println!("3. Exit");
    
    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    
    io::stdin().read_line(&mut input2).expect("Failed to read line");

    let input2: u32 = input2.trim().parse().expect("Please enter a number");
    
    println!("You entered: {}", input2);

    match input2 {
    
        1 => math_op(),

        2 => prime_program().await,
    
        3 => exit_program(),
    
        _ => print_inv_choice_rest_go_menu(),
    
    }


}

pub fn add() {
    let mut num_str = String::new();
    let mut num2_str = String::new();
    let mut input = String::new();

    print!("Enter the first number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num_str).expect("Failed to read line");

    print!("Enter the second number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_str).expect("Failed to read line");

    let num = num_str.trim().parse::<f64>().expect("Please enter a valid number");
    let num2 = num2_str.trim().parse::<f64>().expect("Please enter a valid number");

    let sum = num + num2;
    println!("The sum of {} and {} is {}", num, num2, sum);

    println!("Do you want to continue add operation?(1.YES/2.NO)");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    if input == 1 {

        add();
    
    }
    
    else if input == 2 {
     
        go_menu_menu_or_exit();
    
    } 
    else {
    
        print_invalid_choice_and_restart_add();
    
    }
}

pub fn subtract() {
    let mut num_str = String::new();
    let mut num2_str = String::new();
    let mut input = String::new();


    print!("Enter the first number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num_str).expect("Failed to read line");

    print!("Enter the second number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_str).expect("Failed to read line");

    let num = num_str.trim().parse::<f64>().expect("Please enter a valid number");
    let num2 = num2_str.trim().parse::<f64>().expect("Please enter a valid number");

    let difference = num - num2;
    println!("The difference of {} and {} is {}", num, num2, difference);

    println!("Do you want to continue sub operation?(1.YES/2.NO)");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    if input == 1 {

        subtract();
    
    }
    
    else if input == 2 {
     
        go_menu_menu_or_exit();
    
    } 
    else {
    
        print_invalid_choice_and_restart_sub();
    
    }
}

pub fn multiply() {
    let mut num_str = String::new();
    let mut num2_str = String::new();
    let mut input = String::new();


    print!("Enter the first number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num_str).expect("Failed to read line");

    print!("Enter the second number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_str).expect("Failed to read line");

    let num = num_str.trim().parse::<f64>().expect("Please enter a valid number");
    let num2 = num2_str.trim().parse::<f64>().expect("Please enter a valid number");

    let product = num * num2;
    println!("The product of {} and {} is {}", num, num2, product);

    println!("Do you want to continue mul operation?(1.YES/2.NO)");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    if input == 1 {

        multiply();
    
    }
    
    else if input == 2 {
     
        go_menu_menu_or_exit();
    
    } 
    else {
    
        print_invalid_choice_and_restart_mul();
    
    }
}

pub fn divide_with_quotient() {
    let mut num_str = String::new();
    let mut num2_str = String::new();
    let mut input = String::new();


    print!("Enter the first number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num_str).expect("Failed to read line");

    print!("Enter the second number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_str).expect("Failed to read line");

    let num = num_str.trim().parse::<f64>().expect("Please enter a valid number");
    let num2 = num2_str.trim().parse::<f64>().expect("Please enter a valid number");

    let quotient = num / num2;
    println!("The quotient of {} and {} is {}", num, num2, quotient);

    println!("Do you want to continue division(quotient) operation?(1.YES/2.NO)");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    if input == 1 {

        divide_with_quotient();
    
    }
    
    else if input == 2 {
     
        go_menu_menu_or_exit();
    
    } 
    else {
    
        print_invalid_choice_and_restart_divq();
    
    }
}

pub fn divide_with_remainder() {
    let mut num_str = String::new();
    let mut num2_str = String::new();
    let mut input = String::new();


    print!("Enter the first number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num_str).expect("Failed to read line");

    print!("Enter the second number:>> ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_str).expect("Failed to read line");

    let num = num_str.trim().parse::<f64>().expect("Please enter a valid number");
    let num2 = num2_str.trim().parse::<f64>().expect("Please enter a valid number");

    let remainder = num % num2;
    println!("The remainder of {} and {} is {}", num, num2, remainder);

    println!("Do you want to continue division(remainder) operation?(1.YES/2.NO)");

    print!("Select:>> ");

    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");
    println!("You entered: {}", input);

    if input == 1 {

        divide_with_remainder();
    
    }
    
    else if input == 2 {
     
        go_menu_menu_or_exit();
    
    } 
    else {
    
        print_invalid_choice_and_restart_divr();
    
    }
}
