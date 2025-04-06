<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Collection - S&U Fashion</title>
    <link rel="stylesheet" href="home.css"> <!-- Your existing CSS -->
    <link rel="stylesheet" href="collection.css"> <!--New CSS file for the collection -->
</head>
<body>

    <!-- Header Section -->
    <header>
        <div class="top-bar">
            <div class="email-info">
                <img src="email1.jpg" alt="Email Icon" class="icon">
                <p>info@su-fashion.com</p>
            </div>
            <div class="logo">
                <a href="home.php"><h1>S&U</h1></a>
                <p class="slogan">Dress to Impress</p>
            </div>
            <div class="social-links">
                <img src="like.png" alt="Like Icon" class="icon">
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
                <li><a target="blank" href="login.php">Login</a></li>
                <li>
                    <form class="search-form" action="search.html" method="GET"> <!-- Action for the search results page -->
                        <input type="text" name="query" placeholder="Search..." required>
                        <button type="submit">Search</button>
                    </form>
                </li>
            </ul>
        </nav>
    </header>

    <!-- Collection Section -->
    <section class="collection">
        <h2>Our Collection</h2>
        <p>Explore our latest curated pieces</p>
        <div class="collection-grid">
            <div class="collection-item">
                <img src="jacket1.png" alt="Stylish Jacket">
                <h3>Jackets</h3>
                <p>Elevate your wardrobe with this must-have jacket.</p>
                <button class="view-details">View Details</button>
            </div>
            <div class="collection-item">
                <img src="t-shirt1.png" alt="Casual T-Shirt">
                <h3>Casual T-Shirt</h3>
                <p>Comfort meets style in our latest t-shirt design.</p>
                <button class="view-details">View Details</button>
            </div>
            <div class="collection-item">
                <img src="sneaker.png" alt="Chic Sneakers">
                <h3>Chic Sneakers</h3>
                <p>Step out in style with these trendy sneakers.</p>
                <button class="view-details">View Details</button>
            </div>
            <div class="collection-item">
                <img src="accessories.png" alt="Accessories">
                <h3>Accessories</h3>
                <p>Perfect for any occasion, this dress is a must-have.</p>
                <button class="view-details">View Details</button>
            </div>
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
