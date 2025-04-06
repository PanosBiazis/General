use std::io::{self, Write};
use std::thread::sleep;
use std::time::Duration;
// use std::process::Command;

// use math::math_op;
// use crate::math;
// use script_mode;
// use gui_mode;
// use mode_selector;
// use prime_program;
// use math::go_menu_menu_or_exit;
// use math::add;
// use math::subtract;
// use math::multiply;
// use math::divide_with_quotient;
// use math::divide_with_remainder;
// use java_program_menu;
// use python_program_menu;
// use csharp_program_menu;
// use crate::main;

use crate::math::math_op;
use crate::math::add;
use crate::math::subtract;
use crate::math::multiply;
use crate::math::divide_with_quotient;
use crate::math::divide_with_remainder;
use crate::math::go_menu_menu_or_exit;
use crate::script_mode;
use crate::mode_selector;
use crate::gui_mode;
use crate::java_program_menu;
use crate::python_program_menu;
use crate::csharp_program_menu;
use crate::prime_program;
use crate::connection_dev::connection_dev_menu;
// use crate::web_edition::web_menu;
use crate::web_edition::web_menu;


pub fn print_invalid_choice_and_restart_math() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    math_op(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_add() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    add(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_sub() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    subtract(); // Restart the mode_selector function
}


pub fn print_invalid_choice_and_restart_mul() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    multiply(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_divq() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    divide_with_quotient(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_divr(){

    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    divide_with_remainder(); // Restart the mode_selector function
}

pub fn print_inv_choice_rest_go_menu(){

    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    go_menu_menu_or_exit(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_sm() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    script_mode(); // Restart the script_mode function
}

pub fn print_invalid_choice_and_restart() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    mode_selector(); // Restart the mode_selector function
}

pub fn print_invalid_choice_and_restart_gui() {
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    gui_mode(); // Restart the gui_mode function
}

pub fn print_invalid_choice_and_restart_java_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    java_program_menu();
}

pub fn print_invalid_choice_and_restart_python_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    python_program_menu();
}

pub fn print_invalid_choice_and_restart_csharp_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    csharp_program_menu();
}


pub fn print_invalid_choice_and_restart_prime_program_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    prime_program();
}

pub fn print_invalid_choice_and_restart_connection_dev_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    connection_dev_menu();
}

pub fn print_invalid_choice_and_restart_web_menu(){
    println!("Invalid choice. Please try again.");
    io::stdout().flush().unwrap(); // Ensure the message is printed immediately
    sleep(Duration::from_secs(2)); // Wait for 2 seconds
    // web_edition::web_menu();
    web_menu();
}