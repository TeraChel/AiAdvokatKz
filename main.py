import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from app.handlers import router


async def main():
    load_dotenv()
    bot = Bot(token = os.getenv('TG_TOKEN'))  # токен бота
    dp = Dispatcher(bot)  # создание диспетчера, который получает сообщения
    dp.include_router(router)
    try:
        await executor.start_pollingdp(dp, skip_updates = True) #скрипт обращается к серверу тг и спрашивает есть ли новое сообщение
    except Exception as e:
        print(f"Polling error: {e}")


if __name__ == '__main__': #конструкция для запуска main
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен") #для закрытия бота без огромного сообщения об ошибке
