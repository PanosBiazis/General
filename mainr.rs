use std::io::{self, Write};
// use std::thread::sleep;
// use std::time::Duration;
use std::process::Command;
// use io::stdout;
// use std::process::{Command, Stdio};
// use std::io::Write;
use std::process::Stdio;

mod math;


use invalid_choice::print_invalid_choice_and_restart;
// use invalid_choice::print_invalid_choice_and_restart_sm;

// extern crate invalid_choice::print_invalid_choice_and_restart_sm;

use invalid_choice::print_invalid_choice_and_restart_sm;

use invalid_choice::print_invalid_choice_and_restart_java_menu;

use invalid_choice::print_invalid_choice_and_restart_python_menu;

use invalid_choice::print_invalid_choice_and_restart_csharp_menu;

use invalid_choice::print_invalid_choice_and_restart_prime_program_menu;

mod invalid_choice;

mod web_edition;

fn script_mode() {
    let mut stdout = io::stdout();

    let mut input = String::new();

    println!("Select an option as a prime program:");

    println!("1. Use this program");
    println!("2. C program");
    println!("3. C++ program");
    println!("4. Java program");
    println!("5. Python program");
    println!("6. C# program");
    println!("7. Go program");
    println!("8. Assembly program");
    println!("9. Exit");

    print!("Select: ");

    stdout.flush().expect("Failed to flush stdout");

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");

    println!("You entered: {}", input);

    match input {
        1 => prime_program(),
        2 => c_program(),
        3 => cpp_program(),
        4 => java_program_menu(),
        5 => python_program_menu(),
        6 => csharp_program_menu(),
        7 => go_program(),
        8 => assembly_program(),
        9 => exit_program(),
        _ => print_invalid_choice_and_restart_sm(),
    }
}

fn gui_mode() {
    println!("GUI mode is not implemented yet.");
}

pub fn prime_program() {
    let mut stdout = io::stdout();

    let mut input = String::new();


    println!("Executing prime program...");
    // Implementation for prime program goes here
    
    println!("Select an option to execute:");

    println!("1. Execute math operations");

    println!("2. Web Edition of the program");
    
    println!("3. Go to the previous menu");
    
    println!("4. Exit");

    print!("Select: ");

    stdout.flush().expect("Failed to flush stdout");

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");

    println!("You entered: {}", input);

    match input {
        1 => math::math_op(),
        2 => web_edition::finalcode(),
        3 => script_mode(),
        4 => exit_program(),
        _ => print_invalid_choice_and_restart_prime_program_menu(),
    }
    
}

fn c_program() {
    println!("Executing C program...");

    let output = Command::new("F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\c\\\\mainc.exe")
        .output()
        .expect("Failed to execute process");

    println!("status: {}", output.status);
    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
}

fn cpp_program() {
    println!("Executing C++ program...");
    // Implementation for C++ program goes here

    let output = Command::new("F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\cpp\\\\maincpp.exe")
        .output()
        .expect("Failed to execute process");

    println!("status: {}", output.status);
    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
}

// fn java_program_menu() {
//     let mut input = String::new();
//     println!("Executing Java program...");
//     // Implementation for Java program goes here

//     println!("Select the version of java program:");

//     println!("1. JAR Version(JRE OR JDK REQUIRED)");
//     println!("2. Console Version");
//     println!("3. Go to the previous menu");
//     println!("4. Exit");

//     // print!("Select: ");

//     // stdout().flush().expect("Failed to flush stdout");

//     // io::stdin().read_line(&mut input).expect("Failed to read line");

//     // let input: u32 = input.trim().parse().expect("Please enter a number");

//     // println!("You entered: {}", input);

//     let selection = loop {
//         print!("Select: ");
//         io::stdout().flush().unwrap(); // Ensure the prompt is printed immediately

//         let mut input = String::new();
//         io::stdin().read_line(&mut input).expect("Failed to read input");

//         // Trim whitespace from input and check if it's not empty
//         let input = input.trim();

//         if input.is_empty() {
//             println!("Please enter a number. Empty input is not valid.");
//             continue; // Prompt again if input is empty
//         }

//         // Attempt to parse the input as a number
//         match input.parse::<u32>() {
//             Ok(num) => break num, // Break the loop if the input is valid
//             Err(_) => {
//                 println!("Invalid input. Please enter a valid number.");
//             }
//         }
//     };

