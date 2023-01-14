import telebot  
from telebot import types

data = {}  
token = "5817112218:AAEIttPrN4uvarOgQi9tqrYxz0tOu5vVQZ0" 
bot = telebot.TeleBot(token=token)
x = 0
#commands=["start"] - чтобы работало только от команды старт  
@bot.message_handler(commands=["start"])
def start(message):
    #глобальная переменная, где сохранятеся статус для отдельного пользователя
    global data
    data.update({
       message.chat.id : {
            "status": x,
        }
    })
    #Создаем клавиатуру  
    keyboard = types.InlineKeyboardMarkup()  
    #Текст + фото 
    bot.send_message(message.chat.id, text="«Они сказали, что я бедная. Они сказали, что я недостойна учиться тут.»" )
    bot.send_message(message.chat.id, text="Эти мысли крутились у меня в голове. Уже не помню, как пришла сюда. По моим щекам катятся слезы боли.")
    bot.send_message(message.chat.id, text="«Почему я не такая, как они?» ")
    bot.send_message(message.chat.id, text="Место у мусорного бака выглядело неприятно и мерзко, но меня это не остановило. Из туалета слышались тяжелые всхлипы, которые протяжно разносились по коридору.")
    bot.send_photo(message.chat.id, "https://ibb.co/WDNw9bq", caption="«Зачем я нахожусь здесь?» Снова злосчастный звонок трезвонит по ушам. Когда эта ненавистная мелодия начинает звучать, то тревога наполняет моё тело. Даже сейчас мне становится страшно. Я начинаю слышать свое дыхание, контролировать его, зацикливаться на нем. Раз за разом. Начинаю задыхаться. «Я прямо сейчас упаду».")
    bot.send_message(message.chat.id, text="Но тут кто-то зашел. Не могу сказать точно, сколько их было. Казалось, что целая толпа зашла в одно маленькое помещение. Они смеялись и хохотали, но потом услышали меня.")
    bot.send_photo(message.chat.id,"https://ibb.co/HFLbwwJ", caption="Дверь тихонько приоткрылась. Передо мной стоит миленькая миниатюрная девушка, на фоне которой мелькает еще пару человек.")
    bot.send_message(message.chat.id, text=" -Хей!!! Как тебя зовут?\n-Ли-Лиза….. - робко ответила я, всхлипывая.\n-Что с тобой случилось, солнышко? Не волнуйся, я никому не расскажу! \n «Что же ответить?» ")
    #Добавляем кнопки  
    button1 = types.InlineKeyboardButton(text="Проигнорировать", callback_data="button1")  
    button2 = types.InlineKeyboardButton(text="Излить душу", callback_data="button2")  
    keyboard.add(button1)  
    keyboard.add(button2)  
    bot.send_message(message.chat.id, "Сделайте свой выбор", reply_markup=keyboard)
#Добавляем и изменяем текст после нажатия на определенную кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback(call):  
    if call.message:
        data[call.message.chat.id]["status"] = data[call.message.chat.id]["status"] + 1
        print(data) 
        if call.data == "button1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Проигнорировать*", parse_mode = "MarkdownV2")
            bot.send_photo(call.message.chat.id, "https://ibb.co/1zxfSwf",caption="Девушка фыркает в ответ.")
            bot.send_photo(call.message.chat.id, "https://ibb.co/KDjQHyD", caption="Она недовольна, что кто-то посмел так грубо отреагировать на её любезнейший вопрос. Но всё-таки школьница и её свита уходят отсюда.")
            bot.send_message(call.message.chat.id, text="Совет: Не стоит доверять людям, что находятся в близких отношениях с теми, кто вредил вам и говорил о вас плохо. Если Вам действительно некому излить душу и кажется, что этот человек — ваша последняя надежда, вам стоит попросить его поговорить с вами наедине, в удобное вам время, если он действительно хочет вам помочь, он согласиться. Будьте внимательны к людям и раскрывайтесь полностью лишь тем, кому доверяете.")
        if call.data == "button2":
        
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Излить душу*", parse_mode = "MarkdownV2")  
            bot.send_photo(call.message.chat.id, "https://ibb.co/4YC3V2m" ,caption="— Ой, правда? Быть не может, что с тобой это действительно произошло! Ты же такая хорошая, красивая и милая, правда-правда не заслуживаешь это, милая... \n ... А ещё случилось что? расскажешь?")
            bot.send_photo(call.message.chat.id, "https://ibb.co/mCMg86d", "Ха-ха, тебя так забавно слушать! Поверь, скоро на стенах этого туалета появятся надписи со всеми твоими фразами, все узнают, какая ты жалкая, бедняжка, за синячки под глазами оскорбили, ну не плачь, не плачь... \n Девочки, вы же слышали, что она сказала? Ваши слова ее задели до глубины души... Ну вам разве не жаль ее?")
            bot.send_message(call.message.chat.id, text="Совет: Не стоит доверять людям, что находятся в близких отношениях с теми, кто вредил вам и говорил о вас плохо. Если Вам действительно некому излить душу и кажется, что этот человек — ваша последняя надежда, вам стоит попросить его поговорить с вами наедине, в удобное вам время, если он действительно хочет вам помочь, он согласиться. Будьте внимательны к людям и раскрывайтесь полностью лишь тем, кому доверяете.")       
# поллинг - вечныq цикл с обновлением входящих сообщений  
bot.polling()
