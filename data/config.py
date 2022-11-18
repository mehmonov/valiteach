from environs import Env
import os
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot toekn
ADMINS =   str(os.environ.get("ADMINS"))# adminlar ro'yxati
IP = str(os.environ.get("ip")) # Xosting ip manzili
