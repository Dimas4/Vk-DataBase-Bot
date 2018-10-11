import time

from initialize.initialize_backend.initialize import initialize as init_backend
from initialize.initialize_db.initialize import initialize as init_db
from dialog.dialog import Dialog
from db.db import Db


def get_or_set(text):
    return [text.split(':')[1]] if '&' not in text else [text.split(':')[1].split('&')[0],
                                                         text.split(':')[1].split('&')[1]]


def start(token, backend, db):
    bot = init_backend(token, backend)
    path = db['path']
    del db['path']
    db_path = init_db(path, **db)
    db = Db(db_path)
    dialog = Dialog(db)

    print('Start')
    
    while True:

        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, message_id, body = bot.get_message_and_ids(messages)
            print('Запрос:', id, body)

            if body.lower() in dialog.text:
                bot.send_message(id, dialog.text[body.lower()])
                continue

            for key in dialog.action:
                if key in body.lower():
                    part = body.lower().split(':')[1].strip()
                    if '&' in body.lower():
                        splitted = part.split('&')
                        part_1, part_2 = splitted[0].strip(), splitted[1].strip()
                        db.hset(id, part_1, part_2)
                        bot.send_message(id, dialog.ok)
                        break

                    data = db.hget(id, part)
                    if data:
                        bot.send_message(id, data)
                    else:
                        bot.send_message(id, dialog.text_does_not_exist)
                    break

            else:
                bot.send_message(id, dialog.don_t_understand)

        time.sleep(1)
