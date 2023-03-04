import eel
import vk_api
from config import token


@eel.expose
def add_token(tken):
    my_file = open("config.py", "w+")
    my_file.write(f"token='{tken}'")
    my_file.close()


session = vk_api.VkApi(token='')


@eel.expose
def send_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0})
    print("Сообщение отправлено")


eel.init("interface")
eel.start("main.html", size=(425, 700))
