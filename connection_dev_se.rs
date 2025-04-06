// use tokio::net::TcpListener;
// use tokio::sync::broadcast;
// use std::sync::{Arc, Mutex};
// use std::collections::HashMap;
// use tokio::time::{sleep, Duration};

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let listener = TcpListener::bind("127.0.0.1:8080").await?;
//     let (tx, _rx) = broadcast::channel(100);  // To broadcast messages to clients
//     let client_data = Arc::new(Mutex::new(HashMap::new()));

//     println!("Server listening on 127.0.0.1:8080");

//     loop {
//         let (socket, addr) = listener.accept().await?;
//         println!("Client connected: {}", addr);

//         let tx = tx.clone();
//         let client_data = client_data.clone();

//         // Spawn a task for each client
//         tokio::spawn(async move {
//             // Client handling code here
//             handle_client(socket, addr, tx, client_data).await;
//         });
//     }
// }

// pub async fn handle_client(
//     socket: tokio::net::TcpStream,
//     addr: std::net::SocketAddr,
//     tx: broadcast::Sender<String>,
//     client_data: Arc<Mutex<HashMap<String, std::net::SocketAddr>>>,
// ) {
//     client_data.lock().unwrap().insert(addr.to_string(), addr);

//     loop {
//         // Send and receive data here, update status if needed
//         sleep(Duration::from_secs(5)).await; // Example interval
//     }
// }


// use tokio::net::TcpListener;
// use tokio::sync::broadcast;
// use std::sync::{Arc, Mutex};
// use std::collections::HashMap;
// use tokio::time::{sleep, Duration};

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let listener = TcpListener::bind("127.0.0.1:8080").await?;
//     let (tx, _rx) = broadcast::channel(100); // To broadcast messages to clients
//     let client_data = Arc::new(Mutex::new(HashMap::new()));

//     println!("Server listening on 127.0.0.1:8080");

//     loop {
//         let (socket, addr) = listener.accept().await?;
//         println!("Client connected: {}", addr);

//         let tx = tx.clone();
//         let client_data = client_data.clone();

//         // Spawn a task for each client
//         tokio::spawn(async move {
//             handle_client(socket, addr, tx, client_data).await;
//         });
//     }
// }

// pub async fn handle_client(
//     socket: tokio::net::TcpStream,
//     addr: std::net::SocketAddr,
//     tx: broadcast::Sender<String>,
//     client_data: Arc<Mutex<HashMap<String, std::net::SocketAddr>>>,
// ) {
//     client_data.lock().unwrap().insert(addr.to_string(), addr);

//     loop {
//         // Send and receive data here, update status if needed
//         sleep(Duration::from_secs(5)).await; // Example interval
//         println!("Handling client at {}", addr);
//     }
// }

// use tokio::net::TcpListener;
// use tokio::sync::broadcast;
// use std::sync::{Arc, Mutex};
// use std::collections::HashMap;
// use tokio::time::{sleep, Duration};

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let listener = TcpListener::bind("127.0.0.1:8080").await?;
//     let (tx, _rx) = broadcast::channel(100);  // To broadcast messages to clients
//     let client_data = Arc::new(Mutex::new(HashMap::new()));

//     println!("Server listening on 127.0.0.1:8080");

//     loop {
//         let (socket, addr) = listener.accept().await?;
//         println!("Client connected: {}", addr);

//         let tx = tx.clone();
//         let client_data = client_data.clone();

//         // Spawn a task for each client
//         tokio::spawn(async move {
//             handle_client(socket, addr, tx, client_data).await;
//         });
//     }
// }

// pub async fn handle_client(
//     _socket: tokio::net::TcpStream, // Prefix `socket` with an underscore
//     addr: std::net::SocketAddr,
//     _tx: broadcast::Sender<String>, // Prefix `tx` with an underscore
//     client_data: Arc<Mutex<HashMap<String, std::net::SocketAddr>>>,
// ) {
//     client_data.lock().unwrap().insert(addr.to_string(), addr);

