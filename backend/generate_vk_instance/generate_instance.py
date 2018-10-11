import vk_api


def generate_instance(token):
    vk = vk_api.VkApi(token=token)
    vk._auth_token()
    return vk
