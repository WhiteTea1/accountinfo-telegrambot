import telebot

token = '6103819013:AAGQbE6T3MCnhk5-kt3d4qAhs_s2Qw_SaNI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):
    first_name = f'First name - {message.from_user.first_name}'
    last_Name = f'Last name - {message.from_user.last_name}'
    username = f'UserName - {message.from_user.username}'
    premium = f'Telegram Premium  - {message.from_user.is_premium}'
    id = f'ID - {message.from_user.id}'
    bot.send_message(message.chat.id, 'Привет! Данный бот помогает узнать информация о твоём аккаунта.', parse_mode='html')
    bot.send_message(message.chat.id, f'{first_name}\n {last_Name}\n {username}\n {id}\n {premium}', parse_mode='html')
bot.polling(none_stop=True)