import vk
import facebook

print("Резмещение текста на странице vk.com")
id_app=input("Введите id:")
login=input("Введите номер телефона(в формате +79991112233):")
password=input("Введите пароль:")

s=input("Введите текст:")
if len(s)>140:
    s=s[0:140]

try:
    session=vk.AuthSession(id_app, login, password, scope='wall')
    vk_API=vk.API(session)
    vk_API.wall.post(message=s)
    print("Успешно.")
except:
    print("Что-то пошло не так. Сообщение не опубликовано.")

print("Резмещение текста на странице facebook.com")
your_token=input("Введите token:")

try:
    graph=facebook.GraphAPI(access_token=your_token,version="2.12")
    graph.put_object(parent_object='me',connection_name='feed',message=s)
    print("Успешно.")
except:
    print("Что-то пошло не так. Сообщение не опубликовано.")
