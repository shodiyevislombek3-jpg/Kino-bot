from aiogram import Router
from aiogram.types import Message
import sqlite3

router = Router()

@router.message()
async def movie_handler(message: Message):
    code = message.text.strip()

    db = sqlite3.connect("kino.db")
    cursor = db.cursor()

    cursor.execute(
        "SELECT file_id FROM movies WHERE code=?",
        (code,)
    )
    movie = cursor.fetchone()

    if movie:
        await message.answer_video(movie[0])
    else:
        await message.answer(
            "❌ Bunday koddagi kino topilmadi."
        )
