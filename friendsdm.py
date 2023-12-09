import requests
import time

TOKEN = 'token-self' #token gir
headers = {
    'Authorization': f'{TOKEN}',
}
# Liste çekoz burda belirtıoz
response = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
if response.status_code == 200:
    friends_data = response.json()
    for friend in friends_data:
        #(type=1) ile beniö ekli arkadaslarmı cekdım
        if friend['type'] == 1:
            friend_id = friend['id']
            # dm belirlioz 
            dm_response = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipient_id': friend_id})
            if dm_response.status_code == 200:
                channel_id = dm_response.json()['id'] #jsondan kanalları dm atmak icin idleri cekıoz
                # yenı guncelleme sorunsali önemsiz bir kod ekledim kullanmıyor kod burayı ıstersen kaldır burayı veya biseyler eklersin diye bırakıom canım
                friend_username = friend.get('username', 'Belirsiz Kullanıcı')
                
                dm_send_response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json={'content': f'Yazacağın şey'}) #buraya ne yazmak ıstersen yaz dm geccegn seyi
                
                if dm_send_response.status_code == 200:
                    print(f"gönderildi  {friend_username}")
                else:
                    print(f"hata sanırım dm gecmisin yok {dm_send_response.status_code}")
            else:
                print(f"boş hata devam et: {dm_response.status_code}")
            
            time.sleep(5)  #burayı 5 önerilir
else:
    print(f"Captcha Error {response.status_code}")
    print(f"Capcap Falan {response.text}")
