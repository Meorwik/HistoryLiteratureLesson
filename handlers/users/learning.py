from data.lesson_material.lesson_materials import greece_cities_info, learn_phase_start, additional_info
from keyboards.default.default_keyboard import finished_exercise
from aiogram.dispatcher import FSMContext
from states.states import StateGroup
from loader import dp, bot
from aiogram import types


async def messages_filter(message: types.Message):
    return 'Я завершил(а) задание !' in message.text


async def send_city_info(message: types.Message, city_name):
    photo = open(f"data/pictures/{city_name}.jpg", "rb")
    await message.answer_photo(photo=photo, caption=greece_cities_info[city_name],)
    photo.close()


@dp.message_handler(messages_filter, state=StateGroup.in_learning)
async def start_quiz(message: types.Message):
    await message.answer(text=learn_phase_start)
    await send_city_info(message, "arcadia")
    await send_city_info(message, "stimfal")
    await send_city_info(message, "lerna")
    await message.answer(additional_info, reply_markup=await finished_exercise())
