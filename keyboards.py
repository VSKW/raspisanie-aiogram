from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#Создание кнопопок и клавиатуры
#Начало
b1 = KeyboardButton('Расписание')
b2 = KeyboardButton('Домашка')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(b1, b2)

#Возврат
b10 = KeyboardButton('Назад')


#Дни
b3 = KeyboardButton('Понедельник')
b4 = KeyboardButton('Вторник')
b5 = KeyboardButton('Среда')
b6 = KeyboardButton('Четверг')
b7 = KeyboardButton('Пятница')
b8 = KeyboardButton('Суббота')
kb_day = ReplyKeyboardMarkup(resize_keyboard=True)
kb_day.insert(b3).insert(b4).insert(b5).insert(
    b6).insert(b7).insert(b8).add(b10)


#Загрузка
b11 = KeyboardButton('Загрузить')
b13 = KeyboardButton('Посмотреть')
b15 = KeyboardButton('Удалить')
kb_hw = ReplyKeyboardMarkup(resize_keyboard=True)
kb_hw.row(b11, b10, b13).add(b15)


#Отмена
b12 = KeyboardButton('Отмена')
kb_canc = ReplyKeyboardMarkup(resize_keyboard=True)
kb_canc.add(b12)
