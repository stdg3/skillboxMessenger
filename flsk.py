from flask import Flask, request, abort
import time
from pprint import pprint

# author Никита Левашов 

from datetime import datetime

app = Flask(__name__)

db = [
    {
        'name': 'Jack',
        'text': 'Hello',
        'time': 0.1 # time.time()
    },
    {
        'name': 'Mary',
        'text': 'Jack',
        'time': 0.2 # time.time()
    },
]

@app.route("/")
def hello():
    return 'Hello, World!'

@app.route("/status")
def status():
    # return de dict göndersek flask kendisi http respnse tan otomatik olarak json hal alacak
    # return jsonify(
    #     status = True,
    #     name = "sbox_mes",
    #     time = str(time.ctime())
    # )

    # import json
    # json.dumps({ "key": "val"}) --> satır haline çeviriyor
    
    # return {
    #     "status": True,
    #     "name": "messagebox",
    #     "time": time.ctime(),
    #     "time_unix_time_stamp": time.time(),
    #     "time_gm": time.gmtime(),
    #     "time_asc": time.asctime(),
    #     "date": str(datetime.now()),
    #     "date2": datetime.now().strftime("%Y/%m/%d %H:%M"),
    # }
    t_usrs = []
    t_msgs_counter = 0

    if db:
        for msg in db:
            # for key in msg:
            t_msgs_counter += 1
            if msg["name"] not in t_usrs:
                t_usrs.append(msg["name"])

    res = "users: " + str(len(t_usrs)) + " messages: "+ str(t_msgs_counter) 
    return res



@app.route("/send", methods=["POST"])
# /send view'da yalnızca geçerli olan methods=["POST"] aktiftir, getler ezilir
def send():
    
    # request flask.request'tan çekildi, requestS paketiyle karıştırma
    # posttan gelen cevap requestin içine aktarılır

    data = request.json

    if not isinstance(data, dict):
        return abort(400) # --> 400 hatasını döndür
    if "name" not in data or "text" not in data:
        return abort(400)
    
    name = data["name"]
    text = data["text"]

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not (0 < len(name) <= 64):
        return abort(400)
    if not (0 < len(text) <= 10000):
        return abort(400)

    print(data["name"], data["text"])
    
    db.append({
        'name': data["name"],
        'text': data["text"],
        'time': time.time()
    })
    # pprint(db) # debug вывод

    # yukarıdaki print kodunn bile çalışabilmesi için return boş ta olsa bişi dödürmeli,
    # burada json türü dict gönderdik
    return {} 


@app.route("/messages")
def messages():
    # print(request.args["after"]) # type --> str çünkü /messages?after=0 şeklinde парсируемая строка içerdeki val type ler bilinmediğinden patlamasın diye str şeklinde atıyor deff olrk
    try:
        after = float(request.args["after"])
    except:
        return abort(400)

    filtered_messages = []

    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)

    return {"messages": filtered_messages[:50]}


app.run()
