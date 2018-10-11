import vk_api


def generate_instance(token):
    vk = vk_api.VkApi(token=token)
    vk_upload = vk_api.VkUpload(vk=vk)
    vk._auth_token()
    return vk, vk_upload
