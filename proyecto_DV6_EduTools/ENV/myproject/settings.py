import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga las variables del archivo .env
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Ahora puedes acceder a las variables de entorno
SECRET_KEY = os.getenv('SECRET_KEY')

# Configuración de la base de datos MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'), # Usa 'localhost' si no está en .env
        'PORT': os.getenv('DATABASE_PORT', '3306'),     # Usa '3306' si no está en .env
    }
}

# Otras variables como DEBUG
DEBUG = os.getenv('DEBUG', 'False') == 'True' # Convierte el string a booleano