import types
import sqlite3 as sq
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import kb, kb_canc
from create_bot import dp, bot


#Машина состояний


class FSMAdmin(StatesGroup):
        sub = State()
        day = State()
        text = State()
        photo = State()


#Сохранение


def sql_start():
    try:
        global base, cur
        base = sq.connect('Homework.db')
        cur = base.cursor()
        if base:
            print('Data base connected OK')
        base.execute(
            'CREATE TABLE IF NOT EXISTS how(sub TEXT, day TEXT, text TEXT, photo TEXT)')
        base.commit()
    except:
        pass


async def sql_add(state):
    try:
        async with state.proxy() as data:
            cur.execute('INSERT INTO how VALUES (?, ?, ?, ?)',
                        tuple(data.values()))
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


#Просмотр
#@dp.message_handler(lambda message: 'Посмотреть' in message.text)


async def dz(message: types.Message):
    try:
        await sql_read(message)
    except:
        pass


#Загрузка
#@dp.message_handler(lambda message: 'Загрузить' in message.text, state=None)


async def cm_start(message: types.Message):
    try:
        await FSMAdmin.sub.set()
        await message.reply(f'По какому предмету ты хочешь загрузить задание?\n'
                            f'Тебе нужно обязательно либо закончить загрузку задания, либо нажать отмену\n '
                            f'(это нужно для корректной работы)'
                            f'\nБот восприимает текст.', reply_markup=kb_canc)
    except:
        pass


#Отмена
#@dp.message_handler(lambda message: 'Отмена' in message.text, state='*')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')


async def cancel(message: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK\nЗагрузка отменена', reply_markup=kb)
    except:
        pass


#@dp.message_handler(state=FSMAdmin.sub)


async def loadsubject(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['sub'] = message.text
        await FSMAdmin.next()
        await message.reply('На какую дату оно было задано?\nМожешь просто написать день недели')
    except:
        pass


#@dp.message_handler(state=FSMAdmin.day)


async def loadday(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['day'] = message.text
        await FSMAdmin.next()
        await message.reply('Какое задание?')
    except:
        pass


#@dp.message_handler(state=FSMAdmin.text)


async def loadtext(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['text'] = message.text
        await FSMAdmin.next()
        await message.reply('Загрузите фото\nЭто нужно сделать обязательно. Фото может быть любое')
    except:
        pass


#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)


async def load_photo(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await sql_add(state)
        await state.finish()
        await message.reply('ОК\nЗагрузка завершена', reply_markup=kb)
    except:
        pass


#Просмотр
#@dp.message_handler(lambda message: 'Посмотреть' in message.text)


async def dz(message: types.Message):
    try:
        await sql_read(message)
    except:
        pass


def register_handlers_hw(dp: Dispatcher):
    dp.register_message_handler(cm_start, lambda message: 'Загрузить' in message.text, state=None)
    dp.register_message_handler(cancel, lambda message: 'Отмена' in message.text, state='*')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(loadsubject, state=FSMAdmin.sub)
    dp.register_message_handler(loadday, state=FSMAdmin.day)
    dp.register_message_handler(loadtext, state=FSMAdmin.text)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(dz, lambda message: 'Посмотреть' in message.text)