def send_email(message, recepient, *, sender="university.help@gmail.com"):
    # проверка корректности адресов
    if '@' not in recepient or '@' not in sender \
        or not sender.endswith((".com", ".ru",".net")) \
        or not recepient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса, {sender} на адрес, {recepient}.")
    elif recepient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
      # нет ошибок, отправка письма
      if sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса, {sender} на адрес, {recepient}.")
      else:
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recepient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
