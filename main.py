import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types.message import ContentType
import datetime

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token='6225836939:AAGmvW3hVyguebhD4_NE8ik1PhDVosVwN-I', parse_mode=types.ParseMode.HTML)

# Создаем объект диспетчера
dp = Dispatcher(bot)

first_id = '351162658'
second_id = '1269197191'
# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Привет! Я эхобот. Я буду повторять все сообщения, которые ты мне отправишь.")
    while True:
        now = datetime.time()
        if now.hour in [12, 15, 17, 18, 19, 20]:
            await bot.send_message(first_id, 'Как успехи?')
            await bot.send_message(second_id, 'Как успехи?')

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

