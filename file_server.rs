use warp::Filter;
use std::path::Path;
use std::fs;
use warp::http::Response;
// use warp::http::StatusCode;
// use crate::web_edition;
// use tokio::fs;

// #[tokio::file_sys]
pub async fn file_sys() {
    // Base directory to serve files from
    let base_dir = "/media/panos/panag/Documents/AAP(linux)/others/web/websites";// ./public
    // Define the routes
    let file_server = warp::fs::dir(base_dir);
    let folder_listing = warp::path::end()
        .map(move || list_files(base_dir));
    // Combine routes
    let routes = warp::get().and(folder_listing.or(file_server));
    println!("Serving files at http://127.0.0.1:3030/");
    warp::serve(routes).run(([127, 0, 0, 1], 3030)).await;
}
// Function to list files and folders in a directory
pub fn list_files(base_dir: &str) -> impl warp::Reply {
    let path = Path::new(base_dir);
    if !path.exists() || !path.is_dir() {
        return Response::builder()
            .status(404)
            .body("Directory not found".into())
            .unwrap();
    }
    let mut html = String::new();
    html.push_str("<html><body><h1>File Browser</h1><ul>");
    for entry in fs::read_dir(path).unwrap() {
        if let Ok(entry) = entry {
            let file_name = entry.file_name().into_string().unwrap();
            let file_type = entry.file_type().unwrap();
            if file_type.is_dir() {
                html.push_str(&format!(
                    "<li><a href=\"/{}/\">{}/</a></li>",
                    file_name, file_name
                ));
            } else {
                html.push_str(&format!(
                    "<li><a href=\"/{}\">{}</a></li>",
                    file_name, file_name
                ));
            }
        }
    }
    html.push_str("</ul></body></html>");
    Response::builder()
        .header("Content-Type", "text/html")
        .body(html)
        .unwrap()
}


// use std::fs;
// use std::path::PathBuf;
// use tiny_http::{Server, Response, Request};

// pub async fn main() {
//     let base_dir = "/media/panos/panag/Documents/AAP(linux)/others/web/websites";  //"../../../../AAP(linux)/others/web/websites";
//     let server = Server::http("127.0.0.1:3030").unwrap();

//     println!("Server running at http://127.0.0.1:3030");

//     for request in server.incoming_requests() {
//         let url_path = request.url().trim_start_matches('/'); // Get the clicked link
//         let full_path = PathBuf::from(base_dir).join(url_path);

//         if full_path.is_dir() {
//             // Serve the directory listing
//             let html = generate_directory_listing(&full_path);
//             let response = Response::from_string(html).with_header("Content-Type: text/html".parse().unwrap());
//             request.respond(response).unwrap();
//         } else if full_path.is_file() {
//             // Handle file download or display
//             let response = Response::from_file(fs::File::open(&full_path).unwrap())
//                 .with_header("Content-Type: application/octet-stream".parse().unwrap());
//             request.respond(response).unwrap();

//             // Execute a function when a file link is clicked
//             execute_on_click(&url_path);
//         } else {
//             // Handle 404
//             let response = Response::from_string("404 - Not Found").with_status_code(404);
//             request.respond(response).unwrap();
//         }
//     }
// }

// pub fn generate_directory_listing(path: &PathBuf) -> String {
//     let mut html = String::new();
//     html.push_str("<ul>");
//     for entry in fs::read_dir(path).unwrap() {
//         if let Ok(entry) = entry {
//             let file_name = entry.file_name().into_string().unwrap();
//             let file_type = entry.file_type().unwrap();
//             if file_type.is_dir() {
//                 html.push_str(&format!(
//                     "<li><a href=\"/{}/\">{}/</a></li>",
//                     file_name, file_name
//                 ));
//             } else {
//                 html.push_str(&format!(
//                     "<li><a href=\"/{}\">{}</a></li>",
//                     file_name, file_name
//                 ));
//             }
//         }
//     }
//     html.push_str("</ul>");
//     html
// }

// pub fn execute_on_click(file_path: &str) {
//     // Replace this with your custom logic
//     println!("File clicked: {}", file_path);
// }
