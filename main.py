import telebot
from telebot import types
from random import randint 
import time


TOKEN = '5340444590:AAEyrVhN0Kmkkwb2xdh7qlufqx4RpPWIqVM'

bot = telebot.TeleBot(TOKEN)

rand = {"a":0} 
rand["a"] = randint(1,100)

def son(kluch): 
    if (kluch): 
        rand["a"] = randint(1,100)
        return rand["a"]
    else:
        return rand["a"]
start = {"start": True}
count = {"count": 6}
def game (messages): 
    for m in messages:
        markup = types.ReplyKeyboardMarkup()  
        markup.add('o\'yini boshlash')  
        chatId = m.chat.id
        text = m.text
        if text == '/start'or text == 'o\'yini boshlash':
            son(True)
            count["count"] = 6
            start["start"] = True
            bot.send_message(chatId, 'Son o`yladim toping',reply_markup=markup)
        elif (text.isnumeric() == False):
            bot.send_message(chatId, "Faqat raqam kiriting iltimos")
        elif( int(text) == int(son(False)) and count["count"] > 0 and start["start"]):
            print('teng')
            bot.send_message(chatId, 'Tabriklaymiz to`g`ri topdiz',reply_markup=markup)
            start["start"] = False 
            count["count"] = 6
        elif ( int(text) < int(son(False)) and count["count"] > 0 and start["start"]): 
            print('katta')
            count["count"] = count["count"] - 1
            bot.send_message(chatId, "Men o'ylagan son "+text+" dan katta sizda "+str(count["count"])+" ta urinish qoldi",reply_markup=markup)
        elif ( int(text) > int(son(False)) and count["count"] > 0 and start["start"]):
            count["count"] = count["count"] - 1
            print('kichik')
            bot.send_message(chatId, "Men o'ylagan son "+text+" dan kichik sizda "+str(count["count"])+' ta urinish qoldi', reply_markup=markup)
        elif start["start"] == False: 
            bot.send_message(chatId, "o`yin tugadi")
        else:
            start["start"] = False   
            print('urinish')
            bot.send_message(chatId, "Sizda urinishlar qolmadi yangi o`yin boshlang", reply_markup=markup)  
       

bot.set_update_listener(game)

# bot.polling()
bot.polling(none_stop=True) 