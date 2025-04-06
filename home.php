<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S&U - Dress to Impress</title>
    <link rel="stylesheet" href="home.css">
    <!-- C:\Users\papam\Desktop\clothes site\css\home.css -->
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="top-bar">
            <!-- Email Section with Icon -->
            <div class="email-info">
                <img src="email1.jpg" alt="Email Icon" class="icon">
                <!-- C:\Users\papam\Desktop\clothes site\images\email1.jpg -->
                <p>info@su-fashion.com</p>
            </div>

            <!-- Centered Logo -->
            <div class="logo">
                <a href="home.php"><h1>S&U</h1></a>
                <p class="slogan">Dress to Impress</p>
            </div>

            <!-- Social Media Links and Like Icon -->
            <div class="social-links">
                <img src="like.png" alt="Like Icon" class="icon"> <!-- Like button icon ./clothes site -->
                <a href="https://instagram.com" target="_blank"><img src="instagram.png" alt="Instagram Icon" class="icon"></a>
                <!-- C:\Users\papam\Desktop\clothes site\images\instagram.png -->
                <a href="https://tiktok.com" target="_blank"><img src="tiktok.png" alt="TikTok Icon" class="icon"></a>
                <!-- C:\Users\papam\Desktop\clothes site\images\tiktok.png -->
                <a href="https://youtube.com" target="_blank"><img src="youtube.png" alt="YouTube Icon" class="icon"></a>
                <!-- C:\Users\papam\Desktop\clothes site\images\youtube.png -->
            </div>
        </div>
        
        <!-- Navigation Bar -->
        <nav>
            <ul>
                <li><a href="home.php">Home</a></li>
                <!-- C:\Users\papam\Desktop\clothes site\html\home.html -->
                <li><a href="aboutus.php">About Us</a></li>
                <!-- C:\Users\papam\Desktop\clothes site\html\aboutus.html -->
                <li><a href="collection.php">Collection</a></li>
                <!-- C:\Users\papam\Desktop\clothes site\html\collection.html -->
                <li><a target="_blank" href="login.php">Login</a></li>
                <!-- C:\Users\papam\Desktop\clothes site\html\login.html -->
                <li>
                    <form class="search-form" action="search.html" method="GET"> <!-- Action for the search results page -->
                        <input type="text" name="query" placeholder="Search..." required>
                        <button type="submit">Search</button>
                    </form>
                </li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h2>Welcome to S&U</h2>
        <p>Discover the latest trends, tips, and style guides</p>
        <button class="explore-now"><a href="explore.html">Explore Now</a></button>
        <!-- C:\Users\papam\Desktop\clothes site\html\explore.html -->
    </section>

    <!-- Blog Posts Section -->
    <section class="blog-posts">
        <div class="post">
            <div class="post1">
            <img src="sunglasses.png" alt="Men's Sunglasses">
            <!-- C:\Users\papam\Desktop\clothes site\images\sunglasses.png -->
            <h3>Latest Trends in Men's Sunglasses</h3>
            <p>Explore the newest styles to elevate your look.</p>
            </div>
        </div>
        <div class="post">
            <img src="sneaker.png" alt="Men's Sneakers">
            <!-- C:\Users\papam\Desktop\clothes site\images\sneaker.png -->
            <h3>Men's Sneakers: Comfort Meets Fashion</h3>
            <p>Discover how to pair sneakers with formal and casual wear.</p>
        </div>
        <div class="post">
            <img src="t-shirt.png" alt="Men's T-Shirt">
            <!-- C:\Users\papam\Desktop\clothes site\images\t-shirt.png -->
            <h3>2024 T-Shirt Collection</h3>
            <p>Minimalist yet stylish: A breakdown of the latest t-shirt designs.</p>
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
