import os

# Используется, чтобы сделать универсальный путь к JSON-файлу и БД
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

RAW_JSON_PATH = os.path.join(ROOT_DIR, 'data', 'raw_data.json')
DATABASE_PATH = os.path.join(ROOT_DIR, 'data')

# Параметр пагинации в DAO для запросов, отдающих несколько записей
PAGE_SIZE = 10

# Хэширование паролей
SECRET = 'S$cReT'
JWT_ALGO = 'HS256'
HASH_NAME = 'sha256'
SALT = b'wASodAD'
ITERATIONS = 10_000
