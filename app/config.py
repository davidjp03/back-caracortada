import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
