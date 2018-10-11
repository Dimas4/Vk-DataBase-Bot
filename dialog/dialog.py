class Dialog:
    def __init__(self, backend, dialog):
        self.backend = backend
        self.common_answer = dialog['common_answer']
        self.don_t_understand = dialog['don_t_understand']
        self.action = dialog['action']
        self.ok = dialog['ok']
        self.text_does_not_exist = dialog['text_does_not_exist']
        self.error = dialog['error']