//     println!("You entered: {}", selection);

//     match input {
//         1 => java_program_jar(),
//         2 => java_program_console(),
//         3 => script_mode(),
//         4 => exit_program(),
//         _ => print_invalid_choice_and_restart_java_menu(),
//     }
// }

fn java_program_menu() {
    println!("Executing Java program...");
    // Implementation for Java program goes here

    println!("Select the version of java program:");
    println!("1. JAR Version(JRE OR JDK REQUIRED)");
    println!("2. Console Version");
    println!("3. Go to the previous menu");
    println!("4. Exit");

    let selection = loop {
        print!("Select: ");
        io::stdout().flush().unwrap(); // Ensure the prompt is printed immediately

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");

        // Trim whitespace from input and check if it's not empty
        let input = input.trim();

        if input.is_empty() {
            println!("Please enter a number. Empty input is not valid.");
            continue; // Prompt again if input is empty
        }

        // Attempt to parse the input as a number
        match input.parse::<u32>() {
            Ok(num) => break num, // Break the loop if the input is valid
            Err(_) => {
                println!("Invalid input. Please enter a valid number.");
            }
        }
    };

    println!("You entered: {}", selection);

    match selection {
        1 => java_program_jar(),
        2 => java_program_console(),
        3 => script_mode(),
        4 => exit_program(),
        _ =>print_invalid_choice_and_restart_java_menu(), 
        //  {
        //     println!("Invalid choice. Please try again.");
        //     java_program_menu(); // Restart the menu if input is invalid
        // }
    }
}

fn java_program_console() {
    // println!("Executing Java program on console...");

    // let output = Command::new("F:\\\\panag\\\\Documents\\\\AAP\\\\prime_cores\\\\executable\\\\java\\\\MainJ.exe")
    //     .output()
    //     .expect("Failed to execute process");

    //     println!("status: {}", output.status);
    //     println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    //     println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
    
    println!("Executing Java program on console...");

    let mut child = Command::new("F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\java\\\\MainJ.exe")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .expect("Failed to execute process");

    // Write input to the Java program if it's expected
    if let Some(ref mut stdin) = child.stdin {
        writeln!(stdin, "Your input here").expect("Failed to write to stdin");
    }

    let output = child.wait_with_output().expect("Failed to wait on child");

    println!("status: {}", output.status);
    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    println!("stderr: {}", String::from_utf8_lossy(&output.stderr));

}

fn java_program_jar() {
    println!("Executing JAR program ...");
    // Path to the Java executable and the .jar file
    let java_path = "java"; // or specify the full path if needed
    let jar_path = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\java\\\\MainJ.jar";

    // Build and run the command to execute the jar file
    let output = Command::new(java_path)
        .arg("-jar")
        .arg(jar_path)
        .output()
        .expect("Failed to execute jar");

    // Handle the output
    if output.status.success() {
        println!("Jar executed successfully.");
        let stdout = String::from_utf8_lossy(&output.stdout);
        println!("Output: {}", stdout);
    } else {
        eprintln!("Failed to execute jar.");
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("Error: {}", stderr);
    }
}

fn python_program_menu() {
    println!("Executing Python program...");
    // Implementation for Python program goes here

    println!("Select the version of python program:");
    println!("1. py version(PYTHON REQUIRED)");
    println!("2. Console Version");
    println!("3. Go to the previous menu");
    println!("4. Exit");

    let selection = loop {
        print!("Select: ");
        io::stdout().flush().unwrap(); // Ensure the prompt is printed immediately

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");

        // Trim whitespace from input and check if it's not empty
        let input = input.trim();

        if input.is_empty() {
            println!("Please enter a number. Empty input is not valid.");
            continue; // Prompt again if input is empty
        }

        // Attempt to parse the input as a number
        match input.parse::<u32>() {
            Ok(num) => break num, // Break the loop if the input is valid
            Err(_) => {
                println!("Invalid input. Please enter a valid number.");
            }
        }
    };

    println!("You entered: {}", selection);

    match selection {
        1 => python_program_py(),
        2 => python_program_console(),
        3 => script_mode(),
        4 => exit_program(),
        _ =>print_invalid_choice_and_restart_python_menu(), 
        //  {
        //     println!("Invalid choice. Please try again.");
        //     java_program_menu(); // Restart the menu if input is invalid
        // }
    }
}

