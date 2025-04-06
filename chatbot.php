<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $message = trim($_POST['message']);
    $response = "I'm just a simple PHP bot. You said: " . htmlspecialchars($message);
    echo $response;
}
?>