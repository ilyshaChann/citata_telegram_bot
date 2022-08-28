from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
x1 = KeyboardButton("Да!")
x2 = KeyboardButton("Нет.")

y = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(x1,x2)