fn python_program_py(){
    println!("Executing Python program(py version)...");
    // The Python file you want to execute
    let python_file = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\python\\\\mainpy.py";

    // Execute the Python file using Python interpreter
    let output = Command::new("python")
        .arg(python_file)
        .output()
        .expect("Failed to execute Python script");

    // Check if the execution was successful
    if output.status.success() {
        // Print the output from the Python script (stdout)
        let stdout = String::from_utf8_lossy(&output.stdout);
        println!("Output: {}", stdout);
        println!("status: {}", output.status);
    } else {
        // Print the error (stderr) if execution failed
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("Error: {}", stderr);
    }
}

fn python_program_console(){
    println!("Executing Python program(console version)...");
    let mut child = Command::new("F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\python\\\\mainpy.exe")
    .stdin(Stdio::piped())
    .stdout(Stdio::piped())
    .stderr(Stdio::piped())
    .spawn()
    .expect("Failed to execute process");

// Write input to the Python program if it's expected
if let Some(ref mut stdin) = child.stdin {
    writeln!(stdin, "Your input here").expect("Failed to write to stdin");
}

let output = child.wait_with_output().expect("Failed to wait on child");

println!("status: {}", output.status);
println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
}

fn csharp_program_menu() {
    println!("Executing C# program...");
    // Implementation for C# program goes here

     // Ask the user to choose between running the C# program in the current console or a new window
     println!("Select how you want to run the C# program:");
     println!("1. Run in current console");//(inherit stdin, stdout, stderr)
     println!("2. Run in a new window");
     println!("3. Test in the current console");
     println!("4. Previous menu");
     println!("5. Exit");

     let selection = loop {
        print!("Select: ");
        io::stdout().flush().unwrap(); // Ensure the prompt is printed immediately

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");

        // Trim whitespace from input and check if it's not empty
        let input = input.trim();

        if input.is_empty() {
            println!("Please enter a number. Empty input is not valid.");
            continue; // Prompt again if input is empty
        }

        // Attempt to parse the input as a number
        match input.parse::<u32>() {
            Ok(num) => break num, // Break the loop if the input is valid
            Err(_) => {
                println!("Invalid input. Please enter a valid number.");
            }
        }
    };

    println!("You entered: {}", selection);

    match selection {
        1 => csharp_program_console(),
        2 => csharp_program_new_window(),
        3 => csharp_program_test(),
        4 => script_mode(),
        5 => exit_program(),
        _ => print_invalid_choice_and_restart_csharp_menu(),
    }
}

fn csharp_program_console(){
    println!("Executing C# program(console version)...");

    // Path to the C# executable (.exe)
    let exe_path = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\cs\\\\maincs.exe";

    // Option 1: Run the C# executable in the current console
    println!("Running in current console...");
    let output = Command::new(exe_path)
        .stdin(Stdio::inherit())  // Attach standard input
        .stdout(Stdio::inherit()) // Attach standard output
        .stderr(Stdio::inherit()) // Attach standard error
        .status()                 // Run the command and wait for completion
        .expect("Failed to execute C# program");

    println!("Status: {:?}", output);
}

fn csharp_program_new_window(){
    println!("Executing C# program(new window)...");

    // Path to the C# executable (.exe)
    let exe_path = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\cs\\\\maincs.exe";

     // Option 2: Run the C# executable in a new window
     println!("Running in a new window...");
     let status = Command::new("cmd")
         .args(&["/C", "start", exe_path])  // Use 'start' to open in a new window
         .status()
         .expect("Failed to start C# program in a new window");

     println!("Status: {:?}", status);
}

fn csharp_program_test(){
    println!("Executing C# program(test version)...");

    // Path to the C# executable (.exe)
    let exe_path = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\cs\\\\maincs.exe";

    // Run the executable
    let output = Command::new(exe_path)
        .output()
        .expect("Failed to execute C# program");

    // Print the output from the executable
    println!("Status: {}", output.status);
    println!("Stdout: {}", String::from_utf8_lossy(&output.stdout));
    println!("Stderr: {}", String::from_utf8_lossy(&output.stderr));
}

