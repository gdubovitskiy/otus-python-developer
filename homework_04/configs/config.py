DB_ENGINE = "asyncpg"
# DB_ENGINE = "pg8000"
DB_USER = "postgres"
DB_PASSWORD = "secretpassword"
DB_NAME = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432

DB_URL = f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DB_ECHO = True
# DB_ECHO = False

BASE_DATA_URL = 'https://jsonplaceholder.typicode.com'