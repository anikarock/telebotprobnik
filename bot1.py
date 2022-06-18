import telebot

bot=telebot.TeleBot('5463824330:AAHjDwzicpWzqOlLRAZDkdaSTvBIYLnYlRY')

@bot.message_handler(commands=['start'])
def start (message):
    mess=f'Привет, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode='html')

@bot.message_handler(commands=['how_are_you'])
def how_are_you (message):
    photo= open('img/problem.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['are_you_smart'])
def are_you_smart (message):
    photo= open('img/gordost.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['scream'])
def scream (message):
    photo= open('img/neori.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['scold'])
def scold (message):
    photo= open('img/rastroistvo.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['sorry'])
def sorry (message):
    photo= open('img/fY05Mj_cR80.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['praise'])
def praise (message):
    photo= open('img/eZN9Wq67lss.jpeg','rb') 
    bot.send_photo(message.chat.id,photo)    

@bot.message_handler(content_types=['sticker'])
def sticker (message):
    bot.send_message(message.chat.id,'прикольно, давай еще')

@bot.message_handler()
def user_text (message):
    if message.text=='утро' or message.text=='Утро' :
        photo= open('img/dobroe utro.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='Ночь' or message.text=='ночь':
        photo= open('img/nadegda.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='люблю' or message.text=='Люблю':
        photo= open('img/cfkCPeMaUJk.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='Правда' or message.text=='правда':
        photo= open('img/npodozrenie.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='Ихний' or message.text=='ихний':
        photo= open('img/nedoumenie.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='еда' or message.text=='Еда':
        photo= open('img/gde.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)
     
    elif message.text=='их' or message.text=='Их':
        photo= open('img/bravo.jpeg','rb') 
        bot.send_photo(message.chat.id,photo) 
    
    elif message.text=='програмист' or message.text=='Програмист':
        photo= open('img/ponimanie.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    elif message.text=='пусто' or message.text=='Пусто':
        photo= open('img/vostorg.jpeg','rb') 
        bot.send_photo(message.chat.id,photo)

    else:
        photo= open('img/neponimanie.jpeg','rb')
        bot.send_photo(message.chat.id,photo)



bot.polling(none_stop=True)