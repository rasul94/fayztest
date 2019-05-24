

import telebot


bot = telebot.TeleBot('622767171:AAHFB_dYl1I6SDBJ5hHO81WOkg9Yms6jV64')

bot.send_message(227754968, "sava")


@bot.message_handler(commands=['start'])
def hendle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Navbat olish / Tartib raqamim', 'Navbatdagi mijozlar soni' )
    user_markup.row('Navbatdan chiqish', 'Biz bilan bog`lanish')
    bot.send_message(message.from_user.id, "Bot ishga tushdi", reply_markup=user_markup)


@bot.message_handler(commands=['admin'])
def hendle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Bitta mijoz tayyor',)
    user_markup.row('navbatga mijoz qo`shish', 'Navbatdagi mijozlar soni' )
    user_markup.row('Sartoroshxona ochil', 'Sartoroshxona yopil')
    bot.send_message(sheff, "Bot ishga tushdi", reply_markup=user_markup)



@bot.message_handler(commands=['stop'])
def hendler_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove
    bot.send_message(message.from_user.id, "Ko`rishguncha", reply_markup=hide_markup)


members = []

sheff = 227754968


@bot.message_handler(content_types=['text'])
def hadle_text(message):
    if message.text == "Sartoroshxona yopil" and message.from_user.id == sheff:
        if len(members) != 0:
            return bot.send_message(message.from_user.id, "Navbatdagilar bo`lsa yopib bo`lmaydi")
        members.append(11)
        bot.send_message(message.from_user.id, "Yopildi")
    if message.text == "Sartoroshxona ochil" and message.from_user.id == sheff:
        if 11 not in members:
            return bot.send_message(message.from_user.id, "Sartoroshxona yopiq emas")
        members.remove(11)
        bot.send_message(message.from_user.id, "Oshildi")
    if 11 not in members:
        if message.text == "Navbat olish / Tartib raqamim":
            if message.from_user.id in members:
                return bot.send_message(message.from_user.id, f"Siz navbatdasiz. Navbat raqamingiz №: {members.index(message.from_user.id) + 1}")
            members.append(message.from_user.id)
            bot.send_message(message.from_user.id, "Siz navbatga yozildingiz. Tartib raqamingiz №: {}".format((members.index(message.from_user.id) + 1)))
            bot.send_message(sheff, f"{members.index(message.from_user.id) + 1}- raqamli ismi:{message.chat.first_name} mijoz qo`shildi")
            if len(members) == 1:
                bot.send_message(message.from_user.id, "Eslatma!!! Navbatda mijoz yo`qligi sababli 5-10 daqiqada yetib kelmasangiz, navbatdan chiqarilasiz")
            if len(members) == 2:
                bot.send_message(message.from_user.id, "SARTOROSHXONAGA YETIB KELISHINGIZNI SO`RAYMIZ")
                bot.send_message(message.from_user.id, "Sizdan avvalgi 1 - qaqamli mijozga xizmat ko`rsatilgungacha kelmasangiz navbatdan o`chirilasiz")
        if message.text == 'Navbatdagi mijozlar soni':
            if len(members) == 0:
                return bot.send_message(message.from_user.id, "Hozirda navbatda hech kim yo`q")
            bot.send_message(message.from_user.id, "{} ta mijoz navbatda kutyapti".format(len(members)))
        if message.text == 'Navbatdan chiqish':
            if message.from_user.id not in members:
                return bot.send_message(message.from_user.id, "Navbatga yozilmagansiz")
            bot.send_message(sheff, f"Navbatdan chiqdi  {members.index(message.from_user.id) + 1}-raqaml imijoz ismi-{message.chat.first_name}  ")
            bot.send_message(message.from_user.id, "Siz navbatdan o`chirildingiz".format(members.remove(message.from_user.id)))
            #bot.send_message(members, "navbat kutayotgan mijoz chiqib ketti")
        if message.text == 'Biz bilan bog`lanish':
            bot.send_message(message.from_user.id, "Fayzullo +998903033677")
            bot.send_location(message.from_user.id, 40.440721, 71.712663)
        if message.text == 'navbatga mijoz qo`shish' and message.from_user.id == sheff:
            members.append(1)
            bot.send_message(sheff, "mijoz navbat oxiriga qo`shildi.")
            bot.send_message(sheff, f"Navbatda {len(members)} ta mijoz bor.")
        if message.text == 'Bitta mijoz tayyor' and message.from_user.id == sheff:
            if len(members) == 0:
                return bot.send_message(sheff, "mijoz yo`q")
            if members[0] != 1:
                bot.send_message(members[0], " Sizga xizmat ko`rsatildi va navbatdan chiqarildingiz ")
            members.pop(0)
            bot.send_message(sheff, "Mijozga xizmat \u2611 ko`rsatildi.")
            bot.send_message(sheff, f"Navbatda {len(members)} ta mijoz qoldi.")
            if len(members) >= 2 and 1 == members.index(members[1]) and members[1] != 1:
                bot.send_message(members[1], "Hurmatli mijoz  SARTOROSHXONAGA YETIB KELISHINGIZNI SO`RAYMIZ.")
                bot.send_message(members[1], "Sizdan avvalgi 1 - qaqamli mijozga xizmat ko`rsatilgungacha kelmasangiz navbatdan o`chirilasiz.")
                bot.send_message(members[1], f"Navbat raqamingiz №{len(members)}")
    else:
        bot.send_message(message.from_user.id, "Sartoroshxona hozirda berk")

        #if message.text != 'Navbatga turish' and 'Navbatdan chiqish' 'Navbatdagi mijozlar soni' 'Biz bilan bog`lanish':
        #bot.send_message(message.from_user.id, "Sizni tushunmadim. taqdim etilgan variantlardan foydalaning")






bot.polling(none_stop=True, interval=0)