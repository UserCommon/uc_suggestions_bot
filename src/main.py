import logging
import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

load_dotenv()
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("TG_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
    print("Finished!")
