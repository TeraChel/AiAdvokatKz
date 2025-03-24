from aiogram import F, Router #F - filter
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.generators import gpt4

router = Router()

class Register(StatesGroup):
    sex = State()
    age = State()
    social_status = State()

class AskingQuestion(StatesGroup):
    info = State()
    question = State()

class Generate(StatesGroup):
    text = State()


@router.message(CommandStart()) #обработчик /start
async def cmd_start(message: Message, state: FSMContext): #создание переменной message с типом Message (import aiogram.types)
    await message.answer('Вас приветствует ваш личный ИИ помощник!',) #простое сообщение
    await state.set_state(Register.sex)
    await message.answer('Введите ваше пол:', reply_markup=kb.sex)


@router.message(Register.sex)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(sex = message.text)
    await state.set_state(Register.social_status)
    await message.answer('Выберите ваш социальный статус:', reply_markup=kb.social_status)

# @router.callback_query(F.data == 't-shirt')
# async def t_shirt(callback_query: CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.answer('Вы выбрали футболки:')

@router.message(Register.social_status)
async def register_social_status(message: Message, state: FSMContext):
    await state.update_data(social_status = message.text)
    await message.answer('Введите ваш возраст:')
    await state.set_state(Register.age)

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    data = await state.get_data()
    await message.answer(f'{data["sex"]} в возрасте {data["age"]} Относится к группе: {data["social_status"]}')
    await message.answer('Задайте вопрос связанный с законом...')
    await state.set_state(AskingQuestion.question)


@router.message(AskingQuestion.question)
async def asking_question_question(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(info=f'{data["sex"]} в возрасте {data["age"]} Относится к группе: {data["social_status"]}')
    await state.update_data(question = message.text)
    await message.answer('Идёт генерация ответа...')
    data = await state.get_data()
    response = await gpt4(f'{data["info"]} обращается по вопросу: {data["question"]}')
    await message.answer(response.choices[0].message.content)
    await message.answer('Надеемся что вам помог данный ответ!')
    await state.clear()
