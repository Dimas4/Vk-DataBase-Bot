import json
import requests

from backend.generate_vk_instance.generate_instance import generate_instance


class VkBot:
    def __init__(self, token):
        self.token = token
        self.vk = generate_instance(token)

    def get_unread_messages(self, offset=0, count=20):
        return self.vk.method("messages.getConversations", {"offset": offset, "count": count, "filter": "unread"})

    def send_message(self, id, message=None, attach=None):
        attach = 'doc%s_%s' % (attach['owner_id'], attach['id']) if attach else None
        data = {"peer_id": id, "message": message, 'attachment': attach}
        self.vk.method("messages.send", data)

    @staticmethod
    def get_message_and_ids(messages):
        return messages["items"][0]["last_message"]["from_id"], \
               messages["items"][0]["last_message"]["id"], \
               messages["items"][0]["last_message"]["text"]

    def upload_file(self, path, id):
        audio = {'file': (path, open(path, 'rb'))}
        upload_url = self.vk.method('docs.getMessagesUploadServer',
                                    {'type': 'audio_message', 'peer_id': id})['upload_url']
        upload = requests.post(upload_url, files=audio)
        result = json.loads(upload.text)['file']
        saved = self.vk.method('docs.save', {'file': result, 'title': 'ssasad.ogg'})[0]
        return saved

    def mark_as_read(self, id):
        self.vk.method("messages.markAsRead", {"message_ids": id})
