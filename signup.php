<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - S&U</title>
    <link rel="stylesheet" href="signup.css">
</head>
<body>
    <header>
        <a class="text-button" href="home.php"><h1>S&U</h1></a>
        <p class="slogan">Dress to Impress</p>
    </header>

    <main>
        <section class="form-container">
            <div class="form-box">
                <h2>Sign Up</h2>
                <form action="database.php" method="POST">
                    <div class="input-group">
                        <label for="username">Name:</label>
                        <input type="text" id="username" name="username" required>
                    </div>
                    <div class="input-group">
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="input-group">
                        <label for="pwd">Password:</label>
                        <input type="pwd" id="pwd" name="pwd" required>
                    </div>
                    <button type="submit">Sign Up</button>
                </form>
                <p>Already have an account? <a id="login1" href="login.php">Login</a></p> <!-- Link to login page -->
            </div>
        </section>
    </main>
    <!-- Footer Section -->
    <footer>
        <div class="footer-content">
            <p>&copy; 2024 S&U. All Rights Reserved.</p>
        </div>
    </footer> 
</body>
</html>
