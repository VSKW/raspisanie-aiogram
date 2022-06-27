# import
import types
import os
import sqlite3 as sq
# import библиотеки телеграма
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# import по файлам
from config import token
from keyboards import kb, kb_day, kb_canc, kb_hw


#Память
stor = MemoryStorage


#Создание бота и диспетчера
bot = Bot(token)
dp = Dispatcher(bot, storage=stor())


#Машина состояний
class FSMAdmin(StatesGroup):
    sub = State()
    day = State()
    text = State()
    photo = State()


#Start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    try:
        await message.reply(f"Привет!\n"
                            f'Давай сразу к делу, выреби кнопку', reply_markup=kb)
    except:
        await message.answer("error, try again")
        print("ошибка в блоке start")


#Блок расисания
@dp.message_handler(lambda message: 'Расписание' in message.text)
async def rasp(message: types.Message):
    try:
        await message.reply('На какой день?', reply_markup=kb_day)
    except:
        await message.reply('error, try again')
        print("Ошбика в блоке Расписание")


@dp.message_handler(lambda message: 'Понедельник' in message.text)
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


@dp.message_handler(lambda message: 'Вторник' in message.text)
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


@dp.message_handler(lambda message: 'Среда' in message.text)
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


@dp.message_handler(lambda message: 'Четверг' in message.text)
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


@dp.message_handler(lambda message: 'Пятница' in message.text)
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


@dp.message_handler(lambda message: 'Суббота' in message.text)
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


@dp.message_handler(lambda message: 'Домашка' in message.text)
async def hw(message: types.Message):
    try:
        await message.reply('Хочешь загрузить или посмотреть дз?', reply_markup=kb.hw)
    except:
        await message.reply('error, try again')
        print('ошибка в блоке дз')


#Сохранение
def sql_start():
    try:
        global base, cur
        base = sq.connect('Homework.db')
        cur = base.cursor()
        if base:
            print('Data base connected OK')
        base.execute('CREATE TABLE IF NOT EXISTS how(sub TEXT, day TEXT, text TEXT, photo TEXT)')
        base.commit()
    except:
        pass


async def sql_add(state):
    try:
        async with state.proxy() as data:
            cur.execute('INSERT INTO how VALUES (?, ?, ?, ?)', tuple(data.values()))
            base.commit()
    except:
        pass


async def sql_read(message):
    try:
        for i in cur.execute('SELECT * FROM how').fetchall():
            await bot.send_photo(message.from_user.id, i[-1], f'Предмет: {i[0]}\nДата: {i[1]}\nЗадание: {i[2]}\n')
    except:
        pass


#Удаление
async def sql_read2():
    try:
        return cur.execute('SELECT * FROM how').fetchall()
    except:
        pass
async def del_sql(data):
    try:
        cur.execute('DELETE FROM how WHERE sub == ?', (data,))
        base.commit()
    except:
        pass


#Загрузка
@dp.message_handler(lambda message: 'Загрузить' in message.text, state=None)
async def cm_start(message: types.Message):
    try:
        await FSMAdmin.sub.set()
        await message.reply(f'По какому предмету ты хочешь загрузить задание?\n'
                            f'Тебе нужно обязательно либо закончить загрузку задания, либо нажать отмену\n '
                            f'(это нужно для корректной работы)'
                            f'\nБот восприимает текст.', reply_markup=kb_canc)
    except:
        pass


#Просмотр
@dp.message_handler(lambda message: 'Посмотреть' in message.text)
async def dz(message: types.Message):
    try:
        await sql_read(message)
    except:
        pass


#Отмена
@dp.message_handler(lambda message: 'Отмена' in message.text, state='*')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel(message: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK\nЗагрузка отменена', reply_markup=kb)
    except:
        pass


@dp.message_handler(state=FSMAdmin.sub)
async def loadsubject(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['sub'] = message.text
        await FSMAdmin.next()
        await message.reply('На какую дату оно было задано?\nМожешь просто написать день недели')
    except:
        pass


@dp.message_handler(state=FSMAdmin.day)
async def loadday(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['day'] = message.text
        await FSMAdmin.next()
        await message.reply('Какое задание?')
    except:
        pass


@dp.message_handler(state=FSMAdmin.text)
async def loadtext(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['text'] = message.text
        await FSMAdmin.next()
        await message.reply('Загрузите фото\nЭто нужно сделать обязательно. Фото может быть любое')
    except:
        pass


@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await sql_add(state)
        await state.finish()
        await message.reply('ОК\nЗагрузка завершена', reply_markup=kb)
    except:
        pass


#Блок возрата на начальную страницу
@dp.message_handler(lambda message: "Назад" in message.text)
async  def menu(message: types.Message):
    try:
        await message.reply('Основные возможности на данный момент:', reply_markup=kb)
    except:
        await message.reply('error, try again')
        print('ошибка в блоке меню')


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback(call: types.CallbackQuery):
    await del_sql(call.data.replace('del ', ''))
    await call.answer(text=f'{call.data.replace("del ", "")} удален(а)')


@dp.message_handler(lambda message: 'Удалить' in message.text)
async def delete(message: types.Message):
    read = await sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[-1], f'Предмет: {ret[0]}\nДата: {ret[1]}\nЗадание: {ret[2]}\n')
        await bot.send_message(message.from_user.id, text='Задание выше', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))


sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
