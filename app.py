from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
DEBUG = os.getenv('DEBUG')
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

print(DEBUG)
print(DATABASE_URL)
