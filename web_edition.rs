// use actix_files as fs; // Add this line to use actix-files for serving static files
// use actix_web::{get, App, HttpResponse, HttpServer, Responder, middleware::Logger};
// use std::process::Command;
// // use crate::file_server::file_sys;
// // use crate::file_server;
// // mod file_server;
// use crate::file_server;
// use crate::invalid_choice::print_invalid_choice_and_restart_web_menu;
// // use std::io::stdout;
// use std::io::{self,Write};
// // use tokio::io;
// // use crate::io;

// #[get("/run_php")]
// pub async fn run_php() -> impl Responder {
//     let php_file_path = "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/php/start.php";

//     let output = Command::new("php")
//         .arg(php_file_path)
//         .output();

//     match output {
//         Ok(output) => {
//             if output.status.success() {
//                 let response = String::from_utf8_lossy(&output.stdout).into_owned();
//                 // Print the status and response to the console
//                 println!("Status: 200 OK");
//                 println!("Response: {}", response);
//                 HttpResponse::Ok()
//                     .content_type("text/html")
//                     .body(response)
//             } else {
//                 let error_message = String::from_utf8_lossy(&output.stderr).into_owned();
//                 // Print the error status to the console
//                 println!("Status: 500 Internal Server Error");
//                 println!("Error: {}", error_message);
//                 HttpResponse::InternalServerError()
//                     .body(format!("PHP Error: {}", error_message))
//             }
//         }
//         Err(e) => {
//             // Print the error status to the console
//             println!("Status: 500 Internal Server Error");
//             println!("Failed to run PHP: {}", e);
//             HttpResponse::InternalServerError().body(format!("Failed to run PHP: {}", e))
//         }
//     }
// }

// // #[actix_web::main]
// // pub async fn main() -> std::io::Result<()> {
// //     // Open the default browser and navigate to the URL
// //     let _ = Command::new("cmd")
// //         .arg("/C")
// //         .arg("start")
// //         .arg("http://127.0.0.1:8081/run_php") // Open URL in the default browser
// //         .spawn();

// //     std::env::set_var("RUST_LOG", "actix_web=info");
// //     HttpServer::new(|| {
// //         App::new()
// //             .wrap(Logger::default())
// //             .service(run_php) // Define the route and handler
// //             .service(fs::Files::new("/css", "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/css/start.css").show_files_listing()) // Serve CSS files
// //             .service(fs::Files::new("/js", "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/js/start.js").show_files_listing()) // Serve JavaScript files
// //     })
// //     .bind("127.0.0.1:8081")?
// //     .run()
// //     .await
// // }

// // #[actix_web::run_php_based_web]
// // pub async fn run_php_based_web() -> std::io::Result<()> {
// pub async fn run_php_based_web() -> Result<(), std::io::Error> {
//     // Open the default browser and navigate to the URL
//     let _ = Command::new("cmd")
//     .arg("/C")
//     .arg("start")
//     .arg("http://127.0.0.1:8081/run_php") // Open URL in the default browser
//     .spawn();

//     std::env::set_var("RUST_LOG", "actix_web=info");
//     HttpServer::new(|| {
//         App::new()
//             .wrap(Logger::default())
//             .service(run_php) // Define the route and handler
//             .service(fs::Files::new("/css", "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/css/start.css").show_files_listing()) // Serve CSS files
//             .service(fs::Files::new("/js", "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/js/start.js").show_files_listing()) // Serve JavaScript files
//     })
//     .bind("127.0.0.1:8081")?
//     .run()
//     .await
// }

// pub async fn route_system(){
//     println!("Executing route_system...");

//     file_server::file_sys().await;

// }

// pub async fn web_menu(){

//     let mut stdout = io::stdout();

//     let mut input = String::new();

//     println!("Executing web_menu...");

//     println!("1. Run PHP");
    
//     println!("2. file system web");
    
//     println!("3. Previous menu");
    
//     println!("4. Exit");
    
//     print!("Select: ");

//     stdout.flush().expect("Failed to flush stdout");
    
//     io::stdin().read_line(&mut input).expect("Failed to read line");

//     let input: u32 = input.trim().parse().expect("Please enter a number");

//     println!("You entered: {}", input);

//     match input {
//         1 => run_php().await,
//         2 => route_system().await,
//         3 => web_menu().await,
//         4 => std::process::exit(0),
//         _ => print_invalid_choice_and_restart_web_menu(),
        
//     }

// }


// #[actix_web::main]
// pub async fn main() -> std::io::Result<()> {

//     web_menu().await;

// }


use actix_files as fs;
use actix_web::{get, App, HttpResponse, HttpServer, Responder, middleware::Logger};
use std::process::Command;
use std::io::{self, Write};
use crate::file_server;
use crate::invalid_choice::print_invalid_choice_and_restart_web_menu;
// use crate::main as start_main;
use crate::prime_program;
use crate::exit_program;


#[get("/run_php")]
pub async fn run_php() -> impl Responder {
    let php_file_path = "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/php/start.php";

    let output = Command::new("php")
        .arg(php_file_path)
        .output();

    match output {
        Ok(output) => {
            if output.status.success() {
                let response = String::from_utf8_lossy(&output.stdout).into_owned();
                println!("Status: 200 OK");
                println!("Response: {}", response);
                HttpResponse::Ok()
                    .content_type("text/html")
                    .body(response)
            } else {
                let error_message = String::from_utf8_lossy(&output.stderr).into_owned();
                println!("Status: 500 Internal Server Error");
                println!("Error: {}", error_message);
                HttpResponse::InternalServerError()
                    .body(format!("PHP Error: {}", error_message))
            }
        }
        Err(e) => {
            println!("Status: 500 Internal Server Error");
            println!("Failed to run PHP: {}", e);
            HttpResponse::InternalServerError().body(format!("Failed to run PHP: {}", e))
        }
    }
}

pub async fn run_php_based_web() -> std::io::Result<()> {
    let _ = Command::new("xdg-open")
        .arg("http://127.0.0.1:8081/run_php")
        .spawn();

    std::env::set_var("RUST_LOG", "actix_web=info");
    HttpServer::new(|| {
        App::new()
            .wrap(Logger::default())
            .service(run_php)
            .service(fs::Files::new(
                "/css",
                "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/css",
            ))
            .service(fs::Files::new(
                "/js",
                "/media/panos/SAMSUNGT7/panag/Documents/AAP(linux)/others/web/websites/website1/js",
            ))
    })
    .bind("127.0.0.1:8081")?
    .run()
    .await
}

pub async fn route_system() {
    println!("Executing route_system...");
    file_server::file_sys().await;
}

pub async fn web_menu() {
    loop {
        let mut stdout = io::stdout();
        let mut input = String::new();

        println!("Executing web_menu...");
        println!("1. Run PHP");
        println!("2. File system web");
        println!("3. Previous menu");
        println!("4. Exit");
        print!("Select: ");
        stdout.flush().expect("Failed to flush stdout");

        io::stdin().read_line(&mut input).expect("Failed to read line");

        match input.trim() {
            "1" => run_php_based_web().await.unwrap(),
            "2" => route_system().await,
            "3" => prime_program().await,
            "4" => exit_program().await,//std::process::exit(0),
            _ => print_invalid_choice_and_restart_web_menu(),
        }
    }
}

#[actix_web::main]
pub async fn main() -> std::io::Result<()> {
    web_menu().await;
    Ok(())
}
