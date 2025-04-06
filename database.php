<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "crud";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if form fields are set and not empty
    if(isset($_POST["username"]) && isset($_POST["email"]) && isset($_POST["pwd"]) && 
       !empty($_POST["username"]) && !empty($_POST["email"]) && !empty($_POST["pwd"]) ) {
        
        // Get form data
        $username = $_POST["username"];
        $email = $_POST["email"];
        $password = $_POST["pwd"];
        

            // Hash the password for security
            $hashed_password = password_hash($password, PASSWORD_DEFAULT);

            // Prepare and bind the insert statement
            $stmt = $conn->prepare("INSERT INTO accounts (email, pwd, username) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $email, $hashed_password, $username);

            // Execute the statement
            if ($stmt->execute()) {
                echo "<br>Registration successful!";
                echo "<br>";
                echo "<h1>NOW TRY TO LOGIN</h1>";
                echo "<script>
                setTimeout(function(){
                    window.location.href = 'http://localhost/S&U/home.php';
                }, 3000); // Redirect after 3 seconds
                </script>";// Redirect to the desired page after 3 seconds
                exit;
            } else {
                echo "Error: " . $stmt->error;
            }

            // Close statement
            $stmt->close();
        }
    } else {
        echo "<br><br>Please fill out all the fields.";
        echo "<br>";
    }
    // Close connection
    $conn->close();

?>



