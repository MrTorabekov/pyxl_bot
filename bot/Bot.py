import asyncio
import logging
import openpyxl
from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F

logging.basicConfig(level=logging.INFO)

myToken = "6707467105:AAHIoMkpDRZIhsM7VGGGmiA3pCz0Abue9JU"
bot = Bot(token=myToken)
dp = Dispatcher()

count = 1


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply(f"Hello {message.from_user.full_name}.")
    b = count + 1

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet["A1"] = "id"
    sheet["B1"] = "name"

    sheet[f"A{b}"] = message.from_user.id
    sheet[f"B{b}"] = message.from_user.full_name

    workbook.save('data.xlsx')





# @dp.message(Command("contact_and_location"))
# async def cmd_special_buttons(message: types.Message):
#     kb1 = [
#
#         [types.KeyboardButton(text="Lokatsiya olish", request_location=True)],
#         [types.KeyboardButton(text="Contact yuborish", request_contact=True)],
#
#     ]
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb1,
#         resize_keyboard=True,
#         input_field_placeholder="Word"
#     )
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
