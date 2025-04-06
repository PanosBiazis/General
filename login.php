<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login & Sign Up - S&U</title>
    <!-- <link rel="stylesheet" href="login.css"> -->
    <style>
        body {
            background-color: lightseagreen; /* Background color */
        }
        .login {/*Login Form*/
             position: absolute;
             text-align: center;
             left:750px;
             width: 400px;
             height: 300px;
             border: 10px solid darkblue;
             background-color: white;
        }
        input{
            width: 300px;
            height: 30px;
        }
        .submit {
            position: absolute;
            top :140px;
            left: 70px;
        }
    </style>  
</head>
<body>
<fieldset class="login">
<form action="" method="post">
    <label style="position:relative; left:10px;">Email:</label><!--Email field-->
    <input style="position:relative; left:10px;" type="text" name="email" required><br><br>
    <label>Password:</label><!--Password field-->
    <input type="password" name="pwd" required><br>
    <div class="submit"><!--Submit button-->
    <input type="submit" value="Login"><br><br>
    <a href="Start.php">First page</a><br><br><br>
    <a href="Register.php">Register</a><br><br><br>
    <a href="http://localhost:8080/CRUD/CRUD-BR_User.php">login without account</a><br><br>
    </div><!--Submit button Ends here-->
</form>
<?php
// Start session to store user data
session_start();
// Define the database connection details
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "crud";

// Create a new MySQLi connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if the connection was successful
if ($conn->connect_error) {
    // If the connection failed, display an error message
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {//Login process
    // Check if email and password are set in the $_POST array
    if(isset($_POST["email"]) && isset($_POST["pwd"])) {
        //Get email and password values from the form
        $email = $_POST["email"];
        $password = $_POST["pwd"];

        // Prepare a SQL statement to retrieve the user with the given email
        $sql = "SELECT * FROM accounts WHERE email = ?";//SQL statement
        $stmt = $conn->prepare($sql);//Prepare the statement
        
        // Bind parameters to the prepared statement
        $stmt->bind_param("s", $email);
        
        // Execute the prepared statement
        $stmt->execute();
        
        // Get the result of the query
        $result = $stmt->get_result();

        // Check if there is a user with the given email
        if ($result->num_rows == 1) {
            // Fetch the user's data from the result
            $user = $result->fetch_assoc();
            
            // Verify the password
            if (password_verify($password, $user['pwd'])) {
                // If password is correct, login successful
                echo "Login successful!";
                // Store the username in a session variable
                // $_SESSION['username'] = $user['username'];
                echo "OK!!!";// Redirect to the desired page after 3 seconds
                exit; // Exit the script after successful login
            } else {
                // If password is incorrect
                echo "Invalid password.";
            }
        } else {
            // If no user with the given email was found
            echo "Invalid username or password.";
        }
        
        // Close the prepared statement
        $stmt->close();
    } else {
        // If email or password is not set in the $_POST array
        echo "<br>Please enter both email and password.";
    }
}
?>
</fieldset>  
</html>
   