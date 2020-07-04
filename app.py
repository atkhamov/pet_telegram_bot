import requests

API_LINK = "https://api.telegram.org/bot1329322309:AAFrItMRWlKd1Y5In4VTinuGXSLzC1qF7tk"

updates = requests.get(API_LINK + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]

text = message["text"]

sent_message = requests.get(API_LINK + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")


# import requests
#
# url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/direct/"
#
# querystring = {"destination":"LED","origin":"MOW"}
#
# headers = {
#     'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
#     'x-rapidapi-key': "SIGN-UP-FOR-KEY"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)