fn go_program() {
    println!("Executing Go program...");
    // Implementation for Go program goes here

    let exe_path ="F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\go\\\\maingo.exe";
    

    // Replace with the actual path to your Go executable
    let output = Command::new(exe_path)
        .output()
        .expect("Failed to execute process");

    let stderr = String::from_utf8_lossy(&output.stderr);
    let stdout = String::from_utf8_lossy(&output.stdout);
    // Check if the execution was successful
    if output.status.success() {
        // Print the output from the Go program
        // let stdout = String::from_utf8_lossy(&output.stdout);
        println!("Go program output: {}", stdout);
        println!("Status: {}", output.status);
        eprintln!("Go program error: {}", stderr);
    } else {
        // Handle errors
        // let stderr = String::from_utf8_lossy(&output.stderr);
        println!("Go program output: {}", stdout);
        eprintln!("Go program error: {}", stderr);
        println!("Status: {}", output.status);
    }
}

fn assembly_program() {

// println!("Executing Assembly program...");

// // Define the exact path of the assembly executable
// let exe_path = "F:\\\\panag\\\\Documents\\\\AAP\\\\executable\\\\assembly\\\\mainasm.exe";

// // Try executing the assembly program and catch any errors
// let output = Command::new(exe_path)
//     .output()
//     .expect("Failed to execute Assembly program");

// // Print status and output for diagnostics
// println!("Exit Status: {:?}", output.status);

// // Check if the execution was successful
// if output.status.success() {
//     println!("Assembly program executed successfully.");
// } else {
//     // Check for access violation error code
//     if let Some(code) = output.status.code() {
//         if code as u32 == 3221226505 { // 0xc0000005 in decimal
//             println!("Access violation occurred!");
//         } else {
//             println!("Error: Assembly program exited with status code: {}", code);
//         }
//     } else {
//         println!("The assembly program terminated unexpectedly.");
//     }
// }

// // Output stdout and stderr for debugging
// println!("stdout:\n{}", String::from_utf8_lossy(&output.stdout));
// println!("stderr:\n{}", String::from_utf8_lossy(&output.stderr));

println!("Executing Assembly program...");

// Define the exact path of the assembly executable
let exe_path = r"F:\panag\Documents\AAP\executable\assembly\mainasm.exe"; // or use forward slashes

// Print the path for debugging
println!("Attempting to execute: {}", exe_path);

// Try executing the assembly program and catch any errors
let output = Command::new(exe_path)
    .output()
    .expect("Failed to execute Assembly program");

// Print status and output for diagnostics
println!("Exit Status: {:?}", output.status);

// Check if the execution was successful
if output.status.success() {
    println!("Assembly program executed successfully.");
} else {
    // Check for access violation error code
    if let Some(code) = output.status.code() {
        if code as u32 == 3221226505 { // 0xc0000005 in decimal
            println!("Access violation occurred!");
        } else {
            println!("Error: Assembly program exited with status code: {}", code);
        }
    } else {
        println!("The assembly program terminated unexpectedly.");
    }
}

// Output stdout and stderr for debugging
println!("stdout:\n{}", String::from_utf8_lossy(&output.stdout).trim());
println!("stderr:\n{}", String::from_utf8_lossy(&output.stderr).trim());
}

fn exit_program() {
    println!("Exiting program...");
    std::process::exit(0);
}



fn mode_selector() {

    let mut stdout = io::stdout();

    let mut input = String::new();

    println!("Welcome to the AAP(ALL-AROUND-PROGRAM OR ALL-AROUND-PROJECT)");
    
    println!("This program was designed by Panos Biazis using RUST Language");

    println!("My Email: panosbiazis2003@gmail.com");

    println!("My LinkedIn: https://www.linkedin.com/in/panos-biazis-9a159b2a2/");
    
    println!("Select a mode of the program:");
    
    println!("1. Script mode");
    
    println!("2. GUI mode");

    println!("3. Exit");

    println!("!!!NOTE:IF YOU SELECT THE GUI MODE,THE PROGRAM WILL BE SLOWER AND INCREASE MEMORY USAGE!!!");

    print!("Select: ");

    // io::stdin().read_line(&mut input).expect("Failed to read line");

    // let input: u32 = input.trim().parse().expect("Please enter a number");

    // println!("You entered: {}", input);

    stdout.flush().expect("Failed to flush stdout");

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let input: u32 = input.trim().parse().expect("Please enter a number");

    println!("You entered: {}", input);

    match input {
        1 => script_mode(),
        2 => gui_mode(),
        3 => exit_program(),
        _ => print_invalid_choice_and_restart(),
    }
}

fn main() {
    mode_selector();
}
