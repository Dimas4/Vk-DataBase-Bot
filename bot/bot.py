import time
import urllib.request

from initialize.initialize_backend.initialize import initialize as init_backend
from initialize.initialize_db.initialize import initialize as init_db
from dialog.dialog import Dialog
from db.db import Db


def start(token, backend, db, dialog, filename):
    bot = init_backend(token, backend)
    path = db['path']
    del db['path']
    db_path = init_db(path, **db)
    db = Db(db_path)
    dialog = Dialog(db, dialog)

    print('Start')
    
    while True:
        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, message_id, body, url = bot.get_message_ids_image(messages)
            print('Запрос:', id, body)
            try:

                if url and url[-3:] == 'jpg':
                    urllib.request.urlretrieve(url, filename)
                    db.save_image(id, body, filename)
                    bot.send_message(id, dialog.ok)
                    continue

                if body.lower() in dialog.common_answer:
                    bot.send_message(id, dialog.common_answer[body.lower()])
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

                        if data and len(data) > 15000:
                            with open(filename, 'wb') as file:
                                file.write(data)
                            bot.upload_image(id, filename)
                            break
                        elif data:
                            bot.send_message(id, data)
                        else:
                            bot.send_message(id, dialog.text_does_not_exist)
                        break
                else:
                    bot.send_message(id, dialog.don_t_understand)
            except Exception as e:
                print(str(e))
                bot.send_message(id, dialog.error)
            
        time.sleep(1)
