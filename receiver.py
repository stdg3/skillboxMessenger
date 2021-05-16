import requests
import time
from datetime import datetime

# messages = [
#     {
#         'name': 'Jack',
#         'text': 'Hello',
#         'time': time.time()
#     },
#     {
#         'name': 'Mary',
#         'text': 'Jack',
#         'time': time.time()
#     },
# ]

def print_message(mess):
    dt = datetime.fromtimestamp(_["time"])
    print(dt.strftime("%H:%M:%S"), _["name"],)
    print(_["text"])
    print()


after = 0

while True:
    response = requests.get(
        "http://c6ff98effef0.ngrok.io/messages", 
        params={"after": after}
        )
    
    # у гет апросов не бывает тела запроса как в пост, 
    # чтобы передать параметры в url ставится ? и имяПеременной = 0 например --> фласк отбросит вопр знак и создааст словарь из переменных, след перм через амперсант 
    # пример: http://127.0.0.1:5000/messages?after=0&abc=0 --> format name = url encodding
    # или можно использовать params
    #("http://127.0.0.1:5000/messages", params={"after": 0, })

    messages = response.json()["messages"]

    # [{"name": "123", ...}, ...]

    if messages:
        for _ in messages:
            # print(_["name"], ">>", _["text"])
            print_message(_)
        after = messages[-1]["time"]
        # mesajlar gelirken yalnızca son mesajın time parametresine göre sondan güncellensin
    time.sleep(1)



