<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S&U - Dress to Impress</title>
    <link rel="stylesheet" href="aboutus.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="top-bar">
            <!-- Email Section with Icon -->
            <div class="email-info">
                <img src="email1.jpg" alt="Email Icon" class="icon">
                <p>info@su-fashion.com</p>
            </div>

            <!-- Centered Logo -->
            <div class="logo">
                <a href="home.php"><h1>S&U</h1></a>
                <p class="slogan">dress to impress</p>
            </div>

            <!-- Social Media Links and Like Icon -->
            <div class="social-links">
                <img src="like.png" alt="Like Icon" class="icon"> <!-- Like button icon -->
                <a href="https://instagram.com" target="_blank"><img src="instagram.png" alt="Instagram Icon" class="icon"></a>
                <a href="https://tiktok.com" target="_blank"><img src="tiktok.png" alt="TikTok Icon" class="icon"></a>
                <a href="https://youtube.com" target="_blank"><img src="youtube.png" alt="YouTube Icon" class="icon"></a>
            </div>
        </div>
        
        <!-- Navigation Bar -->
        <nav>
            <ul>
                <li><a href="home.php">Home</a></li>
                <li><a href="aboutus.php">About Us</a></li>
                <li><a href="collection.php">Collection</a></li>
                <li><a target="_blank" href="login.php">Login</a></li>
                <li>
                    <form class="search-form" action="search.html" method="GET"> <!-- Action for the search results page -->
                        <input type="text" name="query" placeholder="Search..." required>
                        <button type="submit">Search</button>
                    </form>
                </li>
            </ul>
        </nav>
    </header>

    <!-- About Us Section -->
    <section class="about-us">
        <h2>About Us</h2>
        <div class="about-content">
            <p>At S&U, we believe that fashion is more than just clothing; it’s a form of self-expression. Founded in 2020, our brand strives to bring the latest trends and timeless styles to every individual, regardless of age or background. Our mission is to inspire confidence and creativity through our diverse collections.</p>
            <p>We source our materials ethically, ensuring quality while being mindful of our environmental impact. Our team is passionate about creating garments that not only look good but feel good. We value inclusivity, offering a wide range of sizes and styles to accommodate all body types.</p>
            <p>We are dedicated to innovation, constantly evolving our designs and practices to meet the needs of our customers. Thank you for being a part of our journey. Together, let's dress to impress.</p>
        </div>
        <div class="signature">
            <p>Best Regards,</p>
            <p>The S&U Team</p>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="footer-content">
            <p>&copy; 2024 S&U. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>
