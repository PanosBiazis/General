<?php
// api_response.php
header('Content-Type: application/json');

if (isset($_GET['input'])) {
    $user_input = escapeshellarg($_GET['input']);
    $output = shell_exec("python3 chat_logic.py " . $user_input);

    if ($output) {
        echo json_encode(array("response" => trim($output)));
    } else {
        echo json_encode(array("response" => "There was an error processing your request."));
    }
} else {
    echo json_encode(array("response" => "No input provided"));
}
?>
