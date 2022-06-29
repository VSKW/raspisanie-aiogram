# import
import types
# import библиотеки телеграма
from aiogram import types
from aiogram.utils import executor
# import по файлам
from keyboards import kb
from create_bot import dp
from handlers import raspisanie, HW


raspisanie.register_handlers_raspisenie(dp)
HW.register_handlers_hw(dp)


#Start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    try:
        await message.reply(f"Привет!\n"
                            f'Давай сразу к делу, выреби кнопку', reply_markup=kb)
    except:
        await message.answer("error, try again")
        print("ошибка в блоке start")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
