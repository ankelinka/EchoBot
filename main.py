import asyncio
import time

from aiogram import html
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import bot, dp, Colors


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Я - эхо-бот. Просто отправь мне сообщение, и я повторю его.")


@dp.message()
async def echo_func(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception as e:
        error_message = f"{html.bold('Возникла ошибка:')} {html.code(e)}"
        await message.answer(error_message)


async def main_func():
    try:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        bot_username = await bot.get_me()
        log_message = (
            f"{Colors.BOLD}{Colors.GREEN}Bot started: "
            f"{Colors.WARNING}[{current_time}] "
            f"{Colors.BOLD}{Colors.BLUE}[@{bot_username.username}]"
        )
        print(log_message)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        await bot.session.close()
        print(f"{Colors.BOLD}{Colors.ERROR}{e}")


if __name__ == '__main__':
    try:
        asyncio.run(main_func())
    except KeyboardInterrupt:
        print("Бот остановлен")
