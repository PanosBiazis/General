//file address F:\panag\Documents\AAP\source\rust\src\connection_dev.rs


use std::io::{self, Write};
// use std::process::Command;
// use std::process::Stdio;


use crate::{prime_program,exit_program};
use crate::invalid_choice::print_invalid_choice_and_restart_connection_dev_menu;
// use crate::connection_dev_Cl; //F:\panag\Documents\AAP\source\rust\src\connection_dev_Cl.rs

// use crate::connection_dev_Ad; //F:\panag\Documents\AAP\source\rust\src\connection_dev_Ad.rs


// mod connection_dev_Cl;
// mod connection_dev_Se;

// use connection_dev_Cl::*;
// use connection_dev_Se::*;


// mod connection_dev_Cl;
// mod connection_dev_Se;

use crate::connection_dev_cl::main as cl_main;
use crate::connection_dev_se::main as se_main;
// use crate::main_funcs::{prime_program, exit_program};


pub async fn connection_dev_menu() {
    let mut stdout = io::stdout();
    let mut input=String::new();
    println!("Select: \n 1. if you are server \n 2. if you are client \n 3. Pevious menu \n 4. Exit");
    
    print!("Select: ");

    stdout.flush().expect("Failed to flush stdout");

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");

    println!("You entered: {}", input);

    match input {
        1 => se_main().expect("Error in connection_dev_Se::main"),
        2 => cl_main().expect("Error in connection_dev_Cl::main"),
        3 => prime_program().await,
        4 => exit_program().await,
        _ => print_invalid_choice_and_restart_connection_dev_menu(),
    }

}
