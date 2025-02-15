import random
import telebot
import time
import threading

bot = telebot.TeleBot("7835884384:AAGhlRshyTR2Uyh28RQX5nYDhMskzePejk8")


books = [
    "Джим Рон, Сезоны жизни",
    "Чарльз Петцольд , Код",
    "Ник Вуйчич , Жизнь без границ",
    "Джон Кехо ,  Подсознание может всё",
    "Ричард Кох , Принцип 80/20",
    "Дойдж Норман , Пластичность мозга"
]

# Функция, которая отправляет напоминание
def send_reminder(chat_id):
    while True:
        # Выбираем случайную книгу из списка
        book = random.choice(books)
        # Отправляем сообщение
        bot.send_message(chat_id, f"Привет! Я чат бот, который будет напоминать, что нужно прочитать очередную нужную вам книгу: {book}")
        # Ждем 10 мин (600 секунд) перед следующим напоминанием
        time.sleep(600)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я чат бот, который будет напоминать, что нужно прочитать очередную нужную вам книгу.")
    # Запускаем поток для отправки напоминаний
    threading.Thread(target=send_reminder, args=(message.chat.id,)).start()

@bot.message_handler(commands=['fact'])
def fact(message):
    list = ["Факт 1: Книги могут улучшать вашу память и концентрацию.",
    "Факт 2: Чтение книг помогает развивать воображение и креативность.",
    "Факт 3: Исследования показывают, что чтение может снижать уровень стресса до 68%."]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Лови факт о книгах {random_fact}")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Приветственное сообщение и информация о боте.\n"
        "/help - Список доступных команд.\n"
        "/fact - Получить интересный факт о книгах.\n"  # Если у вас есть такая команда
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_message)


# Запускаем бота
bot.polling(none_stop=True)

