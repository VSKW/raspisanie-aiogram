import types
from aiogram import types
from aiogram import Dispatcher

from keyboards import kb, kb_day, kb_hw
from create_bot import dp

#Блок расисания
#@dp.message_handler(lambda message: 'Расписание' in message.text)
async def rasp(message: types.Message):
    try:
        await message.reply('На какой день?', reply_markup=kb_day)
    except:
        await message.reply('error, try again')
        print("Ошбика в блоке Расписание")


#@dp.message_handler(lambda message: 'Понедельник' in message.text)
async def mon(message: types.Message):
    try:
        await message.reply(f"14:15-15:00 Индивид проект Амарантова 106\n"
                            f'15:10-15:55 Методы науч познания 408 Ковалёва\n'
                            f'15:10-15:55 Методы науч познания 408 Ковалёва\n'
                            f'16:05-16:50 Физика 408\n'
                            f'17:00-17:45 Физика 408'
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Понедельник")


#@dp.message_handler(lambda message: 'Вторник' in message.text)
async def tue(message: types.Message):
    try:
        await message.reply(f'9:00-9:45 1 подгруппа Информатика Колозян 312\n'
                            f'9:55-10:40 1 подгруппа Информатика Колозян 312\n'
                            f'11:45-12:30 История Енина 404\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'13:00-13:45 Математика Колозян 312\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'14:15-15:00 Математика Колозян 312\n'
                            f'15:10-15:55 Математика Колозян 106\n'
                            f'16:05-16:50 Математика Колозян 106\n'
                            f'17:00-17:45 Родная лит-ра(Русский язык) Ермолова 403\n'
                            f'17:55-18:40 Родная лит-ра(Русский язык) Ермолова 403\n'
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Вторник")


#@dp.message_handler(lambda message: 'Среда' in message.text)
async def wen(message: types.Message):
    try:
        await message.reply(f'9:55-10:40 2 подгруппа Информатика Колозян 309\n'
                            f'10:50-11:35 2 подгруппа Информатика Колозян 309\n'
                            f'11:45-12:30 ОБЖ Широков 408\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'13:00-13:45 Математика Колозян 309\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'14:15-15:00 Математика Колозян 309\n'
                            f'15:10-15:55 Индивид проект Амарантова 305\n'
                            f'16:05-16:50 Индивид проект Амарантова 305\n'
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Среда")


#@dp.message_handler(lambda message: 'Четверг' in message.text)
async def th(message: types.Message):
    try:
        await message.reply(f"9:00-9:45 Информатика Колозян 312\n"
                            f"9:55-10:40 Информатика Колозян 312\n"
                            f"10:50-11:35 Информатика Колозян 312\n"
                            f"11:45-12:30 Информатика Колозян 312\n"
                            f"ОБЕД 30 МИНУТ\n"
                            f"13:00-13:45 Физкультура Кебец 110\n"
                            f"ОБЕД 30 МИНУТ\n"
                            f"14:15-15:00 Физкульура Кебец 110\n"
                            f"15:10-15:55 Человек и общество Енина 404\n"
                            f"16:05-16:50 Человек и общество Енина 404\n"
                            f"17:00-17:45 Человек и общество Енина 404\n"
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Четверг")


#@dp.message_handler(lambda message: 'Пятница' in message.text)
async def fri(message: types.Message):
    try:
        await message.reply(f'10:50 - 11:35 1 погруппа Ин яз Бородина 314\n'
                            f'11:45-12:30 1 подгруппа Ин яз Бородина 314\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'13:00-13:45 Физика/Астрономия Ковалёва 408\n'
                            f'ОБЕД 30 МИНУТ\n'
                            f'14:15-15:00 Физика/Астрономия Ковалёва 408\n'
                            f'15:10-15:55 Литература Ермолова 403\n'
                            f'16:05-16:50 Литература Ермолова 403\n'
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Пятница")


#@dp.message_handler(lambda message: 'Суббота' in message.text)
async def sat(message: types.Message):
    try:
        await message.reply(f'12:40-13:25 Литература/Русский Ермолова 308\n'
                            f'13:45-14:30 Литература/Русский Ермолова 308\n'
                            f'14:40-15:25 Физкультура Кебец 110/Ин яз Бородина 302 и Диланян 314\n'
                            f'15:35-16:20 Физкультура Кебец 110/Ин яз Боридина 302 и Диланян 314\n'
                            f'16:30-17:15 Ин яз Диланян 314\n'
                            f'17:25-18:10 Ин яз Диланян 314'
                            )
    except:
        await message.reply('error, try again')
        print("ошибка в блоке Суббота")


#@dp.message_handler(lambda message: 'Домашка' in message.text)
async def hw(message: types.Message):
    try:
        await message.reply('Хочешь загрузить или посмотреть дз?', reply_markup=kb_hw)
    except:
        await message.reply('error, try again')
        print('ошибка в блоке дз')

# Блок возрата на начальную страницу


#@dp.message_handler(lambda message: "Назад" in message.text)
async def menu(message: types.Message):
    try:
        await message.reply('Основные возможности на данный момент:', reply_markup=kb)
    except:
        await message.reply('error, try again')
        print('ошибка в блоке меню')

def register_handlers_raspisenie(dp: Dispatcher):
    dp.register_message_handler(rasp, lambda message: 'Расписание' in message.text)
    dp.register_message_handler(mon, lambda message: 'Понедельник' in message.text)
    dp.register_message_handler(tue, lambda message: 'Вторник' in message.text)
    dp.register_message_handler(wen, lambda message: 'Среда' in message.text)
    dp.register_message_handler(th, lambda message: 'Четверг' in message.text)
    dp.register_message_handler(fri, lambda message: 'Пятница' in message.text)
    dp.register_message_handler(sat, lambda message: 'Суббота' in message.text)
    dp.register_message_handler(hw, lambda message: 'Домашка' in message.text)
    dp.register_message_handler(menu, lambda message: "Назад" in message.text)



