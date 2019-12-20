import requests
from decouple import config 

token = config('TELEGRAM_BOT_TOKEN')
app_url = f"https://api.telegram.org/bot{token}"
chat_id = config('CHAT_ID')
#update_url = app_url + "/getUpdates"
#response = requests.get(update_url).json()
#print(response)
#chat_id = response["result"][0]["message"]["chat"]["id"]

text ="곧 점심시간!!!"

message_url = app_url + f"/sendMessage?chat_id={chat_id}&text={text}"

requests.get(message_url)