//     loop {
//         // Send and receive data here, update status if needed
//         sleep(Duration::from_secs(5)).await; // Example interval
//     }
// }

// use tokio::net::TcpListener;
// use tokio::sync::broadcast;
// use std::sync::{Arc, Mutex};
// use std::collections::HashMap;
// use tokio::time::{sleep, Duration};
// use tokio::signal;

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let listener = TcpListener::bind("127.0.0.1:8080").await?;
//     let (tx, _rx) = broadcast::channel(100); // To broadcast messages to clients
//     let client_data = Arc::new(Mutex::new(HashMap::new()));

//     println!("Server listening on 127.0.0.1:8080");

//     let shutdown_signal = signal::ctrl_c(); // Handle Ctrl+C signal

//     loop {
//         tokio::select! {
//             // Accept new client connections
//             result = listener.accept() => {
//                 match result {
//                     Ok((socket, addr)) => {
//                         println!("Client connected: {}", addr);
//                         let tx = tx.clone();
//                         let client_data = client_data.clone();
//                         // Spawn a task for each client
//                         tokio::spawn(async move {
//                             handle_client(socket, addr, tx, client_data).await;
//                         });
//                     }
//                     Err(e) => eprintln!("Error accepting connection: {:?}", e),
//                 }
//             },

//             // Handle shutdown signal
//             _ = shutdown_signal => {
//                 println!("Received Ctrl+C. Shutting down server...");
//                 break; // Exit the loop and close the server gracefully
//             }
//         }
//     }

//     println!("Server has been shut down.");
//     Ok(())
// }

// pub async fn handle_client(
//     _socket: tokio::net::TcpStream, // Prefix `socket` with an underscore
//     addr: std::net::SocketAddr,
//     _tx: broadcast::Sender<String>, // Prefix `tx` with an underscore
//     client_data: Arc<Mutex<HashMap<String, std::net::SocketAddr>>>,
// ) {
//     // Store client data
//     client_data.lock().unwrap().insert(addr.to_string(), addr);

//     loop {
//         // Send and receive data here, update status if needed
//         sleep(Duration::from_secs(5)).await; // Example interval
//     }
// }


use tokio::net::TcpListener;
use tokio::sync::broadcast;
use std::sync::{Arc, Mutex};
use std::collections::HashMap;
use tokio::time::{sleep, Duration};
use tokio::signal;

#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("0.0.0.0:8080").await?; // Listens on all network interfaces //127.0.0.1:8080
    let (tx, _rx) = broadcast::channel(100);  // To broadcast messages to clients
    let client_data = Arc::new(Mutex::new(HashMap::new()));

    println!("Server listening on 127.0.0.1:8080");

    loop {
        tokio::select! {
            Ok((socket, addr)) = listener.accept() => {
                println!("Client connected: {}", addr);

                let tx = tx.clone();
                let client_data = client_data.clone();

                // Spawn a task for each client
                tokio::spawn(async move {
                    handle_client(socket, addr, tx, client_data).await;
                });
            }
            _ = signal::ctrl_c() => {
                println!("Received Ctrl+C. Shutting down the server...");
                break; // Exit the loop to shutdown the server
            }
        }
    }

    println!("Server shutting down...");
    Ok(())
}

pub async fn handle_client(
    _socket: tokio::net::TcpStream, // Prefix `socket` with an underscore
    addr: std::net::SocketAddr,
    _tx: broadcast::Sender<String>, // Prefix `tx` with an underscore
    client_data: Arc<Mutex<HashMap<String, std::net::SocketAddr>>>,
) {
    client_data.lock().unwrap().insert(addr.to_string(), addr);

    loop {
        // Send and receive data here, update status if needed
        sleep(Duration::from_secs(5)).await; // Example interval
    }
}
