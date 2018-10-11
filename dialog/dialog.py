class Dialog:
    def __init__(self, backend):
        self.backend = backend
        self.text = {
                        "привет": "Привет! Я бот-база данных! Ты можешь присылать мне текст и ключ к этому тексту. Я сохраню это у "
                                  "себя и потом по твой просьбе верну тебе текст по ключу!",
                        "спасибо": "Всегда пожалуйста!"
                    }
        self.don_t_understand = "Не понимаю тебя"
        self.action = {
                        "сохрани": backend.hset,
                        "дай": backend.hget
                      }
        self.ok = 'Хорошо'
        self.text_does_not_exist = 'Такой записи не сущетсвует'
