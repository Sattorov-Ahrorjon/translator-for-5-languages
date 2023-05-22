from aiogram import executor
import filters
import handlers
import middlewares
from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Default commands (/star and /help)
    await set_default_commands(dispatcher)

    # Notify the admin that the bot has started
    await on_startup_notify(dispatcher)

    # Create a database:
    db.create_table_users()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
