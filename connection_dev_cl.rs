// use tokio::net::TcpStream;
// use std::time::Duration;
// use tokio::time::sleep;

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let socket = TcpStream::connect("127.0.0.1:8080").await?;
//     println!("Connected to server");

//     loop {
//         // Example of sending data every 5 seconds
//         send_packet(&socket, 64, 64).await;
//         sleep(Duration::from_secs(5)).await;
//     }
// }

// pub async fn send_packet(
//     socket: &TcpStream,
//     size: usize,
//     ttl: u8,
// ) -> Result<(), Box<dyn std::error::Error>> {
//     // Here you would define a packet with a specific size and TTL
//     let data = vec![0u8; size];
//     socket.set_ttl(ttl)?;
//     socket.writable().await?;
//     socket.try_write(&data)?;
//     println!("Sent packet with size {} and TTL {}", size, ttl);
//     Ok(())
// }

// use tokio::net::TcpStream;
// use std::time::Duration;
// use tokio::time::sleep;

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let socket = TcpStream::connect("127.0.0.1:8080").await?;
//     println!("Connected to server");

//     loop {
//         // Example of sending data every 5 seconds
//         send_packet(&socket, 64, 64).await?;
//         sleep(Duration::from_secs(5)).await;
//     }
// }

// pub async fn send_packet(
//     socket: &TcpStream,
//     size: usize,
//     ttl: u8,
// ) -> Result<(), Box<dyn std::error::Error>> {
//     // Create a packet with a specific size and TTL
//     let data = vec![0u8; size];
//     socket.set_ttl(ttl)?;
//     socket.writable().await?;
//     socket.try_write(&data)?;
//     println!("Sent packet with size {} and TTL {}", size, ttl);
//     Ok(())
// }


// use tokio::net::TcpStream;
// use std::time::Duration;
// use tokio::time::sleep;

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let socket = TcpStream::connect("127.0.0.1:8080").await?;
//     println!("Connected to server");

//     loop {
//         // Example of sending data every 5 seconds
//         send_packet(&socket, 64, 64).await?;
//         sleep(Duration::from_secs(5)).await;
//     }
// }

// pub async fn send_packet(
//     socket: &TcpStream,
//     size: usize,
//     ttl: u8,
// ) -> Result<(), Box<dyn std::error::Error>> {
//     let data = vec![0u8; size];
//     socket.set_ttl(ttl.into())?; // Convert ttl to u32 using `into()`
//     socket.writable().await?;
//     socket.try_write(&data)?;
//     println!("Sent packet with size {} and TTL {}", size, ttl);
//     Ok(())
// }


// use tokio::net::TcpStream;
// use tokio::time::{sleep, Duration};
// use tokio::signal;
// // use tokio::io::{AsyncWriteExt, AsyncReadExt};

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let socket = TcpStream::connect("127.0.0.1:8080").await?;
//     println!("Connected to server");

//     // Create a mutable flag to track the connection status
//     let mut connected = true;

//     tokio::select! {
//         // Handle the packet sending in a loop
//         _ = async {
//             while connected {
//                 send_packet(&socket, 64, 64).await?;
//                 sleep(Duration::from_secs(5)).await;
//             }
//             Ok::<(), Box<dyn std::error::Error>>(())
//         } => {},
        
//         // Handle Ctrl+C or Esc key to exit gracefully
//         _ = signal::ctrl_c() => {
//             println!("Received Ctrl+C. Exiting...");
//             connected = false;
//         },
        
//         _ = signal::unix::signal(signal::unix::SignalKind::interrupt()).unwrap() => {
//             println!("Received Esc key. Exiting...");
//             connected = false;
//         },
//     }

//     println!("Closing connection...");
//     Ok(())
// }

// pub async fn send_packet(
//     socket: &TcpStream,
//     size: usize,
//     ttl: u8,
// ) -> Result<(), Box<dyn std::error::Error>> {
//     let data = vec![0u8; size];
//     socket.set_ttl(ttl.into())?; // Convert ttl to u32 using `into()`
//     socket.writable().await?;
//     socket.try_write(&data)?;
//     println!("Sent packet with size {} and TTL {}", size, ttl);
//     Ok(())
// }


// use tokio::net::TcpStream;
// use std::time::Duration;
// use tokio::time::sleep;
// use tokio::signal;

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let socket = TcpStream::connect("127.0.0.1:8080").await?;
//     println!("Connected to server");

//     let shutdown_signal = signal::ctrl_c(); // Handle Ctrl+C signal

//     loop {
//         tokio::select! {
//             _ = shutdown_signal => {
//                 println!("Shutdown signal received. Exiting...");
//                 break; // Exit the loop on shutdown signal
//             }
//             _ = send_packet(&socket, 64, 64) => {
//                 // Sending packet every 5 seconds
//                 sleep(Duration::from_secs(5)).await;
//             }
//         }
//     }

//     Ok(())
// }

// pub async fn send_packet(
//     socket: &TcpStream,
//     size: usize,
//     ttl: u8,
// ) -> Result<(), Box<dyn std::error::Error>> {
//     let data = vec![0u8; size];
//     socket.set_ttl(ttl.into())?; // Convert ttl to u32 using `into()`
//     socket.writable().await?;
//     socket.try_write(&data)?;
//     println!("Sent packet with size {} and TTL {}", size, ttl);
//     Ok(())
// }



use tokio::net::TcpStream;
use std::time::Duration;
use tokio::time::sleep;
use tokio::signal;

#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let socket = TcpStream::connect("192.168.0.125:8080").await?; //127.0.0.1:8080
    println!("Connected to server");

    loop {
        let shutdown_signal = signal::ctrl_c(); // Handle Ctrl+C signal for each iteration

        tokio::select! {
            _ = shutdown_signal => {
                println!("Shutdown signal received. Exiting...");
                break; // Exit the loop on shutdown signal
            }
            _ = send_packet(&socket, 64, 64) => {
                // Sending packet every 5 seconds
                sleep(Duration::from_secs(5)).await;
            }
        }
    }

    Ok(())
}

pub async fn send_packet(
    socket: &TcpStream,
    size: usize,
    ttl: u8,
) -> Result<(), Box<dyn std::error::Error>> {
    let data = vec![0u8; size];
    socket.set_ttl(ttl.into())?; // Convert ttl to u32 using `into()`
    socket.writable().await?;
    socket.try_write(&data)?;
    println!("Sent packet with size {} and TTL {}", size, ttl);
    Ok(())
}
