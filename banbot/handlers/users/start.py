import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from banbot.loader import dp
from banbot.models import User, Chat


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}!")


@dp.message_handler(Command('register'))
async def bot_register(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    # Вызываем синхронный код Django через run_in_executor
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, create_or_update_user, chat_id, first_name, last_name, username)
    await message.answer("Done!")

def create_or_update_user(chat_id, first_name, last_name, username):
    user, created = User.objects.update_or_create(
        chat_id=chat_id,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
        }
    )


@dp.message_handler(Command('registerchat'))
async def bot_registerchat(message: types.Message):
    chat_id = message.chat.id
    title = message.chat.title

    # Вызываем синхронный код Django через run_in_executor
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, create_or_update_chat, chat_id, title)
    await message.answer("Done!")

def create_or_update_chat(chat_id, title):
    chat, created = Chat.objects.update_or_create(
        chat_id=chat_id,
        defaults={
            'title': title,
        }
    )
