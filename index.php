<?php
ob_start();
header('Content-Type: application/json');

if (isset($_GET['input']) && !empty($_GET['input'])) {
    // Sanitize the input and prepare the Python command
    $user_input = escapeshellarg($_GET['input']);
    //$python_path = 'C:\Users\panag\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe';  // Update this with your correct Python path
    $python_path = 'C:\\Users\\panag\\AppData\\Local\\Microsoft\\WindowsApps\\python3.exe';

    $script_path = 'C:\\xampp\\htdocs\\chatbot\\chat_logic.py';  // Path to your Python script
    $command = $python_path . ' ' . $script_path . ' ' . $user_input;
    
    // Execute the Python script and capture the output
    $output = shell_exec($command . " 2>&1");

    // Return the output as a JSON response
    echo json_encode(array("response" => trim($output)));
} else {
    // If no input is provided, send a default message
    echo json_encode(array("response" => "No input provided"));
}

ob_end_flush();
?>

