from django.core.management.base import BaseCommand

from aiogram import types, executor, Bot, Dispatcher
from aiogram.types.web_app_info import WebAppInfo
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
import requests
import pprint


class Command(BaseCommand):
    help = 'Telegram-BOT'
    
    def handle(self, *args, **options):

        TG_TOKEN = '6158625955:AAFIe2aRl-nfe0HugQ5IUyRspt-ecz_XPSI'
        PLAN_FIX = '4a0364798374b2d52c84177b32e56077'
        bot = Bot(TG_TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(bot, storage=storage)


        # СТАРТ
        @dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            mes_id = message['from']['id']
            url='https://lyhatik.github.io/_plan_fix/booking.html'
            rbt_booking = types.KeyboardButton(
                'Booking',
                web_app=WebAppInfo(
                    url=url
                    )
                )
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(rbt_booking)

            await bot.send_message(
                chat_id=mes_id,
                text=f'Привет!',
                reply_markup=keyboard
                )


        # Перехватывает контекст с web_app
        @dp.message_handler(content_types=['web_app_data'])
        async def web_app(message: types.Message):
            print('данные тг получены')
            # Собираем данные с web_app
            res = json.loads(message.web_app_data.data)
            from_mes = message['from']
            user_id = from_mes['id']
            res['user_id'] = user_id
            #await get_ts()
            await save_booking(res)
            
            
        # Отправляет POST запрос в planfix
        async def save_booking(data):
            return


        executor.start_polling(dp)
