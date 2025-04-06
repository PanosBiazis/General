<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S&U - Dress to Impress</title>
    <link rel="stylesheet" href="explore.css">
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
                <h1>S&U</h1>
                <p class="slogan">Dress to Impress</p>
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
    <section class="explore-now">
        <h2>Latest Articles</h2>
        <p>Stay updated with our latest insights, trends, and tips in fashion.</p>
        <div class="articles-container">
            <article class="article">
                <img src="path/to/article-image1.jpg" alt="Article Title 1">
                <h3><a href="path/to/article1.html">5 Tips to Elevate Your Style</a></h3>
                <p>Discover simple tips to enhance your wardrobe and boost your confidence.</p>
                <span class="date">Published on: October 30, 2024</span>
            </article>
            <article class="article">
                <img src="path/to/article-image2.jpg" alt="Article Title 2">
                <h3><a href="path/to/article2.html">The Must-Have Accessories for 2024</a></h3>
                <p>Explore the essential accessories to complement your outfits this season.</p>
                <span class="date">Published on: October 15, 2024</span>
            </article>
            <article class="article">
                <img src="path/to/article-image3.jpg" alt="Article Title 3">
                <h3><a href="path/to/article3.html">Trends You Can't Miss This Fall</a></h3>
                <p>Get ready for the fall season with these trending styles.</p>
                <span class="date">Published on: October 1, 2024</span>
            </article>
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