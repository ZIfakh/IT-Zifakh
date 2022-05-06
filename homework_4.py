import requests
import os
import json

directory_user_data = 'user_data'
directory_users = 'user_'
same_directory = 'user_data/user_'

os.mkdir(directory_user_data)
users = json.loads(requests.get('https://reqres.in/api/users?page=2').text)
user = users['data']

for i in range(len(user)):
    os.mkdir(same_directory + str(i))

    with open(f'user_{str(i)}.txt', 'w+') as file:
        file.write(f"Email: {str(user[i]['email'])}\t"
                   f"Имя: {str(user[i]['first_name'])}\t"
                   f"Фамилия: {str(user[i]['last_name'])}\t")
    os.replace(f'user_{str(i)}.txt', f'user_data/user_{str(i)}/user_{str(i)}.txt')

    with open(f"file_{str(i)}.jpg", 'wb') as file:
        response = requests.get(user[i]['avatar'])
        file.write(response.content)
    os.replace(f'file_{str(i)}.jpg', f'user_data/user_{str(i)}/file_{str(i)}.jpg')