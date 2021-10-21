import requests
from bs4 import BeautifulSoup
page = requests.post("https://hub.rgukt.ac.in/hub/notice/index",verify=False)
soup = BeautifulSoup(page.content,"html.parser")
html = list(soup.children)[3]
body = html.body
section = body.find("section",class_="content")
div_collapse = section.find_all("div",class_="collapse")
id_one = int([hid["id"] for hid in div_collapse][0])
print(id_one)
while True:
    try:
        page = requests.post("https://hub.rgukt.ac.in/hub/notice/index",verify=False)
        soup = BeautifulSoup(page.content,"html.parser")
        html = list(soup.children)[3]
        body = html.body
        section = body.find("section",class_="content")
        div_collapse = section.find_all("div",class_="collapse")
        id_zero = int([hid["id"] for hid in div_collapse][0])
        print(id_zero)
        if(id_zero > id_one):
            iter_ = id_zero-id_one
            card_link = section.find_all("a",class_="card-link")
            for i in range(0,iter_):
                msg_one = "Hello RGUKTIAN !!!"
                msg_two = "you have a new notice in hub regarding :)"
                card_info = card_link[i].text.replace("   ","").replace("&"," and ").strip()
                msg_three = "please visit hub for more info..."
                url="https://www.fast2sms.com/dev/bulkV2"
                message=f"{msg_one}\n{msg_two}\n\n{card_info}\n\n{msg_three}"
                number_one =#your number
                payload_one=f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number_one}'
                headers={"authorization":"your Api Authorization Key","Content-Type":"application/x-www-form-urlencoded"}
                response_one=requests.request("POST",url=url,data=payload_one,headers=headers)
                print(response_one.text)
            id_one = id_zero
    except:
        continue
