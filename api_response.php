<?php
// Set the content type to JSON
header('Content-Type: application/json');

// Check if the user input is provided via GET request
if (isset($_GET['input'])) {
    // Sanitize user input to prevent shell injection
    $user_input = escapeshellarg($_GET['input']);
    
    // Define the command to run the Python script with the user input
    $command = "python3 C:\\xampp\\htdocs\\chatbot\\chat_logic.py " . $user_input;
    
    // Execute the command and capture the output
    $output = shell_exec($command . " 2>&1");
    
    // Return the response from the Python script as a JSON object
    echo json_encode(array("response" => trim($output)));
} else {
    // If no input is provided, return a default message
    echo json_encode(array("response" => "No input provided"));
}
?>
