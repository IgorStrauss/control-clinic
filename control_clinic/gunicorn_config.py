import os

from dotenv import load_dotenv

load_dotenv()

workers = 4
bind = "0.0.0.0:8000"
threads = 2

# Obtém a SECRET_KEY do ambiente
secret_key = os.environ.get("SECRET_KEY")


# Configuração específica do Flask-WTF
raw_env = ["SECRET_KEY=" + os.getenv("SECRET_KEY")]
