import telebot

# ضع التوكن من BotFather
TOKEN = "8249571512:AAGprc1cEIRxZaPNYPhT0cjAI8vlqXx2Jjg"
bot = telebot.TeleBot(TOKEN)

# أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = """🤖 أهلاً بك في البوت!

الأوامر المتاحة:
/start - بدء البوت
/help - المساعدة
/about - معلومات عن المطور
"""
    bot.reply_to(message, text)

# أمر /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """🆘 المساعدة:

- أرسل أي كلمة وسيقوم البوت بتكرارها لك.
- استخدم /about لمعلومات المطور.
"""
    bot.reply_to(message, help_text)

# أمر /about
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """👨‍💻 مطور البوت:
Hasneen Al Ali 🇮🇶

📩 للتواصل: @PY_87
📢 القناة: @llxxx3
"""
    bot.reply_to(message, about_text)

# أي رسالة عادية ➝ يكررها
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"📨 أنت كتبت: {message.text}")

# تشغيل البوت
if __name__ == "__main__":
    bot.infinity_polling()
