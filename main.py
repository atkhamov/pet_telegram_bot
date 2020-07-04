import asyncio
import controllers

#Dispatcher - доставщик наших "update"ов
#executor - запускатель бота
# from aiogram import Bot, Dispatcher, executor
# from config import BOT_TOKEN

#поток для обработки всех событий, чтобы работать с асинхронными библиотеками
loop = asyncio.get_event_loop()
telegram = controllers.Telegram(loop=loop)
# bot = Bot(BOT_TOKEN, parse_mode="HTML")
# dp = Dispatcher(bot, loop=loop)

# if __name__ == "__main__":
#     from handlers import dp, send_to_admin
#     executor.start_polling(dp, on_startup=send_to_admin)

futures = [
    asyncio.ensure_future(telegram.create_session()),
    asyncio.ensure_future(telegram.start_session()),
]

loop.run_until_complete(asyncio.gather(*futures))