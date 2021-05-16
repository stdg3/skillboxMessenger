# """
#     в этом методе sender.py отправляются http запросы 
# önemlli olan belirtilen url de send motodun flsk.py da tanımlanmış olması
# """


# get --> запрос инфы
# post --> отправка инфы 
import requests
# pip requests --> look at the meth <)
name = input("your name: ")
# text = input("your message")
while True:
    
    data = {
        "name": name,
        "text": input(">>> "),
    }

    # requests.post datayı url da json olarak sıkıştırıp atıyor
    # server kısmında flsk.py da send metodunda data=request.json dediğimizde de onu geri okunabilir hale getiriyor
    response = requests.post(
        "http://c6ff98effef0.ngrok.io/send",
        json =data,
    )


# print(response) # response kodu döndürür 200 = ok, 400 client hatası, 500 server
# print(response.headers)

# print(response.text) # текст сообщения --> normalde açıktı ama view da send method post yaptığı için ve default olarak return ifadesi barındırmak zorunda olduğundan flsk.py da ordan boş liste dönüyor, onu görmek istersen comment satırı aç
