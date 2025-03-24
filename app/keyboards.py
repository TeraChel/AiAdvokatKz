from gc import callbacks

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

sex = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Мужчина')],
                                       [KeyboardButton(text = 'Женщина')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...') # sex - экземпляр класса, а keyboard принимает двумерный массив
social_status = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Ребенок'), KeyboardButton(text = 'Школьник')],
                                                [KeyboardButton(text = 'Студент'), KeyboardButton(text = 'Пенсионер')],
                                                [KeyboardButton(text = 'Безработный(-ая)')],
                                                [KeyboardButton(text = 'Взрослый, без льгот')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')