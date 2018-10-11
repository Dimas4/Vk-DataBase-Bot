import json
import requests

from backend.generate_vk_instance.generate_instance import generate_instance


class VkBot:
    def __init__(self, token):
        self.token = token
        self.vk, self.vk_upload = generate_instance(token)

    def get_unread_messages(self, offset=0, count=20):
        return self.vk.method("messages.getConversations", {"offset": offset, "count": count, "filter": "unread"})

    def send_message(self, id, message=None, attach=None):
        attach = 'doc%s_%s' % (attach['owner_id'], attach['id']) if attach else None
        data = {"peer_id": id, "message": message, 'attachment': attach}
        self.vk.method("messages.send", data)

    def upload_image(self, id, filename):
        res = self.vk_upload.photo_messages(filename)[0]
        owner_id = res["owner_id"]
        photo_id = res["id"]
        self.vk.method("messages.send", {
            "peer_id": id,
            "attachment": f"photo{owner_id}_{photo_id}"
        })
    
    @staticmethod
    def get_message_ids_image(messages):
        file = messages["items"][0]["last_message"]['attachments']
        url = None
        if file:
            url = file[0]['photo']['sizes'][2]['url']
        return messages["items"][0]["last_message"]["from_id"], \
               messages["items"][0]["last_message"]["id"], \
               messages["items"][0]["last_message"]["text"], url

