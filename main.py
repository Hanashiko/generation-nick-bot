import config
import logging
import random
import nicks

from random import randrange, choice
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт!\nМене звати GeneratorNickBot\nМожеш переглянути інформацію про мне, використавши команду /info \nЯкщо бажаєш згенерувати нікнейм напиши /randomnick \n(якщо що, в мене є скорочення команд: /randomnick -> /randnick -> /nick ; /randomname -> /randname -> /name ; /randomgtanick -> /randgtanick -> /gtanick ")

@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply("Меня зовут: GeneratorNicks\nМой ник: GeneratorNickBot\nДля чего я был создан: для генерации ника\nМой айди: 1934951930\nМой создатель: Белый обама\nМоя нынешняя версия: 0.0.2")



@dp.message_handler(commands=['randname','randomname','name'])
async def cmd_mn(message: types.Message):
    rname = choice(nicks.names)
    await message.reply(f'Ви зарандомили випадкове ім\'я, і вам випало:\n{rname}')

@dp.message_handler(commands=['randnick','randomnick','nick'])
async def cmd_gn(message: types.Message):
    rnick = choice(nicks.nicks)
    await message.reply(f'Ви зарандомили випадковий нікнейм, і вам випало:\n{rnick}')

@dp.message_handler(commands=['randgtanick','randomgtanick','gtanick'])
async def cmd_gn(message: types.Message):
    rgtanick = choice(nicks.gtanicks)
    await message.reply(f'Ви зарандомили випадковий нік, для GTA SAMP, і вам випало:\n{rgtanick}')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
