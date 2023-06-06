# -*- coding: utf-8 -*-
import telebot
import PIL
from telebot import types
from PIL import Image
Image


bot = telebot.TeleBot("6133847062:AAGbjK-paipNHgdU7q0aq-xYQs4AbL9kEL0")


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🍄Fly agaric🍄")
    btn2 = types.KeyboardButton("🌈Magic mushrooms✨")
    btn3 = types.KeyboardButton("🪬Rape🗿")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                     "Добро пожаловать👋", reply_markup=markup)


@bot.message_handler(content_types=['text', 'photo'])
def get_text_messages(message):

    if message.text == "🍄Fly agaric🍄":
        markup = types.InlineKeyboardButton(
            resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Using👨‍🍳")
        btn2 = types.InlineKeyboardButton("Effects📜")
        btn3 = types.InlineKeyboardButton("Product🍄")
        markup.add(btn1, btn2, btn3)
        img = open('photo-output 2.JPG', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id,
                         "Используй их разумно", reply_markup=markup)

    elif message.text == "Using👨‍🍳":
        bot.send_message(message.from_user.id, "Чтобы получить всю пользу для физического и психического здоровья, мухомор сушёный принимается от 0,6 до 3 граммов в сутки. Утром для бодрости и ясности мышления, работоспособности на целый день, вечером для крепкого и глубокого сна.\n\nP.S.  Мухомор рекомендуется употреблять перед едой, так как его всасывание происходит значительно быстрее чем после вкусного и сытого приема пищи.\n\n\nДобавки, усиливающие действие мухомора:\n\n- Лимон -  За счет повышения кислотности повышает лечебные свойства мухомора, а также увеличивает его биодоступность.\n\n- Шоколад -  Усиливает действие грибов. Дорогие быстрые углеводы (сахар и т.п.) выступают в роли транспортной молекулы. За счет быстрых углеводов мусцимол быстрее всасывается в организмом.\n\n- Мед -  Те же быстрые углеводы. Полностью перебивает вкус. Полезно тем кто любит жевать грибы, но не любит их вкус.\n\n- Зверобой -  ингибитор МАО. Усилит эффект, усиление прямо пропорционально количеству зверобоя. Можно заварить вместе с грибами, типа как чай.\n\n- Мелатонин(таблетки) -  Мелатонин вместе с мухомором употребляется для облегчения стрессовых реакций и депрессивных состояний, а также для улучшения сна. Употребляется сугубо перед сном.\n\n\nP.S.S.  Если вы решили принять более 2-3 грамм мухомора за один раз, то возможна тошнота и может клонить в сон, для нивелирования данных побочных эффектов необходимо заваривать мухомор так как обычный чай, температура кипятка не должна превышать 80 с°.")

    elif message.text == "Effects📜":
        bot.send_message(message.from_user.id, "Основные эффекты от микродозинга сушёного мухомора:\n- Тонизирует организм, прилив сил, уверенности.\n- Обеспечивает оптимальную работу всех органов в организме.\n- Обладает антимикробными свойствами.\n- Повышается сила и выносливость.\n- Природные болеутоляющие свойства.\n- Профилактика вирусных и бактериальных заболеваний.\n- Волна радости и эйфории, желание действовать, творить, общаться и развиваться.\n- Снятие симптомов депрессии и беспокойства.\n- Значительное улучшение социальных навыков.\n- Самоанализ и чувство внутренней ясности.\n- Помогает избавиться от вредных привычек.\n- После 1-2 недель приема нормализуется сон, становится крепким и глубоким")

    elif message.text == "Product🍄":
        markupProd = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnProd1 = types.KeyboardButton("Offerings🤝")
        btnProd2 = types.KeyboardButton("Back🔙")
        markupProd.add(btnProd1, btnProd2)
        img = open('photo-output.JPG', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id, "Его Величество Мухомор «Amanita Muscaria» - врач и учитель. Знакомство с ним не оставляет равнодушным никого. Как сказал один известный человек-если ты встал на этот путь, то дороги назад нет. И это правда. Гриб изменяет как состояние физического скафандра, так и сущность человека. О лечебных свойствах гриба написать много, не буду углубляться в это. Если ты намерен познакомиться с Мухомором – наверняка ты знаешь о его волшебных и лечебных свойствах.\n\nP.S.  Грибы сушатся в электросушилке при температуре 40-45 градусов. Сушим только шляпки красного Мухомора🍄(без ножек). Предварительно перед сушкой грибы очищаются от песка и грязи.", reply_markup=markupProd)

    elif message.text == "Offerings🤝":
        bot.send_message(message.from_user.id,
                         "Тест")

    elif message.text == "Back🔙":
        bot.send_message(message.from_user.id,
                         "Эта функция ещё не доступна", reply_markup=markup)

    elif message.text == "🌈Magic mushrooms✨":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnMag1 = types.KeyboardButton("Microdosing💊")
        btnMag2 = types.KeyboardButton("Shrooming🤪👽👻")
        markup1.add(btnMag1, btnMag2)
        img = open('2023-06-02 17.53.16.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id,
                         "Этот раздел пуст", reply_markup=markup1)

    elif message.text == "Shrooming🤪👽👻":
        markupShroom = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnShroom1 = types.KeyboardButton("👨‍🍳Using👨‍🍳")
        btnShroom2 = types.KeyboardButton("📜Effects📜")
        btnShroom3 = types.KeyboardButton("🍄Product🍄")
        markupShroom.add(btnShroom1, btnShroom2, btnShroom3)
        bot.send_message(message.chat.id, "Хорошего путешествия",
                         reply_markup=markupShroom)

    elif message.text == "👨‍🍳Using👨‍🍳":
        bot.send_message(message.from_user.id, "Описания")

    elif message.text == "📜Effects📜":
        bot.send_message(message.from_user.id, "Описания")

    elif message.text == "🍄Product🍄":
        bot.send_message(message.from_user.id, "Фото")

    elif message.text == "🪬Rape🗿":
        markupRape = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnRape = types.KeyboardButton("info")
        btnRape = types.KeyboardButton("product")
        bot.send_message(message.from_user.id,
                         "Этот раздел пуст")


bot.polling(none_stop=True, interval=0)
